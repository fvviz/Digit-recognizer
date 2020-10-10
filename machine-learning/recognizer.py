import joblib
import random

class Recognizer:

    def __init__(self):

        self.model = None
        self.image = f"predictions/img_{random.randint(1000,9000)}.png"

    def load_model(self,model_name):

        self.model = joblib.load("models/{{")





