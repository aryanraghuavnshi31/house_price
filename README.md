# house_price
House Price Prediction Project

Overview

This project is a web-based application that predicts house prices based on user inputs. It utilizes a machine learning model trained using historical data to estimate house prices based on house size, number of bedrooms, and location.

Technologies Used

Flask: A lightweight web framework for Python to handle the backend.

Scikit-Learn: Used for building and training the machine learning model.

Pandas: For data manipulation and preprocessing.

Bootstrap: To enhance the frontend user interface.

Pickle: For saving and loading the trained model.

Project Components

app(1).py: The main Flask application that handles user requests and returns predictions.

index(1).html: The frontend interface for user input and displaying predictions.

aryamodel.pkl: The trained machine learning model saved in pickle format.

house_price.ipynb: A Jupyter Notebook containing data preprocessing, model training, and evaluation steps.

How It Works

The user enters house details (size, bedrooms, and location) through a web form.

The Flask backend processes the input and applies label encoding for the location field using LabelEncoder.

The trained machine learning model predicts the house price using input features.

The predicted price is displayed on the frontend.

Error handling is incorporated to return JSON responses in case of invalid inputs.
