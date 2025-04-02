from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, NumberRange
from app.models import User

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already registered. Please use a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class ClaimsDataForm(FlaskForm):
    age = IntegerField('Age', validators=[
        DataRequired(message="Age is required"),
        NumberRange(
            min=1, 
            max=70, 
            message="Age must be between 1 and 70 years"
        )
    ])
    sex = SelectField('Sex', 
                     choices=[('male', 'Male'), ('female', 'Female')], 
                     validators=[DataRequired(message="Please select your gender")])
    bmi = FloatField('BMI', validators=[
        DataRequired(message="BMI is required"),
        NumberRange(
            min=20, 
            max=50, 
            message="BMI must be between 20 and 50"
        )
    ])
    children = IntegerField('Number of Children', validators=[
        DataRequired(message="Number of children is required"),
        NumberRange(
            min=0, 
            max=5, 
            message="Number of children must be between 0 and 5"
        )
    ])
    smoker = SelectField('Smoker', 
                        choices=[('yes', 'Yes'), ('no', 'No')], 
                        validators=[DataRequired(message="Please select smoking status")])
    region = SelectField('Region', 
                        choices=[
                            ('northeast', 'Northeast'),
                            ('northwest', 'Northwest'),
                            ('southeast', 'Southeast'),
                            ('southwest', 'Southwest')
                        ],
                        validators=[DataRequired(message="Please select your region")])
    submit = SubmitField('Calculate Insurance Cost')

    def validate_bmi(self, bmi):
        if bmi.data < 20:
            raise ValidationError('BMI must be at least 20')
        elif bmi.data > 50:
            raise ValidationError('Please verify your BMI. Values above 50 are unusual.') 