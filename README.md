<div align="center">
  <h1>🫀 HeartIQ Engine</h1>
  <p><strong>Advanced Machine Learning Cardiology Predictor with an Ultra-Premium Glassmorphism Interface</strong></p>
  
  [![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
  [![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
  [![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![UI](https://img.shields.io/badge/UI-Glassmorphism-purple?style=for-the-badge)](#)
</div>

<br />

## 📋 Overview
**HeartIQ Engine** is an end-to-end intelligent predictive diagnostic system. It leverages algorithmic hyperparameter optimization across multiple machine learning models (Random Forest, Gradient Boosting, SVM, Logistic Regression) to assess the risk of cardiovascular presence based on standard clinical metrics. It automatically selects the optimal champion model, achieving **~90%+ prediction accuracy**.

The predictor interfaces with users through a custom-built, ultra-premium web UI engineered with deep `glassmorphism`, dynamic `CSS3` animations, and a seamless backend integration via a RESTful `Flask` server.

---

## ✨ Features

- **🏆 Auto-Optimized ML Pipeline:** Utilizes `GridSearchCV` on scaled medical data to simultaneously test Logistic Regression, SVC, Random Forest, and Gradient Boosting before automatically saving the best performer.
- **⚡ Flask REST API Engine:** A lightweight, non-blocking Python backend ready to receive `JSON` requests and compute complex biometrics in milliseconds.
- **💎 Ultra-Premium UI:** 
  - Dynamic ambient mesh backgrounds and floating organic blobs.
  - Inter & Outfit typography for modern readability.
  - Beautiful neon interactive inputs with animated focal-glow transitions.
  - Interactive prediction cards with an animated "Confidence Score" indicator.

---

## 🛠️ Technology Stack
- **Machine Learning**: `scikit-learn`, `pandas`, `numpy`, `joblib`
- **Backend API**: `Python`, `Flask`, `Flask-CORS`
- **Frontend & UI Elements**: `HTML5`, Vanilla `CSS3`, `JavaScript (ES6+)`, `FontAwesome v6`

---

## 🚀 Quick Start Guide

### 1. Prerequisites
Ensure you have `Python 3.8+` installed. Navigate into your project directory using a terminal (e.g., PowerShell or terminal of your choice).

### 2. Install Dependencies
Install all required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Engine Initialization (Train the Model)
Train the predictive models and let the system find the best configuration automatically. This will generate the `heart_disease_model.pkl` and `scaler.pkl` files natively.
```bash
python train_model.py
```
*Expected Output: Logs tracking training evaluation logic for each algorithm, terminating with the Best Model Selection parameters.*

### 4. Launch the Web Environment
Start the development server bridging the predictive model and the frontend GUI:
```bash
python server.py
```

### 5. Access the Platform
Navigate to the hosted URL on your local browser:
**`http://127.0.0.1:5000`**

---

## 📊 The Dataset
The dataset utilized is standard formatted medical cardiology parameters. Models evaluate metrics strictly across the following 13 biological indicators:
- **Demographics**: `Age`, `Sex`
- **Vitals**: `Resting BP`, `Max Heart Rate`, `Serum Cholesterol`
- **Medical Tests**: `Chest Pain Type`, `Fasting Blood Sugar`, `Resting ECG`, `Exercise Angina`, `ST Depression (Oldpeak)`, `Slope of ST`, `Fluoroscopy Vessels`, `Thallium Scan Results`

---

## 👨‍💻 Architecture Synopsis
1. Client interacts with our premium `glass-paneled` GUI.
2. Form submission generates an asynchronous `POST JSON` request to the Flask server via `fetch()` API.
3. The Flask router decodes parameters, invokes the `joblib` memory loaded `StandardScaler` to align data scales with the trained snapshot.
4. Scale integers are fed into the highest-accuracy predictor model.
5. Probabilities and logical classifications traverse back to the client.
6. The `overlay UI` triggers an engaging diagnostic report card.

<br>

<div align="center">
  <i>Developed to merge rigorous Data Science with cutting-edge Frontend aesthetics.</i>
</div>
