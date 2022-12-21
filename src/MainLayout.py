# main layout for the application when logged in
# note that the actual content is shown within the display_frame

from tkinter import *
from tkinter import ttk

from Application import Application


class MainLayout:

    def __init__(self, root: Application):
        """
        Forms the main layout of the UI when logged in.
        :param root: Application
        """

        self.display_frame = ttk.Frame(root.penultimo)
        self.display_frame.grid(row=0, column=0, columnspan=2)

        self.sidebar = ttk.Frame(root.penultimo)
        self.sidebar.grid(row=0, column=3)
