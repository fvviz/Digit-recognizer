
import pandas as pd
import matplotlib.pyplot as plt
import random

from machine_learning.save_data import save_data


def visualize_data( X, y, type="random", amount=5):
    if type == "random":
        for time in range(amount):
            val = random.randint(0, 5000)

            val_array = X[val, :]
            label = y[val]

            val_image = val_array.reshape(28, 28)

            plt.imshow(val_image, cmap="gray")
            plt.xlabel(label)

            plt.show()

try:
    pd.read_csv("../data/mnist.csv")
except:
    save_data("../data/mnist.csv")

data = pd.read_csv("../data/mnist.csv")
visualize_data(X = data.drop(["class"], axis = 1).to_numpy(), y = data["class"].values,amount=20)

