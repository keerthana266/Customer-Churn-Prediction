print("APP STARTED")

from flask import Flask, render_template, request
import numpy as np
import joblib

app = Flask(__name__)

# Load your trained model
model = joblib.load("models/churn_model.pkl")


# Home route
@app.route("/")
def home():
    return render_template("index.html")


# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    try:
        print("Prediction request received")

        # Get values from HTML form
        tenure = float(request.form["tenure"])
        monthly_charges = float(request.form["monthly_charges"])
        total_charges = float(request.form["total_charges"])

        # Prepare input for model
        features = np.array([[tenure, monthly_charges, total_charges]])

        # Predict
        prediction = model.predict(features)[0]

        # Convert result
        result = "Customer WILL CHURN ⚠️" if prediction == 1 else "Customer will NOT churn ✅"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"


# Run app
if __name__ == "__main__":
    app.run(debug=True)