# layout for screen displayed if not logged in

from tkinter import *
from tkinter import ttk


class LoginScreen:

    def __init__(self, root: Tk):
        """
        Places the elements for the login screen onto the window.
        :param root: Tk
        """

        self.superframe = ttk.Frame(root, padding=(5, 5, 10, 10))
        self.username = StringVar()
        self.password = StringVar()

        self.superframe.grid(row=0, column=0)
        ttk.Label(self.superframe, text="Welcome to Mastk!", style="Title.TLabel").grid(row=0, column=0)
