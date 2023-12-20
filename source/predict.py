from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('logistic_regression_model.joblib')

# load predict data
df_predict = pd.read_csv('customer_churn_predict.csv')


@app.route('/predict', methods=['POST'])
def predict():
    prediction = model.predict(df_predict)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
