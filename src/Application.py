from tkinter import *

from SessionManager import SessionManager
from Styles import Styles


class Application(Tk):

    def __init__(self, title):
        super().__init__()
        self.title(title)
        Styles()

        self.__session = SessionManager()

    # modifiers
    def set_title(self, title: str) -> None:
        """
        Sets the title of the root window.
        :param title: str
        :return: None
        """
        self.title(title)

    # accessors
    def get_session_manager(self):
        """
        Returns the SessionManager object in use.
        :return: SessionManager
        """
        return self.__session
