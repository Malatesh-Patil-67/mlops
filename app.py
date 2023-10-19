from flask import Flask, request, jsonify
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler


# Load the trained model
model = load('trained_model.joblib')

app = Flask(__name__)

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    
    # Get the data from the request
    data = request.json
    # Convert the input data values to a list
    data = list(data.values())

    # Convert the data to a numpy array
    input_data = np.array(data).reshape(1, -1)

    # Load the scaler and transform the input data
    scaler = StandardScaler()
    input_data = scaler.fit_transform(input_data)

    # Make predictions using the loaded model
    predictions = model.predict(input_data)
    # Print the predictions
    print("Predictions:", predictions.tolist())


    # Return the predictions as a JSON response
    return jsonify({'predictions': predictions.tolist()})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)  # Change 8081 to your desired port number
