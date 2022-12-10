import mysql.connector as conn
from AppFlow.logger import logging
from AppFlow.exception import CreditcardException
import pandas as pd
from AppFlow.constant import *
import sys,os

class DataIngestion:

    def __init__(self):
        try:
            logging.info(f"{'>>'*15}Data Ingestion log started.{'<<'*15}")
            self.dataset_file_path:str = DATASET_FILE_PATH
            #self.dataset_file_path_file = os.path.join(self.dataset_file_path, 'Credit-card.csv')
            self.dataset_file_path_file = DATASET_FILE_PATH_FILE

        except Exception as e:
            raise CreditcardException(e,sys)

    def download_creditcard_data(self,) -> str:
        try:            
            logging.info(f"Connecting to database")
            
            myobj=conn.connect(host='localhost',user='root',passwd='MySql')
            
            cursor=myobj.cursor()
            
            cursor.execute("use ccdp")
            #print(cursor.fetchall())
            
            logging.info(f"Database connect established")
            
            cursor.execute("select * from creditcardd")
            
            logging.info(f"Loading data from the database.")
            mydata=cursor.fetchall()
            
            df = pd.DataFrame(mydata)
            print(df.head())
            
            if(os.path.exists(self.dataset_file_path_file)):
                os.remove(self.dataset_file_path_file)

            os.makedirs(self.dataset_file_path,exist_ok=True)

            df.to_csv (self.dataset_file_path_file, index = False, header=False)

            logging.info("Loading data from database to csv->Completed")
            logging.info(f"{'>>'*15}Data Ingestion log completed.{'<<'*15} \n\n")
        except Exception as e:
            raise CreditcardException(e,sys) from e

  



