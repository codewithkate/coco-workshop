import pandas as pd
import snowflake.connector
import os

USER = os.environ.get('SNOWFLAKE_USER')
PASSWORD = os.environ.get('SWOWFLAKE_PASSWORD')
ACCOUNT = os.environ.get('SWOWFLAKE_ACCOUNT')
WAREHOUSE = os.environ.get('SWOWFLAKE_WAREHOUSE')
DATABASE = 'TIL_PLAYGROUND'
SCHEMA = 'PREPPIN_DATA_INPUTS'

conn = snowflake.connector.connect(
    user=USER,
    password=PASSWORD,
    account=ACCOUNT,
    warehouse=WAREHOUSE,
    database=DATABASE,
    schema=SCHEMA
)

pd2023_wk01 = pd.read_sql(
    "SELECT * FROM TIL_PLAYGROUND.PREPPIN_DATA_INPUTS.PD2023_WK01",
    conn
)

# Enter your code here, name the final dataframes as 'output_1', 'output_2', 'output_3'   
# 1. Total Values of Transactions by each bank
df1 = pd2023_wk01[['transaction_code', 'value']]



#1. Total Values of Transactions by each bank
output_1 = '1'
output_2 = '2'
output_3 = '3'

# pd2023_wk01["online_or_in_person"] = pd2023_wk01["online_or_in_person"].map({1: "Online", 2: "In-Person"})
# pd2023_wk01["transaction_date"] = pd2023_wk01.to_datetime(df["transaction_date"], format="%d/%m/%Y %H:%M:%S")
# pd2023_wk01["day_of_week"] = pd2023_wk01["transaction_date"].dt.day_name()

print(output_1.to_string(index=False))
print(output_2.to_string(index=False))
print(output_3.to_string(index=False))
conn.close()