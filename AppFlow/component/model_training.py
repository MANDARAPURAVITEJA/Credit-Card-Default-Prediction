from AppFlow.logger import logging
from AppFlow.constant import *
from AppFlow.exception import CreditcardException
from AppFlow.component.data_transformation import DataTransformation
import sys,os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from imblearn.over_sampling import SMOTE
from xgboost import XGBClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline


class ModelTrainer:

    def __init__(self) -> None:
        try:
            logging.info(f"{'>>'*15}Model Training log started{'<<'*15}")

        except Exception as e:
            raise CreditcardException(e,sys) from e
        pass

    def creating_pipeline(self,data_transform_dataset):
        try:
            logging.info("Loading the transformed dataset from Data Transformation phase")
            
            # data_transform = DataTransformation()
            # self.dataset = data_transform.data_transformation()
            self.dataset = data_transform_dataset

            X = self.dataset.iloc[:,:-1]
            y = self.dataset.iloc[:,-1]

            #Doing the stratified train test split for the dataset based on dependent variable.
            X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42, stratify=y)

            numerical_columns=X_train.select_dtypes(include=['int64','float64']).columns

            #numerical pipeline
            logging.info("Creating Numerical Pipeline")
            numerical_pipeline=Pipeline([('feature_scaling',StandardScaler())])

            categorical_columns=X_train.select_dtypes(include=['object','category']).columns
            
            #Categorical pipeline
            logging.info("Creating Categorical Pipeline")
            categorical_pipeline=Pipeline([('categorical_encoder', OrdinalEncoder())])

            logging.info("Combing both numerical and categorical pipeline")
            column_pipeline=ColumnTransformer([
                ("numerical_pipeline",numerical_pipeline,numerical_columns),
                ("categorical_pipeline",categorical_pipeline,categorical_columns)])

            # Preprocessing the X_train set through pipeline
            X_train_processed = column_pipeline.fit_transform(X_train)

            logging.info("Re-sampling the dataset using SMOTE method")
            smote = SMOTE(sampling_strategy=0.5)
            self.X_train1, self.y_train1 = smote.fit_resample(X_train_processed,y_train)

            logging.info("Applying the column transformer to the Test set data")
            self.X_test1 = column_pipeline.transform(X_test)

            #returning column pipeline for transforming the realtime data with the Column Transformer.
            return self.X_train1,self.X_test1,self.y_train1,y_test,column_pipeline

        except Exception as e:
            raise CreditcardException(e,sys) from e
    
    def model_training(self,X_train,y_train):
        try:
            #self.X_train, self.y_train = self.get_trainset_values()
            self.X_train, self.y_train = X_train, y_train

            logging.info("Training the model using XGBClassifier")
            xgc = XGBClassifier(n_estimators=500,max_depth=3,n_jobs=-1, use_label_encoder =False)
            xgc.fit(self.X_train, self.y_train)

            logging.info("Training the model using RandomForest Classifier")
            rforest=RandomForestClassifier(n_estimators=10, max_depth=3, criterion='entropy',random_state=0)
            rforest.fit(self.X_train,self.y_train)
            #predict=rforest.predict(X_test)

            gboost=GradientBoostingClassifier(n_estimators=500,learning_rate=0.05,random_state=100,max_features=5)
            gboost.fit(self.X_train, self.y_train)

            logging.info(f"{'>>'*15}Model Training completed{'<<'*15}")
            return {'xgc':xgc, 'rforest':rforest, 'gboost':gboost}
        
        except Exception as e:
            raise CreditcardException(e,sys) from e



        








            
            



