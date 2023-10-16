# Import necessary libraries
import joblib
from flask import Flask, request, jsonify

# Create a Flask application
app = Flask(__name__)

# Load the pickled model
loaded_model = joblib.load('nutricow.pkl')

# Define an endpoint for making predictions
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data as JSON
        input_data = request.get_json()

        # Perform any necessary data preprocessing based on your model's requirements
        # Ensure the input data is in the correct format for prediction

        # Make predictions using the loaded model
        predicted_values = loaded_model.predict(input_data)

        # Return the prediction results as JSON
        return jsonify({'prediction': predicted_values.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main':
    # Run the Flask application
    app.run(host='0.0.0.0', port=5000)
