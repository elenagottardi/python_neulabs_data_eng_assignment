# SET ENVIRONMENT
# install pandas
import pandas as pd
from datetime import datetime

def main():

    ############
    # 1. EXTRACT

    print(f'Note: EXTRACT')
    df1 = pd.read_json('data/orders.json', lines=True)

    # create shipping_address composed column as dataframe
    dict_shipping_address = df1.ShippingAddress
    df_shipping_address = pd.DataFrame(columns=['StateOrRegion', 'PostalCode', 'City', 'CountryCode'])
    for key, value in dict_shipping_address.items():
        df_shipping_address = pd.concat([df_shipping_address, pd.DataFrame([value])], axis=0)

    # create order total composed column as dataframe
    dict_order_total = df1.OrderTotal
    df_order_total = pd.DataFrame(columns=['CurrencyCode', 'Amount'])
    for key, value in dict_order_total.items():
        df_order_total = pd.concat([df_order_total, pd.DataFrame([value])], axis=0)

    ##############
    # 2. TRANSFORM

    print(f'Note: TRANSFORM')

    # add new columns from shipping_address
    df_tot_00 = pd.merge(df1, df_shipping_address, left_index=True, right_index=True)
    # add new columns from order total
    df_tot = pd.merge(df_tot_00, df_order_total, left_index=True, right_index=True)
    # df_tot.head()

    # datetime
    df_tot['ShipDate'] = pd.to_datetime(df_tot['ShipDate'])
    df_tot['LatestShipDate'] = pd.to_datetime(df_tot['LatestShipDate'])
    df_tot['PurchaseDate'] = pd.to_datetime(df_tot['PurchaseDate'])
    df_tot['LastUpdateDate'] = pd.to_datetime(df_tot['LastUpdateDate'])
    # string
    df_tot['OrderStatus'] = df_tot['OrderStatus'].astype('string')
    df_tot['OrderType'] = df_tot['OrderType'].astype('string')
    df_tot['IsReplacementOrder'] = df_tot['IsReplacementOrder'].astype('string')
    df_tot['StateOrRegion'] = df_tot['StateOrRegion'].astype('string')
    df_tot['PostalCode'] = df_tot['PostalCode'].astype('string')
    df_tot['City'] = df_tot['City'].astype('string')
    df_tot['CountryCode'] = df_tot['CountryCode'].astype('string')
    df_tot['County'] = df_tot['County'].astype('string')
    df_tot['CurrencyCode'] = df_tot['CurrencyCode'].astype('string')
    # int
    df_tot['NumberOfItemsShipped'] = df_tot['NumberOfItemsShipped'].astype('int64')
    # float
    df_tot['Amount'] = df_tot['Amount'].astype('float64')

    # drop columns unused
    df_tot = df_tot.drop(columns=['0_x', '0_y', 'ShippingAddress', 'OrderTotal'])

    # remove duplicates
    df_tot_nodups = df_tot.drop_duplicates(keep='first').copy()

    # add Year column that refers to PurchaseDate
    df_tot_nodups['Year'] = df_tot_nodups['PurchaseDate'].dt.strftime('%Y').astype('int64')

    # add YearMonth column that refers to PurchaseDate
    df_tot_nodups['YearMonth'] = df_tot_nodups['PurchaseDate'].dt.strftime('%Y%m').astype('string')

    # add YearQuarter column that refers to PurchaseDate
    df_tot_nodups['YearQuarter'] = df_tot_nodups['PurchaseDate'].dt.strftime('%YQ').astype('string')

    # add YearWeek column that refers to PurchaseDate
    df_tot_nodups['Weekday'] = df_tot_nodups['PurchaseDate'].dt.dayofweek
    df_tot_nodups.info()

    #############################
    # 3. LOAD (DOWNLOAD AS CSV FILE)

    print(f'Note: LOAD')

    df_tot_nodups.to_csv('data_out.csv', index=False, encoding='utf-8')

# MAIN
if __name__ == '__main__':
    print(main())