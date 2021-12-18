from tkinter import *
import hashlib
import sqlite3


def UserApp(Frame):
    def __init__(self, container, username):
        Frame.__init__(self, container, username)
        self.container = container
        self.container.title("Shopee - User App")
        self.config(bg="white")
        self.pack(side="bottom", fill="both", expand=True)