from sklearn.datasets import fetch_openml

import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt

from PIL import Image
from skimage.io import imread

class Digit:

    def __init__(self):
       self.id =int(random.randint(1000,9000))
       self.save_path = f"../predictions/img_1.png"

       self.pixel_matrix= np.zeros((28,28))
       self.vector_transpose = np.zeros((1,784))
       self.size = (28,28)

    def load_from_canvas(self,path= "../predictions/CANVAS_DIGIT.png"):

        image = Image.open(path)
        resized_image = image.resize(self.size)
        resized_image.save(self.save_path)

        self.pixel_matrix =imread(self.save_path,as_gray=True)
        #plt.imshow(255-self.pixel_matrix,cmap = "gray")
        #plt.show()
        self.vector_transpose = self.pixel_matrix.reshape(1,784)



def save_data(path):

    mnist = fetch_openml("mnist_784", version=1)

    features = mnist["data"]
    labels = mnist["target"]
    columns = mnist["feature_names"] + mnist["target_names"]

    data_matrix = np.concatenate([features, labels.reshape(labels.shape[0], 1)], axis=1)

    mnist_df = pd.DataFrame(data_matrix, columns=columns)
    mnist_df.to_csv(path,index=False)



save_data("..\data\mnist.csv")











