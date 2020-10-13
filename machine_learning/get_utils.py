from sklearn.datasets import fetch_openml

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt




def save_data(path):

    mnist = fetch_openml("mnist_784", version=1)

    features = mnist["data"]
    labels = mnist["target"]
    columns = mnist["feature_names"] + mnist["target_names"]

    data_matrix = np.concatenate([features, labels.reshape(labels.shape[0], 1)], axis=1)

    mnist_df = pd.DataFrame(data_matrix, columns=columns)
    mnist_df.to_csv(path,index=False)



save_data("..\data\mnist.csv")











