import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import os
from app import db
from app.models import ClaimsData
from flask import current_app

class InsuranceModel:
    def __init__(self):
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.le_sex = LabelEncoder()
        self.le_region = LabelEncoder()
        
        # Load initial data from CSV
        csv_path = r"C:\Users\psspo\Downloads\insurance (1).csv"
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"CSV file not found at {csv_path}")
            
        self.initial_data = pd.read_csv(csv_path)
        print("Initial data loaded successfully. Shape:", self.initial_data.shape)
        
        # Initialize encoders with all possible values
        self.le_sex.fit(self.initial_data['sex'])
        self.le_region.fit(self.initial_data['region'])
        
        # Train only with CSV data initially
        self.train_with_csv_data()

    def train_with_csv_data(self):
        """Train initial model with CSV data only"""
        print("Training initial model with CSV data...")
        df = self.prepare_data(self.initial_data)
        self._train_model(df)

    def _train_model(self, df):
        """Internal method to train model with prepared data"""
        X = df[['age', 'sex_encoded', 'bmi', 'children', 'smoker', 'region_encoded']]
        y = df['charges']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        train_score = self.model.score(X_train, y_train)
        test_score = self.model.score(X_test, y_test)
        print(f"Model R² score on training data: {train_score:.3f}")
        print(f"Model R² score on test data: {test_score:.3f}")
        
        features = ['age', 'sex', 'bmi', 'children', 'smoker', 'region']
        importances = self.model.feature_importances_
        print("\nFeature Importances:")
        for feature, importance in zip(features, importances):
            print(f"{feature}: {importance:.3f}")

    def prepare_data(self, data):
        if isinstance(data, dict):
            df = pd.DataFrame([data])
        else:
            df = pd.DataFrame(data)
        
        df['smoker'] = (df['smoker'] == 'yes').astype(int)
        df['sex_encoded'] = self.le_sex.transform(df['sex'])
        df['region_encoded'] = self.le_region.transform(df['region'])
        
        return df

    def predict(self, data):
        """Make prediction for new data"""
        print("Making prediction for data:", data)
        df = self.prepare_data(data)
        X = df[['age', 'sex_encoded', 'bmi', 'children', 'smoker', 'region_encoded']]
        prediction = self.model.predict(X)[0]
        print("Prediction result:", prediction)
        return prediction

    def retrain_with_all_data(self):
        """Retrain model with both CSV and database data"""
        try:
            # Get data from database
            claims_data = ClaimsData.query.all()
            if not claims_data:
                print("No additional data in database")
                return
                
            real_time_data = []
            for claim in claims_data:
                real_time_data.append({
                    'age': claim.age,
                    'sex': claim.sex,
                    'bmi': claim.bmi,
                    'children': claim.children,
                    'smoker': 'yes' if claim.smoker else 'no',
                    'region': claim.region,
                    'charges': claim.charges
                })
            
            # Combine with initial data
            real_time_df = pd.DataFrame(real_time_data)
            combined_data = pd.concat([self.initial_data, real_time_df], ignore_index=True)
            print("Combined data shape:", combined_data.shape)
            
            # Train with combined data
            print("Retraining model with all data...")
            df = self.prepare_data(combined_data)
            self._train_model(df)
            
        except Exception as e:
            print(f"Error during retraining: {str(e)}") 