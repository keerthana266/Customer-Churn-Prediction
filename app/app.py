print("APP STARTED")

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

model = joblib.load("models/churn_model.pkl")


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        tenure = float(request.form.get("tenure"))
        monthly = float(request.form.get("monthly_charges"))
        total = float(request.form.get("total_charges"))

        features = np.array([[tenure, monthly, total]])

        prediction = model.predict(features)[0]

        result = "Customer WILL CHURN ⚠️" if prediction == 1 else "Customer will NOT churn ✅"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"