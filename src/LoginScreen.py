# layout for screen displayed if not logged in

from tkinter import *
from tkinter import ttk

from Application import Application
from SessionManager import SessionManager


class LoginScreen:

    def __init__(self, root: Application, session: SessionManager):
        """
        Places the elements for the login screen onto the window.
        :param root: Application
        :param session: SessionManager
        """

        self.superframe = ttk.Frame(root.penultimo, padding=(15, 15, 15, 15))
        self.email = StringVar(None, "")
        self.instance = StringVar(None, "")
        self.__password = StringVar(None, "")
        self.status = StringVar(None, "")
        self.__session = session

        self.superframe.grid(row=0, column=0)
        self.welcome = ttk.Label(self.superframe, text="Welcome to Mastk!", style="Title.TLabel")
        self.welcome.grid(row=0, column=0, columnspan=2, pady=10, sticky="NW")

        ttk.Label(self.superframe, text="Email:").grid(row=1, column=0, sticky="NW")
        self.email_field = ttk.Entry(self.superframe, textvariable=self.email)
        self.email_field.grid(row=1, column=1, sticky="NWE")
        ttk.Label(self.superframe, text="Instance (domain.name):").grid(row=2, column=0, sticky="NW")
        self.instance_field = ttk.Entry(self.superframe, textvariable=self.instance)
        self.instance_field.grid(row=2, column=1, sticky="NWE")
        ttk.Label(self.superframe, text="Password:").grid(row=3, column=0, sticky="NWE")
        self.password_field = ttk.Entry(self.superframe, show="*", textvariable=self.__password)
        self.password_field.grid(row=3, column=1, sticky="NWE")

        self.status_label = ttk.Label(self.superframe, textvariable=self.status, style="Error.TLabel")
        self.status_label.grid(row=4, column=0, sticky="NWE")

        self.login = ttk.Button(self.superframe, text="Login", command=self.__login_cb)
        self.login.grid(row=4, column=1, sticky="NE")

        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        self.superframe.columnconfigure(0, weight=1)

    # modifiers
    def __login_cb(self):
        """
        Callback from the Login button; attempt to log in
        :return: None
        """

        # blah blah blah, ensure it's not empty
        if self.email.get() == "":
            self.status.set("Email not specified")
            return
        if self.instance.get() == "":
            self.status.set("Instance not specified")
            return
        if self.__password.get() == "":
            self.status.set("Password not specified")
            return

        self.__session.set_creds(self.email.get(), self.instance.get(), self.__password.get())
        status = self.__session.login()
        if status == -1:
            self.status.set("Login failed! Are your email, instance, and password correct?")
            return
        if status == -2:
            self.status.set("Oops! Something else went wrong...")
            return
