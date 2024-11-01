import pandas as pd

def calculate_metrics(data, variable1, variable2):
    # Ensure 'Date' is a datetime column for date calculations
    data['Date'] = pd.to_datetime(data['Date'])

    # Historical high/low prices over the past {variable1} days
    data[f'High_Last_{variable1}_Days'] = data['High'].rolling(window=variable1).max()
    data[f'Low_Last_{variable1}_Days'] = data['Low'].rolling(window=variable1).min()
    
    # Days since last high/low
    data[f'Days_Since_High_Last_{variable1}_Days'] = (
        data['Date'] - data['Date'][data['High'] == data[f'High_Last_{variable1}_Days']].reindex_like(data).ffill()
    )
    data[f'Days_Since_High_Last_{variable1}_Days'] = data[f'Days_Since_High_Last_{variable1}_Days'].dt.days

    data[f'Days_Since_Low_Last_{variable1}_Days'] = (
        data['Date'] - data['Date'][data['Low'] == data[f'Low_Last_{variable1}_Days']].reindex_like(data).ffill()
    )
    data[f'Days_Since_Low_Last_{variable1}_Days'] = data[f'Days_Since_Low_Last_{variable1}_Days'].dt.days

    # % Difference from Historical High/Low
    data[f'%_Diff_From_High_Last_{variable1}_Days'] = ((data['Close'] - data[f'High_Last_{variable1}_Days']) / data[f'High_Last_{variable1}_Days']) * 100
    data[f'%_Diff_From_Low_Last_{variable1}_Days'] = ((data['Close'] - data[f'Low_Last_{variable1}_Days']) / data[f'Low_Last_{variable1}_Days']) * 100
    
    # Future high/low prices over the next {variable2} days
    data[f'High_Next_{variable2}_Days'] = data['High'].shift(-variable2).rolling(window=variable2).max()
    data[f'Low_Next_{variable2}_Days'] = data['Low'].shift(-variable2).rolling(window=variable2).min()
    
    # % Difference from Future High/Low
    data[f'%_Diff_From_High_Next_{variable2}_Days'] = ((data['Close'] - data[f'High_Next_{variable2}_Days']) / data[f'High_Next_{variable2}_Days']) * 100
    data[f'%_Diff_From_Low_Next_{variable2}_Days'] = ((data['Close'] - data[f'Low_Next_{variable2}_Days']) / data[f'Low_Next_{variable2}_Days']) * 100
    
    return data
