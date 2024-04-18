# Job ETL to insert data in the postgres 
import os
import sys
sys.path.insert(0, '/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline')

import pandas as pd
from config import *
from sqlalchemy import create_engine

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")
conn = engine.connect()

for file in os.listdir(STAGING):
    file_path = os.path.join(STAGING, file)
    if file.endswith('.csv'):
        df = pd.read_csv(file_path)
        table_name = file.replace('.csv', '')
        df.to_sql(table_name, engine, if_exists='append', index=False)

print("Data was properly inserted in the database.")
engine.dispose()