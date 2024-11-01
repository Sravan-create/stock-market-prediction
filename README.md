# stock-market-prediction
Cryptocurrency price prediction project using Python: Includes data retrieval from Crypto Compare API, metrics calculation, and a linear regression model to forecast future price movements.

# Cryptocurrency Price Prediction

This project uses Python to predict future price movements of Bitcoin using historical data retrieved from the CryptoCompare API. It includes data retrieval, feature engineering, and machine learning model training for forecasting.

## Project Overview
The goal of this project is to make predictions about the percentage difference from future highs and lows of Bitcoin prices. The project is divided into the following main parts:
1. **Data Retrieval**: Using the CryptoCompare API to fetch historical price data.
2. **Metrics Calculation**: Processing the data to extract meaningful features for prediction.
3. **Model Training**: Building and evaluating machine learning models to make predictions.

## Project Structure
- `data_retrieval.py`: Script for fetching historical cryptocurrency data using the CryptoCompare API.
- `metric_calculations.py`: Script for calculating important metrics, such as days since last high/low and percentage differences.
- `ml_model.py`: Script for training a Linear Regression model to predict future price differences and evaluating the model's performance.
- `crypto_data.xlsx`: Excel file containing the processed data used for model training and analysis.
- `project_explanation.txt`: Detailed explanation of the project, including challenges and solutions.
- **Loom Video Link**: A video explanation of the project (provided in the text document).

## Setup and Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/yourusername/crypto-price-prediction.git
2. pip install -r requirements.txt
