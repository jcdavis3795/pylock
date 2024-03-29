import os
import sys

from models import Crypto, Locker
from config import CONFIG_DIR, MASTER_PASS_FILE, MASTER_KEY_FILE, PASS_FILE


master_locker = Locker.Locker('pylock', 'master_password', MASTER_PASS_FILE)
master_crypto = Crypto.Crypto(MASTER_PASS_FILE, MASTER_KEY_FILE)


def initialize(crypto: Crypto = master_crypto, locker: Locker = master_locker, directory: str = CONFIG_DIR,
               password_file: str = PASS_FILE, master_file: str = MASTER_PASS_FILE):
    """

    :param crypto:
    :param locker:
    :param directory:
    :param password_file:
    :param master_file:
    :return:
    """
    r = create_master_password(get_input())
    if r == 'Invalid entry: passwords do not match':
        print(r)
        sys.exit()
    else:
        os.makedirs(directory, exist_ok=True)
        with open(password_file, 'w'):
            pass
        with open(master_file, 'w'):
            pass
        locker.create(r)
        crypto.encrypt()


def get_input():
    return str(input('Enter the password you will use to access pylock. This is your master password and'
                                ' should not match any of the passwords that you will store within pylock: '))


def get_master(crypto: Crypto = master_crypto, locker: Locker = master_locker):
    """

    :param crypto:
    :param locker:
    :return:
    """
    crypto.decrypt()
    master_password = locker.read()
    crypto.encrypt()

    return master_password


def create_master_password(input_func):
    master_password = input_func
    return master_password
