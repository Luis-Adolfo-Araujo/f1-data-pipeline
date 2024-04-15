# Job ETL to insert data in the postgres 
import pandas as pd
from sqlalchemy import create_engine
from config import *

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")
conn = engine.connect()

print(conn)