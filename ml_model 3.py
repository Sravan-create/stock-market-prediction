from sklearn.model_selection import train_test_split  # For splitting the data into training and testing sets
from sklearn.linear_model import LinearRegression  # The regression model used to make predictions
from sklearn.metrics import mean_absolute_error  # Metric to evaluate the model's performance
import pandas as pd  # For data manipulation

def train_model(data, variable1=7, variable2=5):
    # Defining the feature columns dynamically based on variable1
    X_columns = [
        f'Days_Since_High_Last_{variable1}_Days', f'%_Diff_From_High_Last_{variable1}_Days',
        f'Days_Since_Low_Last_{variable1}_Days', f'%_Diff_From_Low_Last_{variable1}_Days'
    ]
    # Target columns for predicting the percentage difference from future highs and lows
    y_high_column = f'%_Diff_From_High_Next_{variable2}_Days'
    y_low_column = f'%_Diff_From_Low_Next_{variable2}_Days'

    # Dropping rows with missing values to ensure the model has complete data to work with
    data = data.dropna(subset=X_columns + [y_high_column, y_low_column])

    # Setting up the input features (X) and target variables (y)
    X = data[X_columns]
    y_high = data[y_high_column]
    y_low = data[y_low_column]

    # Splitting the data into 80% training and 20% testing
    X_train, X_test, y_high_train, y_high_test, y_low_train, y_low_test = train_test_split(
        X, y_high, y_low, test_size=0.2, random_state=42
    )

    # Training linear regression models to predict high and low percentage differences
    model_high = LinearRegression().fit(X_train, y_high_train)
    model_low = LinearRegression().fit(X_train, y_low_train)

    # Making predictions on the test set
    y_high_pred = model_high.predict(X_test)
    y_low_pred = model_low.predict(X_test)
    
    # Calculating the Mean Absolute Error (MAE) for each model
    high_error = mean_absolute_error(y_high_test, y_high_pred)
    low_error = mean_absolute_error(y_low_test, y_low_pred)

    # Printing the MAE to see how well the models are performing
    print(f"High Prediction MAE: {high_error}")
    print(f"Low Prediction MAE: {low_error}")

    # Returning the trained models
    return model_high, model_low

def predict_outcomes(model_high, model_low, new_data, feature_names):
    # Creating a DataFrame for the new data using the same feature names as the training data
    new_data_df = pd.DataFrame([new_data], columns=feature_names)
    
    # Using the models to make predictions for future high and low percentage differences
    high_prediction = model_high.predict(new_data_df)[0]
    low_prediction = model_low.predict(new_data_df)[0]
    
    # Returning the predicted values
    return high_prediction, low_prediction
