import pickle
import pandas as pd
from fredapi import Fred
fred_key = "b0295abae73a8425886a7af979f3a1d7"
fred = Fred(api_key=fred_key)
# fred_data = pd.DataFrame(fred.get_series('WTISPLC'), columns=['WTISPLC']);
datasets_fred = [ 'CPIENGSL', 'CAPG211S', 'CAPUTLG211S', 'IPG211S', 'IPG211111CN', 'INDPRO', 'IPN213111N', 'PCU211211', 'WTISPLC']
fred_data = [pd.DataFrame(fred.get_series(series_id), columns=[series_id]) for series_id in datasets_fred]
def clean_fred_data (df):
    df.index = pd.to_datetime(df.index)
    print(df.head())
    return df[df.index> '2003-01-01']
fred_data_cleaned = list(map(clean_fred_data, fred_data))

with open('FRED_DATA.pkl', 'wb') as f:
    pickle.dump(fred_data_cleaned, f)