from flask import Flask, render_template, request
import numpy as np
import joblib
import os

print("APP STARTED")

app = Flask(__name__)

# Load model safely
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "churn_model.pkl")

model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        tenure = float(request.form["tenure"])
        monthly = float(request.form["monthly_charges"])
        total = float(request.form["total_charges"])

        features = np.array([[tenure, monthly, total]])

        prediction = model.predict(features)[0]

        if prediction == 1:
            result = "⚠️ Customer is likely to churn"
        else:
            result = "✅ Customer is not likely to churn"

        return render_template(
            "index.html",
            prediction_text=result
        )

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)