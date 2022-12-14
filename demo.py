# import mysql.connector as conn
# import csv
# from AppFlow.constant import *
# from AppFlow.exception import CreditcardException
# import sys,os,io
# import requests
# import pandas as pd
# from six.moves import urllib

# dataset_download_url = Dataset_download_raw_url
# myobj=conn.connect(host='localhost',user='root',passwd='MySql')
# cursor=myobj.cursor()
# cursor.execute("show databases;")

# #download = requests.get(dataset_download_url).content
# #print(download)
# # Reading the downloaded content and turning it into a pandas dataframe

# #df = pd.read_csv(io.StringIO(download.decode('utf-8')))

# # Printing out the first 5 rows of the dataframe

# #print (df.head())

# # list_of_databases = cursor.fetchall()
# # if('ccdp' in list_of_databases):
# #     print("Exists")
# # #cursor.execute("create database ccdp")
# # #cursor.execute("show databases")
# # #print(cursor.fetchall())
# # cursor.execute("use ccdp")
# # #cursor.execute("create table creditcardD(ID varchar(20),LIMIT_BAL varchar(20),SEX varchar(20),EDUCATION varchar(20),MARRIAGE varchar(20),AGE varchar(20),PAY_1 varchar(20),PAY_2 varchar(20),PAY_3 varchar(20),PAY_4 varchar(20),PAY_5 varchar(20),PAY_6 varchar(20),BILL_AMT1 varchar(20),BILL_AMT2 varchar(20),BILL_AMT3 varchar(20),BILL_AMT4 varchar(20),BILL_AMT5 varchar(20),BILL_AMT6 varchar(20),PAY_AMT1 varchar(20),PAY_AMT2 varchar(20),PAY_AMT3 varchar(20),PAY_AMT4 varchar(20),PAY_AMT5 varchar(20),PAY_AMT6 varchar(20),Default_Prediction varchar(20))")
# # cursor.execute("show tables")
# # print(cursor.fetchall())
# count=0


# ROOT_DIR = os.getcwd()  #to get current working directory
# DATASET_DIR = "Data"
# DATASET_FILE_NAME = "Credit__card.csv"
# DATASET_FILE_PATH = os.path.join(ROOT_DIR,DATASET_DIR,DATASET_FILE_NAME)

# #urllib.request.urlretrieve(dataset_download_url, DATASET_FILE_PATH)

# print(DATASET_FILE_PATH)
# with open(DATASET_FILE_PATH,'r') as f:
#     cd=csv.reader(f,delimiter='\n')
#     print(cd)
#     for i in cd:
#         count+=1
#         if count==1:
#             rows = str(i[0])
#             print(f'insert into creditcardD values ({chr(34)+"ID"+chr(34)+rows[2:]})')
#             #print(type(i[0]))
#             #print(str(i[0]))
#             t=i[0].split(",");#print(t)
#             a0='""'+t[0]+'""'
#             a1='"'+t[1]+'"'
#             a2='"'+t[2]+'"'
#             a3='"'+t[3]+'"'
#             a4='"'+t[4]+'"'
#             a5='"'+t[5]+'"'
#             a6='"'+t[6]+'"'
#             a7='"'+t[7]+'"'
#             a8='"'+t[8]+'"'
#             a9='"'+t[9]+'"'
#             a10='"'+t[10]+'"'
#             a11='"'+t[11]+'"'
#             a12='"'+t[12]+'"'
#             a13='"'+t[13]+'"'
#             a14='"'+t[14]+'"'
#             a15='"'+t[15]+'"'
#             a16='"'+t[16]+'"'
#             a17='"'+t[17]+'"'
#             a18='"'+t[18]+'"'
#             a19='"'+t[19]+'"'
#             a20='"'+t[20]+'"'
#             a21='"'+t[21]+'"'
#             a22='"'+t[22]+'"'
#             a23='"'+t[23]+'"'
#             a24='"'+t[24]+'"'

#             print('insert into ccdp.creditcardD values({a0},{a1},{a2},{a3},{a4},{a5},{a6},{a7},{a8},{a9},{a10},{a11},{a12},{a13},{a14},{a15},{a16},{a17},{a18},{a19},{a20},{a21},{a22},{a23},{a24})'.format(a0=a0,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,a10=a10,a11=a11,a12=a12,a13=a13,a14=a14,a15=a15,a16=a16,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,a23=a23,a24=a24))
#             #print(f'insert into creditcardD values ({str(i[0])})')
#             #break
        #cursor.execute('insert into ccdp.creditcardD values({a0},{a1},{a2},{a3},{a4},{a5},{a6},{a7},{a8},{a9},{a10},{a11},{a12},{a13},{a14},{a15},{a16},{a17},{a18},{a19},{a20},{a21},{a22},{a23},{a24})'.format(a0=a0,a1=a1,a2=a2,a3=a3,a4=a4,a5=a5,a6=a6,a7=a7,a8=a8,a9=a9,a10=a10,a11=a11,a12=a12,a13=a13,a14=a14,a15=a15,a16=a16,a17=a17,a18=a18,a19=a19,a20=a20,a21=a21,a22=a22,a23=a23,a24=a24))

#print("Total rows effected",count-1)
#for saving the values to db
#myobj.commit()
#cursor.execute("select * from creditcardD limit 0,10")
#print(cursor.fetchall())

from AppFlow.pipeline.pipeline import Pipeline
from AppFlow.component.model_training import ModelTrainer
import pandas as pd
import pickle
pipeline = Pipeline()
ct=pipeline.run_pipeline()

# mt=ModelTrainer()
# ct=mt.column_pipeline()
df=pd.DataFrame({"LIMIT_BAL":[3e+05],"SEX":['male'],"EDUCATION":['university'],"MARRIAGE":['single'],"AGE":[31],"PAY_1":[0],"PAY_2":[0],"PAY_3":[0],"PAY_4":[0],"PAY_5":[0],"PAY_6":[0],"BILL_AMT1":[0],"PAY_AMT1":[12507],"PAY_AMT2":[15056],"PAY_AMT3":[5027],"PAY_AMT4":[5007],"PAY_AMT5":[5063],"PAY_AMT6":[3039]})
pickled_model = pickle.load(open('K:\\DATA SCIENCE Reference\\Projects\\Credit-Card-Default-Prediction\\trained_model\\model.pkl', 'rb'))
l=pickled_model.predict_proba(ct.transform(df))
print(l)