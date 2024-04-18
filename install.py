import os
import subprocess

def start_services():
    try:
        subprocess.run(["docker-compose", "up", "-d"], check=True)
        subprocess.run(["docker-compose", "up", "-d"], check=True, cwd="/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline/metabase")
    except subprocess.CalledProcessError as e:
        print(f"Error starting services: {e}")

def execute_jobs():
    try:
        subprocess.run(["python3", "s1.py"], check=True, cwd="/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline/jobs")
        subprocess.run(["python3", "s2.py"], check=True, cwd="/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline/jobs")
    except subprocess.CalledProcessError as e:
        print(f"Error executing jobs: {e}")

if __name__ == "__main__":
    start_services()
    execute_jobs()
