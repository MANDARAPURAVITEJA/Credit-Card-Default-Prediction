import sys,os
from AppFlow.exception import CreditcardException
from AppFlow.pipeline.pipeline import Pipeline
import pandas as pd
import dill

class CreditcardData:

    def __init__(self, 
                LIMIT_BAL: float,
                SEX: str,
                EDUCATION:str,
                MARRIAGE:str,
                AGE:float,
                PAY_1:float,
                PAY_2:float,
                PAY_3:float,
                PAY_4:float,
                PAY_5:float,
                PAY_6:float,
                BILL_AMT1:float,
                PAY_AMT1:float,
                PAY_AMT2:float,
                PAY_AMT3:float,
                PAY_AMT4:float,
                PAY_AMT5:float,
                PAY_AMT6:float,
                Default_Prediction: float = None
                ):
        try:
            self.LIMIT_BAL = LIMIT_BAL
            self.SEX = SEX
            self.EDUCATION = EDUCATION
            self.MARRIAGE = MARRIAGE
            self.AGE = AGE
            self.PAY_1 = PAY_1
            self.PAY_2 = PAY_2
            self.PAY_3 = PAY_3
            self.PAY_4 = PAY_4
            self.PAY_5 = PAY_5
            self.PAY_6 = PAY_6
            self.BILL_AMT1 = BILL_AMT1
            self.PAY_AMT1 = PAY_AMT1
            self.PAY_AMT2 = PAY_AMT2
            self.PAY_AMT3 = PAY_AMT3
            self.PAY_AMT4 = PAY_AMT4
            self.PAY_AMT5 = PAY_AMT5
            self.PAY_AMT6 = PAY_AMT6
            self.Default_Prediction = Default_Prediction
        except Exception as e:
            raise CreditcardException(e,sys) from e
    
    def get_creditcard_input_data_frame(self):
        try:
            creditcard_dict = self.get_creditcard_data_as_dict()
            return pd.DataFrame(creditcard_dict)
        except Exception as e:
            raise CreditcardException(e,sys) from e
    
    def get_creditcard_data_as_dict(self):
        try:
            input_data = {
                "LIMIT_BAL": [self.LIMIT_BAL],
                "SEX": [self.SEX],
                "EDUCATION": [self.EDUCATION],
                "MARRIAGE": [self.MARRIAGE],
                "AGE": [self.AGE],
                "PAY_1": [self.PAY_1],
                "PAY_2": [self.PAY_2],
                "PAY_3": [self.PAY_3],
                "PAY_4": [self.PAY_4],
                "PAY_5": [self.PAY_5],
                "PAY_6": [self.PAY_6],
                "BILL_AMT1": [self.BILL_AMT1],
                "PAY_AMT1": [self.PAY_AMT1],
                "PAY_AMT2": [self.PAY_AMT2],
                "PAY_AMT3": [self.PAY_AMT3],
                "PAY_AMT4": [self.PAY_AMT4],
                "PAY_AMT5": [self.PAY_AMT5],
                "PAY_AMT6": [self.PAY_AMT6]}
            return input_data
        except Exception as e:
            raise CreditcardException(e,sys)

class CreditcardDefaultPredictor:

    def __init__(self, model_dir: str):
        try:
            self.pipeline = Pipeline()
            self.column_pipeline = self.pipeline.column_transform()
            self.model_dir = model_dir
        except Exception as e:
            raise CreditcardException(e,sys) from e
    
    def predict(self, X_test):
        try:
            model_path = self.model_dir
            model = self.load_object(file_path=model_path)
            defaulter = model.predict(self.column_pipeline.transform(X_test))
            if(defaulter==0):
                return "Not a Defaulter"
            else:
                return "Defaulter"
        except Exception as e:
            raise CreditcardException(e, sys) from e

    def load_object(self,file_path:str):
        try:
            with open(file_path, "rb") as file_obj:
                return dill.load(file_obj)
        except Exception as e:
            raise CreditcardException(e,sys) from e

