# layout for screen displayed if not logged in

from tkinter import *
from tkinter import ttk


class LoginScreen:

    def __init__(self, root: Tk):
        """
        Places the elements for the login screen onto the window.
        :param root: Tk
        """

        self.superframe = ttk.Frame(root, padding=(15, 15, 15, 15))
        self.username = StringVar()
        self.password = StringVar()
        self.status = StringVar(None, "")

        self.superframe.grid(row=0, column=0)
        self.welcome = ttk.Label(self.superframe, text="Welcome to Mastk!", style="Title.TLabel")
        self.welcome.grid(row=0, column=0, columnspan=2, pady=10, sticky="NW")

        ttk.Label(self.superframe, text="Username (username@instance.name):").grid(row=1, column=0, sticky="NW")
        self.username_field = ttk.Entry(self.superframe, textvariable=self.username)
        self.username_field.grid(row=1, column=1, sticky="NWE")
        ttk.Label(self.superframe, text="Password:").grid(row=2, column=0, sticky="NWE")
        self.password_field = ttk.Entry(self.superframe, show="*", textvariable=self.password)
        self.password_field.grid(row=2, column=1, sticky="NWE")

        self.status = ttk.Label(self.superframe, textvariable=self.status, style="Error.TLabel")
        self.status.grid(row=4, column=0, sticky="NWE")

        self.login = ttk.Button(self.superframe, text="Login")
        self.login.grid(row=4, column=1, sticky="NE")

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        self.superframe.columnconfigure(0, weight=1)
