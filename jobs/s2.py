# Job ETL to insert data in the postgres 
import psycopg2

try:
    conn = psycopg2.connect(host="localhost", )
except:
    print(e)
    exit(0)