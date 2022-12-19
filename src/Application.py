from tkinter import *
from tkinter import ttk

from Styles import Styles


class Application(Tk):

    def __init__(self, title):
        super().__init__()
        self.title(title)
        Styles()

    # modifiers
    def set_title(self, title: str) -> None:
        """
        Sets the title of the root window.
        :param title: str
        :return: None
        """
        self.title(title)
