import joblib
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from tensorflow import keras

import random
from PIL import Image, ImageOps
from skimage.io import imread

class Digit:

    def __init__(self):
       self.id =int(random.randint(1000,9000))
       self.save_path = f"predictions/img_1.png"

       self.pixel_matrix= np.zeros((28,28))
       self.vector_transpose = np.zeros((1,784))
       self.size = (28,28)

    def load_from_canvas(self,path= "predictions/CANVAS_DIGIT.png",save_path = None):

        if not save_path:
            save_path = self.save_path

        image = Image.open(path)
        resized_image =ImageOps.invert(image.resize(self.size))
        resized_image.save(save_path)

        self.pixel_matrix =imread(save_path,as_gray=True)
        self.vector_transpose = self.pixel_matrix.reshape(1,784)


class Recognizer:

    def __init__(self,dataset_type = "sklearn"):

        self.model = None
        self.model_type = None
        self.digit = Digit()


        if dataset_type == "kaggle":
            self.data = pd.read_csv("data/kaggle_mnist.csv")

        elif dataset_type == "sklearn":
            self.data = pd.read_csv("data/mnist.csv")


    def load_model(self,model_name):
        if str(model_name).endswith(".sav"):
             self.model = joblib.load(f"models/{model_name}")
             self.model_type = "sklearn_ml"

        elif str(model_name).endswith(".model"):
             self.model = keras.models.load_model(f"models/{model_name}")
             self.model_type = "neural_net"

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

        if self.model and self.model_type == "sklearn_ml":
            prediction  = self.model.predict(digit_vector)[0]
            pred_stats= self.model.decision_function(digit_vector)[0]
            return prediction,pred_stats

        if self.model and self.model_type == "neural_net":

            normalized_digit  = keras.utils.normalize(digit.pixel_matrix.reshape((1,28,28)))
            prediction_array = self.model.predict(normalized_digit)
            prediction = np.argmax(prediction_array)
            pred_stats = prediction_array.copy()
            return prediction, pred_stats

        else:
            raise Exception("No model available")



















