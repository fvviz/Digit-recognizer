from tkinter import *
from PIL import ImageGrab
from time import sleep
import os
import random
import matplotlib.pyplot as plt


from machine_learning.recognizer import Recognizer, Digit
from app.app_utils import PredictionStats



class GUI:

    def __init__(self,dim = 200,model = "forest_clf.sav"):

        dim_dict = {
            100: 87.4999999998,
            28: 24.4999999999,
            200: 196.078431373,
            500: 496.031746032,
        }

        self.window=  Tk()
        self.dim = dim
        self.window.configure(bg="gray")
        self.window.title("Digit recognizer")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        self.window.geometry(f'600x500')
        self.window.iconphoto("app/app_icon.png")

        self.current_x = 0
        self.current_y = 0

        self.canvas = Canvas(self.window,height=dim_dict[dim],width=dim_dict[dim],bg = "white")
        self.img_canvas = Canvas(self.window,height = 24.4999999999,width = 24.4999999999)
        self.predict_button = Button(self.window,text= "Predict",command = self.predict_digit,height = 2,width = 10)
        self.clear_button = Button(self.window, text="Clear", command=self.clear_screen, height=2, width=10)
        self.recognizer = Recognizer()
        self.prediction_label = Label(self.window,text = "Draw and click predict",width = 20,height = 1)
        self.scale_label_frame = LabelFrame(self.window,text= "Brush size",bd = 5, font = ('arial',7,'bold'), relief = RIDGE)
        self.prediction_bars = PredictionStats(self)
        self.scale_bar = Scale(self.scale_label_frame,orient = VERTICAL,from_  = 10, to = 60,length = 100)
        self.scale_bar.set(1)


        self.canvas.place(x=130,y = 60)
        self.prediction_label.place(x=140, y= 270)
        self.predict_button.place(x=0, y=50)
        self.clear_button.place(x=0, y=4)
        self.scale_label_frame.place(x = 0,y =100,height = 150,width = 60)
        self.scale_bar.place(x = 0, y = 20)
        self.recognizer.load_model(model)
        self.prediction_bars.create_bars(pixel_distance=40)

    def click(self,event):
        self.current_x = event.x
        self.current_y = event.y

    def draw(self,event):
        self.canvas.create_rectangle((self.current_x, self.current_y, event.x, event.y),fill = "black",width = self.scale_bar.get())
        self.current_x = event.x
        self.current_y = event.y



    def predict_digit(self):
        x = self.window.winfo_rootx() + self.canvas.winfo_x()
        y = self.window.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("predictions/CANVAS_DIGIT.png")

        self.digit = Digit()
        self.digit.load_from_canvas()
        digit_image = PhotoImage(file = self.digit.save_path)
        prediction, bars = self.recognizer.recognize(self.digit)


        self.img_canvas.create_image(100,100,image = digit_image,anchor = NW)
        self.prediction_label.configure(text = f"Prediction : {prediction}")
        self.prediction_bars.show_stats(bars)

    def mouse_in_screen(self):

        while True:
            x = self.window.winfo_rootx() + self.canvas.winfo_x()
            y = self.window.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save("predictions/screen_cap.png")

            self.digit = Digit()
            self.digit.load_from_canvas(path="predictions/CANVAS_DIGIT_2.png",
                                        save_path="predictions/screen_cap.png")
            prediction, bars = self.recognizer.recognize(self.digit)
            self.prediction_bars.show_stats(bars)

            try:
                os.remove("predictions/screen_cap.png")
            except:
                pass
            try:
                os.remove("predictions/screen_cap.png")
            except:
                pass

            sleep(0.005)

    def clear_screen(self):

        self.canvas.delete("all")
        self.prediction_label.configure(text = "Draw and click predict")
        self.prediction_bars.clear_bars()

        try:
            os.remove("predictions/CANVAS_DIGIT.png")
        except:
            pass

        try:
            os.remove("predictions/img_1.png")
        except:
            pass

    def visualize_data(self,X,y, type="random", amount=5):

        if type == "random":
            for time in range(amount):
                val = random.randint(0, 5000)

                val_array = X[val, :]
                label = y[val]
                
                val_image = val_array.reshape(28, 28)

                plt.imshow(255 - val_image, cmap="gray")
                plt.xlabel(label)
                
                plt.show()

    def init(self):

        self.canvas.bind("<Button-1>", self.click)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.window.mainloop()





















