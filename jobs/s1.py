import requests
import csv

BASE_URL = "https://api.openf1.org/v1/"
methods = ['car_data', 'drivers', 'intervals', 'laps', 'location', 'meetings', 'pit', 'position', 'race_control', 'sessions', 'stints', 'team_radio', 'weather']

for method in methods:
    uri = method
    req = requests.get(BASE_URL+uri)
    print(req.url)
    print(req.status_code)

    if req.status_code == 200:
        data = req.json()
        file_path = f'../staging/{method}.csv'
        with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.DictWriter(csvfile, fieldnames=data[0].keys())
            csv_writer.writeheader()
            csv_writer.writerows(data)
    else:
        print(f'Err {req.status_code}: {method}')