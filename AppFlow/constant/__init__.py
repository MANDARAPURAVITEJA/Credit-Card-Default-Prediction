import os
from datetime import datetime

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"

ROOT_DIR = os.getcwd()  #to get current working directory
DATASET_DIR = "dataset"
DATASET_FILE_NAME = "Credit-card.csv"
DATASET_FILE_PATH = os.path.join(ROOT_DIR,DATASET_DIR)
DATASET_FILE_PATH_FILE = os.path.join(ROOT_DIR,DATASET_DIR,DATASET_FILE_NAME)

CURRENT_TIME_STAMP = get_current_time_stamp()

Dataset_download_raw_url = 'https://raw.githubusercontent.com/MANDARAPURAVITEJA/Credit-Card-Default-Prediction/main/Data/UCI_Credit_Card.csv'

RAW_DATASET_DIR = "Data"
RAW_DATASET_FILE_NAME = "Credit__card.csv"
RAW_DATASET_FILE_PATH = os.path.join(ROOT_DIR,DATASET_DIR,DATASET_FILE_NAME)

PICKLE_FILE_DIR = "trained_model"
PICKLE_FILE_NAME = "model.pkl"
PICKLE_FILE_PATH_FILE = os.path.join(ROOT_DIR,PICKLE_FILE_DIR,PICKLE_FILE_NAME)