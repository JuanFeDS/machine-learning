import pandas as pd
import joblib

class Utils():
    
    def load_from_csv(self, path):
        dataset = pd.read_csv(path) 
        return dataset

    def loaf_from_sql(self):
        pass

    def features_target(self, dataset, drop_columns, target):
        X = dataset.drop(drop_columns, axis=1)
        y = dataset[target]

        return X, y   

    def model_export(self, model, score):
        print(score)
        joblib.dump(model, 'models/model.pkl')