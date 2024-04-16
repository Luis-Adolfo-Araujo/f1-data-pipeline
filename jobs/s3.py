# Job to normalize the data and create its tables in the data warehouse

import sys
sys.path.insert(0, '/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline')

import pandas as pd
from config import *
from sqlalchemy import create_engine
from scipy.stats import shapiro
import matplotlib.pyplot as plt

engine = create_engine(f"postgresql://{PG_USER}:{PG_PASS}@{PG_HOST}:{PG_PORT}/{PG_DB}")

def remove_outliers(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return data[(data >= lower) & (data <= upper)]

def convert_to_seconds(time_str):
    try:
        minutes, seconds = time_str.split(':')
        seconds, milliseconds = seconds.split('.')
        total_seconds = int(minutes) * 60 + int(seconds) + int(milliseconds) / 1000
        return total_seconds
    except:
        return None


alpha = 0.05
tables = {'pit_stops': 'duration', 'qualifying': 'q1', 'qualifying': 'q2', 'qualifying': 'q3'}
for k, v in tables.items():
    query = f"SELECT {v} FROM {k};"
    df = pd.read_sql(query, engine)

    if k == 'pit_stops':
        df[v] = pd.to_numeric(df[v], errors='coerce')
    else:
        df[v] = df[v].apply(convert_to_seconds)
    df = df.dropna(subset=[v])
    print(df)
    stat, p = shapiro(df[v])
    print(f"Shapiro-Wilk Statistic: {stat}, p-value: {p}")
    
    # not normal distribution
    if p <= alpha:
        print('not normal distribution')
        df[v] = remove_outliers(df[v])
    # normal distribution



engine.dispose()
