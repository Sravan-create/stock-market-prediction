import requests  # Importing requests to handle API calls
import pandas as pd  # Importing pandas for data manipulation and analysis

def fetch_crypto_data(crypto_pair, start_date):
    # Constructing the API URL to fetch historical crypto data
    url = f"https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000&toTs=-1"
    
    # Setting up the headers with the API key for authorization
    headers = {
        'authorization': 'Apikey YOUR_API_KEY'  # Replace 'YOUR_API_KEY' with your actual API key
    }
    
    # Making a GET request to the API
    response = requests.get(url, headers=headers)
    if response.status_code != 200:  # Check if the response status is not OK
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None  # Exit if the data fetch fails

    try:
        # Parsing the JSON response into a Python dictionary
        data = response.json()
        # Extracting the 'Data' section, which contains the historical prices
        prices = data['Data']['Data']
        
        # Creating a DataFrame from the prices data
        df = pd.DataFrame(prices)
        # Converting the 'time' column from UNIX timestamp to a readable date
        df['Date'] = pd.to_datetime(df['time'], unit='s').dt.date
        # Renaming columns to more familiar financial terms
        df = df.rename(columns={'open': 'Open', 'high': 'High', 'low': 'Low', 'close': 'Close'})
        
        print("Data fetched and processed successfully!")
        # Returning only the relevant columns for further analysis
        return df[['Date', 'Open', 'High', 'Low', 'Close']]
    except Exception as e:
        # Catching any exceptions and printing the error message
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    # Fetching the crypto data and printing basic information if successful
    crypto_data = fetch_crypto_data("BTC/USD", "2023-01-01")
    if crypto_data is not None:
        print(crypto_data.shape)  # Printing the shape of the DataFrame
        print(crypto_data.head())  # Displaying the first few rows of the DataFrame
