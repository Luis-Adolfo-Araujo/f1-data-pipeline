# Job ETL to insert data in the postgres 
import pandas as pd

f1_df = pd.read_csv('../staging/drivers.csv')
print(f1_df.head())