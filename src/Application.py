from tkinter import *
from tkinter import ttk

from MainLayout import MainLayout
from SessionManager import SessionManager
from Styles import Styles


class Application(Tk):

    def __init__(self, title):
        super().__init__()
        self.title(title)
        Styles()

        self.penultimo = ttk.Frame(self)
        self.penultimo.grid(row=0, column=0)

        # screens and other management
        self.__session = SessionManager()
        self.layout = MainLayout(self)

        # menu bar
        self.option_add("*tearOff", FALSE)
        self.menu_bar = Menu(self)

        # macOS needs special handling
        if self.tk.call("tk", "windowingsystem") == "aqua":
            self.applemenu = Menu(self.menu_bar, name="apple")
            self.menu_bar.add_cascade(menu=self.applemenu)
            self.applemenu.add_command(label="About Mastk")
            self.applemenu.add_separator()

        self["menu"] = self.menu_bar
        self.menu_items = {
            "file": Menu(self.menu_bar),
            "help": Menu(self.menu_bar)
        }

        self.menu_bar.add_cascade(menu=self.menu_items["file"], label="File")
        self.menu_bar.add_cascade(menu=self.menu_items["help"], label="Help")

        # don't put the close button in the File menu on macOS
        if self.tk.call("tk", "windowingsystem") != "aqua":
            self.menu_items["file"].add_command(label="Quit", accelerator="Alt+F4", command=self.close)
        else:
            self.createcommand("tk::mac::Quit", self.close)

    # modifiers
    def set_title(self, title: str) -> None:
        """
        Sets the title of the root window.
        :param title: str
        :return: None
        """
        self.title(title)

    def clear_penultimo(self):
        """
        Destroys all child widgets of penultimo, the penultimate frame.
        :return: None
        """
        for widget in self.penultimo.winfo_children():
            widget.destroy()

    # accessors
    def get_session_manager(self):
        """
        Returns the SessionManager object in use.
        :return: SessionManager
        """
        return self.__session

    def close(self):
        """
        Cleans up and closes the application.
        :return: None
        """
        self.quit()
        exit()
