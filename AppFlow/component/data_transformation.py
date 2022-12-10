from AppFlow.logger import logging
from AppFlow.constant import *
from AppFlow.exception import CreditcardException
import pandas as pd
import numpy as np
import sys,os

class DataTransformation():

    def __init__(self) -> None: 
        try:
            logging.info(f"{'>>>'*10}Data Tranformation log started.{'<<<'*10}")
            self.dataset_file_path_file = DATASET_FILE_PATH_FILE
            pass
        except Exception as e:
            raise CreditcardException(e,sys) from e

    def data_transformation(self):
        try:
            #Loading the file which we downloaded from database
            logging.info("Loading the dataset")
            dataset = pd.read_csv(self.dataset_file_path_file)
            dataset.head()

            #Replacing the column names in the dataset
            dataset.rename(columns={'PAY_0':'PAY_1'},inplace=True)
            dataset.rename(columns={'default.payment.next.month':'Default_Prediction'},inplace=True)

            logging.info("------Doing Feature engineering to the dataset--------")
            
            #Replacing values in the features with their Actual names
            dataset['SEX'] = dataset['SEX'].replace({1:'male', 2:'female'})

            #Here, we have some other values in Education like {0,4,5,6} which are not in first 3 categories.
            #So, we are replacing all with section 4
            dataset['EDUCATION']=dataset['EDUCATION'].replace({0:4,5:4,6:4})
            dataset['EDUCATION']=dataset['EDUCATION'].replace({1:'graduate school',2:'university',3:'high school',4:'others'})

            #Doing the transformation to Marriage columns
            dataset['MARRIAGE']=dataset['MARRIAGE'].replace({0:3})
            dataset['MARRIAGE']=dataset['MARRIAGE'].replace({1:'married',2:'single',3:'others'})

            #We are replacing the values of all PAY_X features -1,-2 with 0.
            for i in range(1,7):
                field='PAY_'+str(i)
                dataset[field]=dataset[field].replace({-1:0})
                dataset[field]=dataset[field].replace({-2:0})
            
            #Dropping the unique ID column
            dataset=dataset.drop(columns='ID')

            self.outliers = self.Finding_outliers(dataset['LIMIT_BAL'])

            median = np.median(dataset['LIMIT_BAL'])# Replace with median
            
            for i in self.outliers:
                c = np.where(dataset['LIMIT_BAL']==i, median, dataset['LIMIT_BAL'])
            dataset['LIMIT_BAL']=c

            #There is high correlation between the BILL_AMTX features. So, dropping the last 5 BILL_AMT features.
            logging.info("Dropping the last 5 BILL_AMT features")

            self.df = dataset.drop(columns=['BILL_AMT2', 'BILL_AMT3', 'BILL_AMT4', 'BILL_AMT5', 'BILL_AMT6'])

            #print(self.df.head())
            logging.info("Returning the transformed dataset after feature engineering")
            logging.info(f"{'>>'*15}Data Transformation log completed.{'<<'*15} \n\n")
            return self.df

        except Exception as e:
            raise CreditcardException(e,sys) from e


            
    def Finding_outliers(self,data):
        try:
            outliers = []
            data = sorted(data)
            q1 = np.percentile(data, 25)
            q3 = np.percentile(data, 75)
            IQR = q3-q1
            lwr_bound = q1-(1.5*IQR)
            upr_bound = q3+(1.5*IQR)
            for i in data: 
                if (i<lwr_bound or i>upr_bound):
                    outliers.append(i)
            return outliers
        
        except Exception as e:
            raise CreditcardException(e,sys) from e

    # def __del__(self):
    #     logging.info(f"{'>>'*15}Data Transformation log completed.{'<<'*15} \n\n")