from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for your JS frontend

model_path = 'heart_disease_model.pkl'
scaler_path = 'scaler.pkl'

# Ensure the model is trained before starting the server
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    print("Warning: Model or scaler not found. Please run 'python train_model.py' first.")
else:
    # Load the trained model and scaler
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    print("Model and scaler successfully loaded into memory.")

@app.route('/')
def serve_frontend():
    """Serve the main index.html file to automatically open the frontend."""
    if os.path.exists('index.html'):
        return send_from_directory('.', 'index.html')
    elif os.path.exists('templates/index.html'):
        return send_from_directory('templates', 'index.html')
    return "Warning: index.html not found! Please make sure it's in the project folder."

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files like style.css, app.js, images, etc."""
    if os.path.exists(filename):
        return send_from_directory('.', filename)
    elif os.path.exists(os.path.join('templates', filename)):
        return send_from_directory('templates', filename)
    return "File not found", 404

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        
        # Extract features from incoming JSON exactly in the order the model was trained
        # Expected features: Age, Sex, Chest pain type, BP, Cholesterol, FBS over 120, 
        # EKG results, Max HR, Exercise angina, ST depression, Slope of ST, Number of vessels fluro, Thallium
        features = [
            float(data['age']),
            float(data['sex']),
            float(data['cp']),
            float(data['trestbps']),
            float(data['chol']),
            float(data['fbs']),
            float(data['restecg']),
            float(data['thalach']),
            float(data['exang']),
            float(data['oldpeak']),
            float(data['slope']),
            float(data['ca']),
            float(data['thal'])
        ]
        
        # Scale the features
        features_scaled = scaler.transform([features])
        
        # Make Prediction
        prediction = model.predict(features_scaled)[0]
        
        # Calculate probability/confidence score
        probabilities = model.predict_proba(features_scaled)[0]
        confidence = probabilities[prediction] * 100
        
        return jsonify({
            'prediction': int(prediction),  # 1 for Presence, 0 for Absence
            'confidence': float(confidence)
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    print("Starting Flask API Server on http://127.0.0.1:5000 ...")
    app.run(debug=True, port=5000)
