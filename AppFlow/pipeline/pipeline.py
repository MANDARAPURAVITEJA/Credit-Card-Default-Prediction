from AppFlow.component.data_ingestion import DataIngestion
from AppFlow.component.data_transformation import DataTransformation
from AppFlow.component.model_training import ModelTrainer
from AppFlow.component.model_evaluation import ModelEvaluation
from Data.Database_connect import *
from AppFlow.logger import logging


class Pipeline:
    def __init__(self) -> None:
        try:
            pass
        except Exception as e:
            raise CreditcardException(e,sys) from e

    def run_pipeline(self):
        try:
            logging.info(f"{'>>'*30}Pipeline Started{'<<'*30}")

            logging.info(f"{'-'*10}Data Ingestion{'-'*10}")
            self.data_ingestion_variable = DataIngestion()
            self.data_ingestion_variable.download_creditcard_data()

            logging.info(f"{'-'*10}Data Transformation{'-'*10}")
            self.data_transformation_variable = DataTransformation()
            self.dataset = self.data_transformation_variable.data_transformation()
            print(self.dataset.head())

            logging.info(f"{'-'*10}Model Training{'-'*10}")
            self.model_trainer_variable = ModelTrainer()
            self.X_train, self.X_test, self.y_train, self.y_test, self.column_pipeline = self.model_trainer_variable.creating_pipeline(self.dataset)
            self.models = self.model_trainer_variable.model_training(self.X_train,self.y_train)

            logging.info(f"{'-'*10}Model Evaluation{'-'*10}")
            self.model_evaluation_variable = ModelEvaluation()
            self.best_model = self.model_evaluation_variable.model_evaluation(self.models, self.X_test, self.y_test)
            self.model_evaluation_variable.model_pickling(self.best_model)
            
            return self.column_pipeline

        except Exception as e:
            raise CreditcardException(e,sys) from e
        
    def column_transform(self):
        try:
            self.data_transformation_variable = DataTransformation()
            self.dataset = self.data_transformation_variable.data_transformation()

            self.model_trainer_variable = ModelTrainer()
            self.X_train, self.X_test, self.y_train, self.y_test, self.column_pipeline = self.model_trainer_variable.creating_pipeline(self.dataset)
            return self.column_pipeline
        except Exception as e:
            raise CreditcardException(e,sys) from e


# data_ingestion= DataIngestion()
# data_ingestion.download_creditcard_data()

# Db=Database_Creation()
# print(Db.database_create())

# data_transform=DataTransformation()
# dataset=data_transform.data_transformation()
# print(dataset.head())

# model_trainer=ModelTrainer()
# X_train,y_train = model_trainer.get_trainset_values()
# print(X_train[0])

# model_evaluation=ModelEvaluation()
# model_evaluation.model_pickling()