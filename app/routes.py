from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, ClaimsData, LoginHistory
from app.forms import RegistrationForm, LoginForm, ClaimsDataForm
from app import db
from app.ml_model import InsuranceModel

main = Blueprint('main', __name__)
model = InsuranceModel()

@main.route('/')
def index():
    return render_template('base.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.predict'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('🎉 Welcome aboard! Your account has been created successfully!', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.predict'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        success = user and user.check_password(form.password.data)
        
        # Create login history entry
        login_entry = LoginHistory(
            user_id=user.id if user else None,
            ip_address=request.remote_addr,
            user_agent=request.user_agent.string,
            success=success
        )
        db.session.add(login_entry)
        db.session.commit()
        
        if success:
            login_user(user)
            flash('👋 Welcome back! You have been logged in successfully!', 'success')
            return redirect(url_for('main.predict'))
        flash('❌ Invalid username or password', 'error')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('👋 You have been logged out successfully!', 'info')
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    # Get user's prediction history
    user_predictions = ClaimsData.query.filter_by(user_id=current_user.id).order_by(ClaimsData.id.desc()).all()
    
    # Calculate some statistics
    total_predictions = len(user_predictions)
    avg_cost = sum(pred.charges for pred in user_predictions) / total_predictions if total_predictions > 0 else 0
    latest_prediction = user_predictions[0] if user_predictions else None
    
    return render_template('dashboard.html', 
                         predictions=user_predictions,
                         total_predictions=total_predictions,
                         avg_cost=avg_cost,
                         latest_prediction=latest_prediction)

@main.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    form = ClaimsDataForm()
    if form.validate_on_submit():
        try:
            data = {
                'age': form.age.data,
                'sex': form.sex.data,
                'bmi': form.bmi.data,
                'children': form.children.data,
                'smoker': form.smoker.data,
                'region': form.region.data
            }
            
            prediction = model.predict(data)
            
            claims_data = ClaimsData(
                user_id=current_user.id,
                age=data['age'],
                sex=data['sex'],
                bmi=data['bmi'],
                children=data['children'],
                smoker=data['smoker'] == 'yes',
                region=data['region'],
                charges=prediction
            )
            db.session.add(claims_data)
            db.session.commit()
            
            model.retrain_with_all_data()
            
            flash(f'🎯 Prediction calculated successfully! Your estimated insurance cost is ${prediction:,.2f}', 'success')
            
            return render_template('predict.html', 
                                 form=None,
                                 prediction=prediction, 
                                 data=data,
                                 show_results=True)
        except Exception as e:
            flash(f'❌ Error making prediction: {str(e)}', 'error')
            return render_template('predict.html', form=form, show_results=False)
            
    return render_template('predict.html', form=form, show_results=False)

@main.route('/login-history')
@login_required
def login_history():
    history = LoginHistory.query.filter_by(user_id=current_user.id)\
        .order_by(LoginHistory.login_time.desc()).all()
    return render_template('login_history.html', history=history) 