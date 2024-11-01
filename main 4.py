from data_retrieval import fetch_crypto_data  # Importing the function to fetch cryptocurrency data
from metric_calculations import calculate_metrics  # Importing the function to calculate metrics
from ml_model import train_model, predict_outcomes  # Importing the functions to train the model and make predictions

# Step 1: Fetch historical cryptocurrency data
crypto_data = fetch_crypto_data("bitcoin", "2023-01-01")  # Fetching data for Bitcoin from the specified start date

# Step 2: Calculate metrics needed for the model
processed_data = calculate_metrics(crypto_data, variable1=7, variable2=5)  # Calculating metrics with a 7-day historical window and a 5-day future window

# Step 3: Train the machine learning models using the processed data
model_high, model_low = train_model(processed_data, variable1=7, variable2=5)  # Training models to predict future high and low differences

# Step 4: Define the feature names for the new data input
feature_names = [
    'Days_Since_High_Last_7_Days', '%_Diff_From_High_Last_7_Days',
    'Days_Since_Low_Last_7_Days', '%_Diff_From_Low_Last_7_Days'
]  # The names of the features we use for predictions

# Step 5: Prepare new data for prediction
new_data = [7, -0.9, 3, 1.5]  # Example input data: days since last high/low and percentage differences

# Step 6: Use the trained models to make predictions
high_pred, low_pred = predict_outcomes(model_high, model_low, new_data, feature_names)  # Making predictions for future high and low differences

# Step 7: Print the predicted values
print(f"Predicted % Difference from Future High: {high_pred}")  # Output the prediction for future high difference
print(f"Predicted % Difference from Future Low: {low_pred}")  # Output the prediction for future low difference

#processed_data.to_excel("crypto_data.xlsx", index=False, sheet_name="BTC-USD")