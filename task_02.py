# SET ENVIRONMENT

# pip install pandas
import pandas as pd
from datetime import datetime

# EXTRACT
# from json file to dataframe
def json_to_dataframe():
    print(f'Note: from json to dataframe')
    df = pd.read_json('data/orders.json', lines=True)
    df.info()
    return df

# TRANSFORM
def fix_column_type(df):
    print(f'Note: fix column type')
    # datetime
    df['ShipDate'] = pd.to_datetime(df['ShipDate'])
    df['LatestShipDate'] = pd.to_datetime(df['LatestShipDate'])
    df['PurchaseDate'] = pd.to_datetime(df['PurchaseDate'])
    # string
    df['OrderStatus'] = df['OrderStatus'].astype('string')
    df['OrderType'] = df['OrderType'].astype('string')
    df['IsReplacementOrder'] = df['IsReplacementOrder'].astype('string')
    # int
    df['NumberOfItemsShipped'] = df['NumberOfItemsShipped'].astype('int64')
    # dict
    # df['ShippingAddress'] = df['ShippingAddress'].to_list()
    df.info()

# MAIN
if __name__ == '__main__':
    fix_column_type(json_to_dataframe())