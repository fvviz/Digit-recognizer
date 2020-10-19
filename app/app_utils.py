from tkinter import *
from tkinter.ttk import *


class PredictionStats:

    def __init__(self, GUI):

        self.window = GUI
        self.frames = [None] * 10
        self.bars = [None] * 10

    def create_bars(self, pixel_distance=30, bar_length=100, frame_width=130):
        for i in range(10):
            self.frames[i] = LabelFrame(self.window, text=str(i))
            self.bars[i]   = Progressbar(self.frames[i], orient=HORIZONTAL, length=bar_length, mode='determinate', value=1, maximum=100)
        self.frames[0].place(x=400, y=0, height=30, width=frame_width)
        for i in range(1, 10):
            self.frames[i].place(x=400, y=pixel_distance*i, height=30, width=frame_width)
            self.bars[i].place(x=7, y=-2)

    def show_stats(self, stat_list):
        try:
            for i in range(10):
                amount = stat_list[i]
                self.bars[i]['value'] = amount*1000
                self.window.update()
        except:
            for i in range(10):
                amount = stat_list[0][i]
                self.bars[i]['value'] = amount * 1000
                self.window.update()

    def clear_bars(self):
        for i in range(10):
            self.bars[i]['value'] = 1
            self.window.update()
