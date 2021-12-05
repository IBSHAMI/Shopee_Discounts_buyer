from tkinter import *


# page to log in and register
class ResultsPage(Frame):

    def __init__(self, container):
        Frame.__init__(self, container)
        self.container = container
        self.config(bg="#393e46")
        self.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.read_results_data()