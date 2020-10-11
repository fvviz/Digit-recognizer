
from app.GUI import GUI
import pandas as pd



print("App starting")
data = pd.read_csv("../data/mnist.csv")

app = GUI()
#app.visualize_data(data.drop(["class"], axis = 1).to_numpy(),data["class"].values,amount=10)

app.init()