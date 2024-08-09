import tensorflow as tf
from tensorflow.keras.models import load_model
import pandas as pd

# Load model
model = load_model('models/my_model.keras')

# Prediction function
def predict_real_time(new_data, feature_cols):
    X_new = new_data[feature_cols].values.reshape((1, new_data.shape[0], len(feature_cols)))
    prediction = model.predict(X_new)
    return prediction

if __name__ == "__main__":
    # Example usage
    new_data = pd.DataFrame({...})  # Replace with actual data
    feature_cols = ['sst', 'ssta', 'sst_avhrr_sst', 'anom']
    print(predict_real_time(new_data, feature_cols))
