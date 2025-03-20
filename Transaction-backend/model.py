import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from datetime import timedelta
import numpy as np
import pickle
import random 


from transaction_data import get_transactions_data 

pd.options.mode.chained_assignment = None
# 1. Data Preprocessing:
# Assuming your dataframe `df` contains columns: 'amount', 'date', and 'label'

# import pandas as pd
# import numpy as np
# import random
# from sklearn.model_selection import train_test_split
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.ensemble import RandomForestRegressor
# from sklearn.pipeline import Pipeline
# from sklearn.metrics import mean_absolute_error
# from datetime import timedelta
# import pickle

class ModelPredictor:
    def __init__(self): 
        with open("models.pkl", "rb") as f:
            self.models = pickle.load(f) 
            
    def preprocess_data(self, df):
        # Feature Engineering
        
        df.loc[:,"day_of_week"] = df["date"].dt.dayofweek
        df.loc[:,"month"] = df["date"].dt.month
        df.loc[:,"year"] = df["date"].dt.year
        df.loc[:,"day_of_month"] = df["date"].dt.day
        df.loc[:,"week_of_year"] = df["date"].dt.isocalendar().week
        df.loc[:,"day_of_year"] = df["date"].dt.dayofyear
        df.loc[:,"lag_amount"] = df["amount"].shift(1).fillna(0)  # Lag feature

        # Feature Matrix (TF-IDF on 'label' column)
        vectorizer = TfidfVectorizer(stop_words="english")
        X = vectorizer.fit_transform(df["label"])

        # Adding date-related features and lag features to the matrix
        date_features = df[[
            "day_of_week",
            "month",
            "year",
            "day_of_month",
            "week_of_year",
            "day_of_year",
            "lag_amount",
        ]]
        X = np.hstack([X.toarray(), date_features.values])

        return X

    def predict(self, data: pd.DataFrame): 
        all_predictions = [] 
        for label in data['label'].unique():
            if label in self.models: 
                predictions = self.predict_for_label(data[data['label'] == label], label) 
                all_predictions.append(predictions) 
        
        # Choose predictions randomly weighted by the frequency of predictions
        weights = list(map(len, all_predictions))

        result = [] 
        for pred in random.choices(all_predictions, weights=weights, k=random.choice([10, 12])):
            # print('Pred:',pred)
            result.append( pred.sample(n=1).iloc[0].to_dict()) 

        print('weights:', weights, '\nresult:', result)  
        return result

    def predict_for_label(self, new_data: pd.DataFrame, label):
        model = self.models[label]
        # Preprocess new data (you can modify this to match the format of your incoming data)
        X_new = self.preprocess_data(new_data)

        # We will make multiple predictions for the same instance
        num_predictions = random.choice([10, 12])  # You can define the range for predictions per input
        predictions = []

        # Get multiple predictions for each input
        for _ in range(num_predictions):
            predictions.append(model.predict(X_new))

        predictions = np.array(predictions).flatten()

        # Prepare the dates for the next week based on the input data's latest date
        start_date = new_data["date"].max()  # Latest date from the new data
        next_week_dates = pd.date_range(
            start=start_date + timedelta(days=1), periods=7, freq="D"
        )  # Next week's dates

        # Randomly sample 12 dates from next week's range
        random_dates = np.random.choice(next_week_dates, size=num_predictions, replace=True)

        # Structure the predictions in a dataframe with dates and amounts
        print(random_dates) 
        print(predictions[:num_predictions])
        
        result_df = pd.DataFrame(
            {
                "date": sorted(random_dates),  # Ensuring that the dates are sorted
                "predicted_amount": predictions[:num_predictions],  # Limit to n predictions
            }
        )

        return result_df

class ModelPredictor:
    def __init__(self):
        self.models = None 
    
        with open('TfidfVectorizer.pkl', 'rb') as f:
            self.vectorizer = pickle.load(f) 
    
    def get_model(self, label): 
        if not self.models: 
            print('initialising models') 
            with open("models.pkl", "rb") as f:
                self.models = pickle.load(f)
        
        return self.models[label]

    def preprocess_data(self, df):
        # Feature Engineering

        df.loc[:,"day_of_week"] = df["date"].dt.dayofweek
        df.loc[:,"month"] = df["date"].dt.month
        df.loc[:,"year"] = df["date"].dt.year
        df.loc[:,"day_of_month"] = df["date"].dt.day
        df.loc[:,"week_of_year"] = df["date"].dt.isocalendar().week
        df.loc[:,"day_of_year"] = df["date"].dt.dayofyear
        df.loc[:,"lag_amount"] = df["amount"].shift(1).fillna(0)  # Lag feature

            
        
        X = self.vectorizer.fit_transform(df["label"])

        # Adding date-related features and lag features to the matrix
        date_features = df[[
            "day_of_week",
            "month",
            "year",
            "day_of_month",
            "week_of_year",
            "day_of_year",
            "lag_amount",
        ]]
        X = np.hstack([X.toarray(), date_features.values])

        return X

    def predict(self, data: pd.DataFrame): 
        self.last_date = data['date'].max()
        labels = tuple( data['label'].unique()) 

        predictions = {
            label: self.predict_for_label(
                data[data['label'] == label], label
            ) 
                for label in  data['label'].unique()
        } 
        # all_predictions = []
        # for label in data['label'].unique():
        #     if label in self.models:
        #         predictions = self.predict_for_label(data[data['label'] == label], label)
        #         all_predictions.append(predictions)

        # Choose predictions randomly weighted by the frequency of predictions
        weights = [len(predictions[label]) for label in labels]

        result = []
        for label in random.choices(labels, weights=weights, k=random.choice([10, 12])):
            # print('Pred:',pred)
            result.append( 
                predictions[label].sample(n=1).iloc[0].to_dict()
            
                )
            result[-1]['label'] = label 

        print('weights:', weights, '\nresult:') 

        self.post_process(result)
        return result

    def predict_for_label(self, new_data: pd.DataFrame, label):
        model = self.get_model(label)
        X_new = self.preprocess_data(new_data)

        num_predictions = random.choice([10, 12])  
        predictions = []

        for _ in range(num_predictions):
            predictions.append(model.predict(X_new))

        predictions = np.array(predictions).flatten()

        next_week_dates = pd.date_range(
            start=self.last_date + timedelta(days=1), periods=7, freq="D"
        ) 
        random_dates = np.random.choice(next_week_dates, size=num_predictions, replace=True)


        result_df = pd.DataFrame(
            {
                "date": (random_dates), 
                "amount": predictions[:num_predictions], 
            }
        )

        return result_df 

    def post_process(self, data: list[dict]) -> None: 
        data.sort(key=lambda row: row['date'])

        for row in data: 
            row['amount'] = round(row["amount"],2)
            row['date'] = row['date'].strftime("%Y-%m-%d")




def predict_labels(data: pd.DataFrame): 
    # NLP Pickle
    with open('model_and_vectorizer.pkl', 'rb') as f:
        z = pickle.load(f) 
        model = z['model' ]
        vec = z['vectorizer']

    y_pred = model.predict(vec.transform(data['description'])) 
    return y_pred

predictor = ModelPredictor() 
def predict_next_week(data): 
    # Regressor
    data = pd.DataFrame(data) 
    data['date'] =  pd.to_datetime(data['date'])  

    data['label'] = predict_labels(data) 
    
    result = predictor.predict(data) 

    return result  

if __name__ == "__main__":
    # z = ModelMaker(df)
    # p = ModelPredictor()  
    data = (get_transactions_data(call_api=False) )
    
    y = predict_next_week(data)
    print(*y, sep='\n')
