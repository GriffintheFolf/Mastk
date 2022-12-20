# Mastodon login logic

from mastodon import *
from pathlib import Path
import os


save_directory = ""
mastodon = None


def login(email, instance, password):
    """
    Attempts to log in to the given Mastodon instance.

    Note: instance should be in the form of "instance.name".
    :param email: str
    :param instance: str
    :param password: str
    :return: None
    """
    global save_directory, mastodon

    # on Windows systems, save to AppData\Local\Mastk; on Unix-like systems
    # save to ~/.config/Mastk
    if os.name == "nt":
        save_directory = f"{os.getenv('LOCALAPPDATA')}\\Mastk"
    else:
        save_directory = f"{os.path.expanduser('~')}/.config/Mastk"

    if not Path(f"{save_directory}/Mastk_client.secret").exists():
        f = open(Path(f"{save_directory}/Mastk_client.secret"), "w")
        f.close()
        Mastodon.create_app("Mastk", api_base_url=f"https://{instance}", to_file=Path(f"{save_directory}/Mastk_client.secret"))

    # try to log in
    mastodon = Mastodon(client_id=f"{save_directory}/Mastk_client.secret")
    mastodon.log_in(email, password, to_file=f"{save_directory}/Mastk_creds.secret")


# testing
if __name__ == "__main__":
    email = "youreally@th.ink"
    password = "I'm going to tell you?"
    instance = "tech.lgbt"

    login(email, instance, password)

    # assuming all went well...
    mastodon = Mastodon(access_token=f"{save_directory}/Mastk_creds.secret")
    mastodon.toot("just trying out some stuff with the Mastodon API. did anyone receive this?")
