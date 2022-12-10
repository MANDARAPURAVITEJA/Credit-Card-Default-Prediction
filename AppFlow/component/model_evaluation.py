from AppFlow.logger import logging
from AppFlow.constant import *
from AppFlow.exception import CreditcardException
from AppFlow.component.model_training import ModelTrainer
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
#import pickle
import dill
import sys,os

class ModelEvaluation:

    def __init__(self) -> None:
        try:
            logging.info(f"{'>>'*15}Model Evaluation started{'<<'*15}")
            self.accuracy = 0
            self.F1_score = 0
            self.roc_score = 0
            self.pickle_file_path = PICKLE_FILE_PATH_FILE

        except Exception as e:
            raise CreditcardException(e,sys) from e
        pass

    def model_evaluation(self,models,X_test,y_test):
        try:
            logging.info("Finding the best model..")
            # model_trainer=ModelTrainer()
            # self.models= model_trainer.model_training()
            self.models = models

            list_of_models = self.models.values()
            print(list_of_models)
            
            #self.X_test, self.y_test = model_trainer.get_testset_values()
            self.X_test, self.y_test = X_test, y_test

            for i in list_of_models:
                predict=i.predict(self.X_test)
                accuracy = accuracy_score(self.y_test,predict)
                F1_score = f1_score(self.y_test,predict)
                roc_score = roc_auc_score(self.y_test,predict)
                if((accuracy>self.accuracy and F1_score>self.F1_score) or (accuracy>self.accuracy and roc_score>self.roc_score) or (roc_score>self.roc_score and F1_score>self.F1_score)):
                    self.accuracy = accuracy
                    self.F1_score = F1_score
                    self.roc_score = roc_score
                    self.model = i
            
            logging.info(f"Best model found>>>>>{self.model}<<<<<")
            logging.info(f"{'>>'*15}Model Evaluation Completed{'<<'*15}")
            return self.model
        
        except Exception as e:
            raise CreditcardException(e,sys) from e

    def model_pickling(self,best_model):
        try:
            logging.info(f"{'>>'*15}Model Pickling started{'<<'*15}")

            #model_evaluation = self.model_evaluation()
            model_evaluation = best_model

            print(model_evaluation)
            dir_path = os.path.dirname(self.pickle_file_path)
            os.makedirs(dir_path, exist_ok=True)
            with open(self.pickle_file_path, "wb") as file_obj:
                dill.dump(model_evaluation, file_obj)
            logging.info(f"{'>>'*15}Model Pickling Completed{'<<'*15}")

        except Exception as e:
            raise CreditcardException(e,sys) from e        

        







                

            