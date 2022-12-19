from tkinter import *
from tkinter import ttk


class Application(Tk):

    def __init__(self, title):
        super().__init__()
        self.title(title)

    # modifiers
    def set_title(self, title: str):
        """
        Sets the title of the root window.
        :param title: str
        :return:
        """
        self.title(title)
