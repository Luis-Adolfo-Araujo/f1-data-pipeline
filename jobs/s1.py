import io
import os
import zipfile as zp
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()
dataset = 'rohanrao/formula-1-world-championship-1950-2020'
staging_dir = "/home/luis/Documents/CesarSchool/periodo5/f1-data-pipeline/staging"
os.makedirs(staging_dir, exist_ok=True)
api.dataset_download_files(dataset, path=staging_dir, unzip=True)
