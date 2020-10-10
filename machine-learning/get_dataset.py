from sklearn.datasets import fetch_openml
import numpy as np
import pandas as pd

#from constants import current_path


mnist = fetch_openml("mnist_784",version= 1)

features = mnist["data"]
labels = mnist["target"]
columns = mnist["feature_names"] + mnist["target_names"]

data_matrix = np.concatenate([mnist["data"],mnist["target"].reshape(mnist["target"].shape[0],1)],axis = 1)

mnist_df =pd.DataFrame(data_matrix,columns=columns)
mnist_df.to_csv(f"data/mnist.csv")

