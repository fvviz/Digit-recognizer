import joblib
import pandas as pd

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from machine_learning.get_utils import Digit


class Recognizer:

    def __init__(self,dataset_type = "sklearn"):

        self.model = None
        self.digit = Digit()


        if dataset_type == "kaggle":
            self.data = pd.read_csv("../data/kaggle_mnist.csv")

        elif dataset_type == "sklearn":
            self.data = pd.read_csv("../data/mnist.csv")


    def load_model(self,model_name):
        self.model = joblib.load(f"../models/{model_name}")

    def train_new_model(self,model_name,estimator = "random_forest"):
            data = self.data.copy()
            print("copied data")

            X = data.drop(["class",],axis = 1).to_numpy()
            y = data["class"].values
            print("features and labels configured")

            if estimator == 'random_forest':
                forest_clf = RandomForestClassifier(verbose=2)

                param_grid = {
                    "n_estimators": [200, 300, 400],
                    "min_samples_leaf": [70, 80, 100, 150],
                    "min_samples_split": [100, 200, 300, 400]
                }

                grid_clf = GridSearchCV(forest_clf, param_grid, scoring="accuracy", cv=3)
                print("Initiating Grid Search...")

                grid_clf.fit(X, y)
                print("Model training using Grid search completed")

                joblib.dump(grid_clf, f"../models/{model_name}")
                print(f"Model Saved as {model_name}")

                self.model = self.load_model(model_name)


    def recognize(self,digit : Digit):

        digit_vector = digit.vector_transpose

        if self.model:
            return self.model.predict(digit_vector)[0]
        else:
            raise Exception("No model available")



















