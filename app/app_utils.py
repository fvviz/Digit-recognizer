from tkinter import *
from tkinter.ttk import *


class PredictionStats:

    def __init__(self,GUI):

        self.window = GUI.window

    def create_bars(self,pixel_distance = 30,bar_length= 100,frame_width = 130):

        self.zero_frame =  LabelFrame(self.window, text="0")
        self.one_frame =   LabelFrame(self.window, text="1")
        self.two_frame =   LabelFrame(self.window, text="2")
        self.three_frame = LabelFrame(self.window, text="3")
        self.four_frame =  LabelFrame(self.window, text="4")
        self.five_frame =  LabelFrame(self.window, text="5")
        self.six_frame =   LabelFrame(self.window, text="6")
        self.seven_frame = LabelFrame(self.window, text="7")
        self.eight_frame = LabelFrame(self.window, text="8")
        self.nine_frame =  LabelFrame(self.window, text="9")

        self.zero_bar =  Progressbar(self.zero_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.one_bar =   Progressbar(self.one_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.two_bar =   Progressbar(self.two_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.three_bar = Progressbar(self.three_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.four_bar =  Progressbar(self.four_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.five_bar =  Progressbar(self.five_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.six_bar =   Progressbar(self.six_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.seven_bar = Progressbar(self.seven_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.eight_bar = Progressbar(self.eight_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)
        self.nine_bar =  Progressbar(self.nine_frame, orient=HORIZONTAL, length=bar_length, mode='determinate',value = 1, maximum = 100)

        self.pred_bars = [self.zero_bar,self.one_bar,self.two_bar,self.three_bar,self.four_bar,self.five_bar,self.six_bar,self.seven_bar,self.eight_bar,self.nine_bar]

        self.zero_frame.place(x=400, y=0, height=30, width=frame_width)
        self.one_frame.place(x=400,  y=pixel_distance, height=30, width=frame_width)
        self.two_frame.place(x= 400, y =pixel_distance*2 ,height = 30, width = frame_width)
        self.three_frame.place(x = 400,y = pixel_distance*3,height = 30,width = frame_width)
        self.four_frame.place(x = 400,y = pixel_distance*4,height = 30,width = frame_width)
        self.five_frame.place(x = 400,y = pixel_distance*5,height = 30,width = frame_width )
        self.six_frame.place(x = 400,y = pixel_distance*6,height = 30,width = frame_width)
        self.seven_frame.place(x = 400,y = pixel_distance*7,height = 30,width = frame_width)
        self.eight_frame.place(x = 400,y = pixel_distance*8,height = 30,width = frame_width)
        self.nine_frame.place(x = 400,y = pixel_distance*9,height = 30,width =frame_width )

        self.zero_bar.place(x=7, y=-2)
        self.one_bar.place(x=7, y=-2)
        self.two_bar.place(x=7, y=-2)
        self.three_bar.place(x=7, y=-2)
        self.four_bar.place(x=7, y=-2)
        self.five_bar.place(x=7, y=-2)
        self.six_bar.place(x=7, y=-2)
        self.seven_bar.place(x=7, y=-2)
        self.eight_bar.place(x=7, y=-2)
        self.nine_bar.place(x=7, y=-2)

    def show_stats(self,stat_list):

         for bar in self.pred_bars:

             amount = stat_list[self.pred_bars.index(bar)]
             bar['value'] = amount*1000
             self.window.update()

             #bar.step(amount = stat_list[self.pred_bars.index(bar)]*100)

    def clear_bars(self):

        for bar in self.pred_bars:

            bar['value'] = 1
            self.window.update()











