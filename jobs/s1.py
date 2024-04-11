# ETL job to get the f1 data and store in local stage staging/ds.csv
import pandas as pd
import requests
import csv

BASE_URL = "https://api.openf1.org/v1/"
methods = ['car_data', 'drivers', 'intervals', 'laps', 'location', 'meetings', 'pit', 'position', 'race_control', 'sessions', 'stints', 'team_radio', 'weather']

for i in range(len(methods)):
    uri = methods[i]
    req = requests.get(BASE_URL+uri)
    print(req.url)
    print(req.status_code)
    
    with open(f'../staging/{methods[i]}.csv', 'w') as csvfile:
        csvwiter = csv.writer(csvfile)
        csvwiter.writerow(req)
