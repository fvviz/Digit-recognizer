from sklearn.datasets import fetch_openml
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

import numpy as np
import pandas as pd
import joblib

def save_data(path):

    mnist = fetch_openml("mnist_784", version=1)

    features = mnist["data"]
    labels = mnist["target"]
    columns = mnist["feature_names"] + mnist["target_names"]

    data_matrix = np.concatenate([features, labels.reshape(labels.shape[0], 1)], axis=1)

    mnist_df = pd.DataFrame(data_matrix, columns=columns)
    mnist_df.to_csv(path)


def train_model(model_name,estimator = "random_forest",data_path = "data/mnist.csv"):

    data = pd.read_csv(data_path)

    X = data.drop("class").to_numpy()
    y = data["class"].values



    if estimator == 'random_forest':

        forest_clf = RandomForestClassifier(n_estimators=200,min_samples_leaf=70,min_samples_split=120)

        param_grid ={
            "n_estimators" : [200,300,400],
            "min_samples_leaf" : [70,80,100,150],
            "min_samples_split" : [100,200,300,400]
        }


        grid_clf = GridSearchCV(forest_clf,param_grid,scoring="accuracy",cv = 3)

        print("Training model...")

        grid_clf.fit(X,y)

        print("Model training completed")

        joblib.dump(grid_clf,f"models/{model_name}")

        print(f"Model Saved as {model_name}")












