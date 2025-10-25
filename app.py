# app.py

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load data
data = pd.read_csv("house.csv")

# Encode area_type (Urban/Rural)
le = LabelEncoder()
data['area_type_encoded'] = le.fit_transform(data['area_type'])

# Features and target
X = data[['area_type_encoded', 'bedrooms', 'area_sqft']]
y = data['price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Streamlit UI
st.set_page_config(page_title="House Price Prediction", layout="centered")

st.markdown("""
    <style>
    h1 { text-align: center; color: #4B9CD3; }
    .stButton>button {
        background-color: #4B9CD3;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
    }
    .result {
        background-color: #d1e7dd;
        color: #0f5132;
        font-size: 20px;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🏠 Smart House Price Predictor</h1>", unsafe_allow_html=True)

with st.form("prediction_form"):
    area_type_input = st.selectbox("📍 Select Area Type", ['Urban', 'Rural'])
    area_sqft_input = st.number_input("📐 Enter Area (sq ft)", min_value=100, max_value=100000, step=100)
    bedrooms_input = st.slider("🛏️ Number of Bedrooms", 1, 10, 3)
    submitted = st.form_submit_button("Predict Price")

if submitted:
    # Convert area type to encoded format
    area_type_encoded = le.transform([area_type_input])[0]
    input_features = np.array([[area_type_encoded, bedrooms_input, area_sqft_input]])
    predicted_price = model.predict(input_features)[0]
    st.markdown(f"<div class='result'>Estimated House Price: <strong>₹{int(predicted_price):,}</strong></div>", unsafe_allow_html=True)
