import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model

# Load the model
model = load_model('models/my_model.keras')

# Streamlit app for real-time prediction
st.title('Typhoon Prediction Dashboard')

def predict_real_time(new_data, feature_cols):
    X_new = new_data[feature_cols].values.reshape((1, new_data.shape[0], len(feature_cols)))
    prediction = model.predict(X_new)
    return prediction

# Upload data
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    new_data = pd.read_csv(uploaded_file)
    feature_cols = ['sst', 'ssta', 'sst_avhrr_sst', 'anom']
    predictions = predict_real_time(new_data, feature_cols)
    st.write("Predictions:", predictions)
