from tkinter import Tk, Canvas, Button
from tkinter import messagebox
from PIL import ImageGrab
import os
import random

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

from machine_learning.recognizer import Recognizer
from machine_learning.get_utils import Digit



class GUI:

    def __init__(self):
        self.window=  Tk()
        self.window.configure(bg="gray")
        self.window.title("Digit recognizer")
        self.window.rowconfigure(0, weight=1)
        self.window.columnconfigure(0, weight=1)
        #self.window.state('windowed')

        self.current_x = 0
        self.current_y = 0

        self.canvas = Canvas(self.window,height=296.05263158,width=296.05263158,bg = "white")
        self.predict_button = Button(self.window,text= "Predict",command = self.button_click,height = 2,width = 20)
        self.clear_button = Button(self.window, text="Clear", command=self.clear_screen, height=2, width=20)
        self.recognizer = Recognizer()
        self.message_window = messagebox

        fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = fig.add_subplot(111)
        self.mt_canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.mt_canvas.get_tk_widget().grid()
        self.mt_canvas.draw()

        toolbar = NavigationToolbar2Tk(self.mt_canvas,self.window)
        toolbar.update()

        self.canvas.grid(row=0, column=0)
        self.predict_button.grid(row=0, column=1)
        self.clear_button.grid(row=1,column = 1)
        self.mt_canvas.get_tk_widget().grid(row=0)
        self.recognizer.load_model("forest_clf.sav")



    def click(self,event):

        self.current_x = event.x
        self.current_y = event.y

    def draw(self,event):

        self.canvas.create_line((self.current_x, self.current_y, event.x, event.y),width = 40)
        self.current_x = event.x
        self.current_y = event.y

    def button_click(self):
        x = self.window.winfo_rootx() + self.canvas.winfo_x()
        y = self.window.winfo_rooty() + self.canvas.winfo_y()
        x1 = x + self.canvas.winfo_width()
        y1 = y + self.canvas.winfo_height()
        ImageGrab.grab().crop((x, y, x1, y1)).save("../predictions/CANVAS_DIGIT.png")

        self.digit = Digit()
        self.digit.load_from_canvas()
        prediction = self.recognizer.recognize(self.digit)
        self.ax.imshow(self.digit.pixel_matrix)


        self.message_window.showinfo("Prediction", f"The digit you drew is {prediction}")

    def clear_screen(self):

        self.canvas.delete("all")

        try:
            os.remove("../predictions/CANVAS_DIGIT.png")
        except:
            pass

        try:
            os.remove("../predictions/img_1.png")
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













