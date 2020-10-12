
import pandas as pd
import matplotlib.pyplot as plt
import random

from app.GUI import GUI



def visualize_data( X, y, type="random", amount=5):
    if type == "random":
        for time in range(amount):
            val = random.randint(0, 5000)

            val_array = X[val, :]
            label = y[val]

            val_image = val_array.reshape(28, 28)

            plt.imshow(255 - val_image, cmap="gray")
            plt.xlabel(label)

            plt.show()

#data = pd.read_csv("../data/mnist.csv")
#visualize_data(X = data.drop(["class"], axis = 1).to_numpy(), y = data["class"].values,amount=10)

app = GUI(dim=200)
app.init()

