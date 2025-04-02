from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler, LabelEncoder

app = Flask(__name__)

# Load the trained model
with open('aryamodel.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Initialize label encoder for 'Location' transformation
label_encoder = LabelEncoder()

# Define the homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from the form
        house_size = float(request.form['house_size'])
        bedrooms = int(request.form['bedrooms'])
        location = request.form['location']

        # Label encode the location (assuming the model uses encoded locations)
        location_encoded = label_encoder.fit_transform([location])[0]  # We assume the model uses encoded locations

        # Create a DataFrame for the input
        input_data = pd.DataFrame([[house_size, bedrooms, location_encoded]],
                                 columns=['House Size (sqft)', 'Bedrooms', 'Location'])

        

        # Scale the house size feature (assuming 'House Size (sqft)' was scaled during training)
        

        # Ensure the model gets the same set of features (e.g., Location_1, Location_2, etc.)
        # Add missing columns with zero values if needed
        missing_cols = set(model.feature_names_in_) - set(input_data.columns)
        for col in missing_cols:
            input_data[col] = 0

        # Reorder the columns to match the model's expected feature order
        input_data = input_data[model.feature_names_in_]

        # Make the prediction
        predicted_price = model.predict(input_data)[0]

        # Render the prediction result
        return render_template('index.html', prediction=f"The predicted price is: ${predicted_price:.2f}")

    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
