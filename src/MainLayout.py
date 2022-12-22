# main layout for the application when logged in
# note that the actual content is shown within the display_frame

from tkinter import *
from tkinter import ttk


class MainLayout:

    def __init__(self, root):
        """
        Forms the main layout of the UI when logged in.
        Does not grid the widgets yet!
        :param root: Application
        """

        self.display_frame = ttk.Frame(root.penultimo)
        self.sidebar = ttk.Frame(root.penultimo)
        self.sidebar_buttons = {}
        # relegated to separate function for organization
        self.__init_sidebar()

    def __init_sidebar(self):
        """
        Creates the buttons for the sidebar.
        :return: None
        """

        # note: images for buttons coming eventually
        self.sidebar_buttons = {
            "new_post": ttk.Button(self.sidebar, text="New Post"),
            "home": ttk.Button(self.sidebar, text="Home"),
            "my_profile": ttk.Button(self.sidebar, text="My Profile"),
            "settings": ttk.Button(self.sidebar, text="Settings")
        }

    def place(self):
        """
        Grids all the widgets on-screen.
        :return: None
        """
        self.display_frame.grid(row=0, column=0, columnspan=2)
        self.sidebar.grid(row=0, column=3)

        i = 0
        for button in self.sidebar_buttons:
            self.sidebar_buttons[button].grid(row=i, column=0, padx=5, pady=15)
            i += 1
