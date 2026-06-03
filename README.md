# Customer Churn Prediction

## Project Overview

Customer Churn Prediction is a machine learning project that identifies customers who are likely to leave a telecom service. The project analyzes customer demographics, subscription details, billing information, and service usage patterns to understand churn behavior and support customer retention strategies.

Using classification techniques, the model learns from historical customer data and predicts whether a customer will churn. This helps businesses take proactive measures to improve customer satisfaction and reduce revenue loss.

---

## Dataset

The project uses the Telco Customer Churn dataset, which contains information about customer demographics, account tenure, internet services, billing methods, contract types, and monthly charges. The target variable is **Churn**, indicating whether a customer has left the service.

---

## Technologies Used

* Python
* Pandas & NumPy
* Matplotlib & Seaborn
* Scikit-learn
* Flask
* Jupyter Notebook

---

## Machine Learning Models

Two classification models were developed and evaluated for churn prediction. Logistic Regression achieved the highest accuracy and was selected as the final model for deployment.

* Logistic Regression Accuracy: **82.19%**
* Random Forest Accuracy: **79.21%**

---

## Key Insights

The analysis revealed that contract type, internet service type, online security, technical support, billing preferences, and payment methods significantly influence customer churn. Customers with long-term contracts showed lower churn rates, while customers using electronic check payments were more likely to leave the service.

---

## Project Workflow

Data Collection → Data Cleaning → Exploratory Data Analysis → Feature Encoding → Train-Test Split → Model Training → Model Evaluation → Model Saving → Flask Web Application → Deployment

---

## Conclusion

The developed churn prediction system successfully identifies customers at risk of leaving a telecom service. With an accuracy of over 82%, the model provides valuable insights that can help businesses improve customer retention and make data-driven decisions.

---

## Author

**Dasari Keerthana**
