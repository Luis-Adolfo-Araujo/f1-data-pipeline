# Job to normalize the data and create its tables in the data warehouse

# driver_number → position
# driver_number → team_name
# driver_number → lap_number
import sys
sys.path.insert(0, '/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline')

from datetime import datetime
import pandas as pd
from config import *
from sqlalchemy import create_engine

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")
# tables = ['drivers', 'position', 'pit']
# for i in range(len(tables)):
#     query = f"SELECT * FROM {tables[i]};"
#     df = pd.read_sql(query, engine)
#     df = df.drop_duplicates()
#     df.to_sql(f'{tables[i]}', engine, if_exists='replace', index=False)

# engine.dispose()

# Qual o historico de posições de max verstappen?