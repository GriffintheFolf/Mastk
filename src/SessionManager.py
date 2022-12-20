# class for managing the current session: logins, data, etc.

from mastodon import *
from pathlib import Path
import os

MASTK_CLIENT_KEYFILE = "Mastk_client.secret"
MASTK_USERCREDS_FILE = "Mastk_usercreds.secret"


class SessionManager:

    def __init__(self, email: str = "", instance: str = "", password: str = ""):
        """
        A class to manage the active Mastodon login session.

        :param email: Email used to log in to the instance
        :param instance: The instance name, e.g. mastodon.social
        :param password: The password for the email
        """

        self.__email = email
        self.__instance_name = instance
        self.__password = password

        self.__api_instance = None
        self.__login_save_dir = Path("")

        # on Windows systems, save to AppData\Local\Mastk; on Unix-like systems
        # save to ~/.config/Mastk
        if os.name == "nt":
            self.__login_save_dir = Path(f"{os.getenv('LOCALAPPDATA')}/Mastk")
        else:
            self.__login_save_dir = Path(f"{os.path.expanduser('~')}/.config/Mastk")

    # modifiers
    def set_creds(self, email: str, instance: str, password: str):
        """
        Sets the email, instance, and password.
        :param email: Email used to log in to the instance
        :param instance: The instance name, e.g. mastodon.social
        :param password: The password for the email
        :return: None
        """
        self.__email = email
        self.__instance_name = instance
        self.__password = password

    def login(self):
        """
        Attempts to log in to the instance with the given email and password.

        Returns 0 on successful login, -1 if incorrect email/instance/password
        combination, -2 if other error.
        :return: int
        """

        # login will fail if the configuration directory doesn't exist yet
        if not self.__login_save_dir.exists():
            os.mkdir(self.__login_save_dir)
        if not Path(f"{self.__login_save_dir}/{MASTK_CLIENT_KEYFILE}").exists():
            Mastodon.create_app("Mastk",
                                api_base_url=f"https://{self.__instance_name}",
                                to_file=Path(f"{self.__login_save_dir}/{MASTK_CLIENT_KEYFILE}"))

        # attempt to login
        self.__api_instance = Mastodon(client_id=Path(f"{self.__login_save_dir}/{MASTK_CLIENT_KEYFILE}"))
        try:
            self.__api_instance.log_in(self.__email, self.__password,
                                       to_file=Path(f"{self.__login_save_dir}/{MASTK_USERCREDS_FILE}"))
        except MastodonIllegalArgumentError:
            return -1
        except MastodonAPIError:
            return -2

        # if we made it this far, we should be in now!
        print("we did it!")
        return 0
