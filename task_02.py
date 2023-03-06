# SET ENVIRONMENT

# pip install pandas
import pandas as pd

# EXTRACT
# from json file to dataframe
def json_to_dataframe():
    print(f'Note: from json to dataframe')
    df = pd.read_json('data/orders.json', lines=True)
    df.info()

# MAIN
if __name__ == '__main__':
    json_to_dataframe()