# class containing various font styles, etc.

from tkinter import *
from tkinter import ttk


class Styles:

    def __init__(self):
        s = ttk.Style()

        # font styles
        s.configure("Title.TLabel", font="helvetica 36", padding=5)
