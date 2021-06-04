from initialize import create_master_password, get_master, initialize
from models.Locker import Locker
from models.Crypto import Crypto
from tests.config_tests import TEST_DIR, TEST_PASS_FILE, TEST_MASTER_PASS_FILE, TEST_MASTER_KEY_FILE


def setup_module(module):
    master_test_locker = Locker('master_test_service', 'master_test_user', TEST_MASTER_PASS_FILE)
    master_test_crypto = Crypto(TEST_MASTER_PASS_FILE, TEST_MASTER_KEY_FILE)


class TestInitialize:

    @classmethod
    def setup_class(cls):
        master_test_locker = Locker('master_test_service', 'master_test_user', TEST_MASTER_PASS_FILE)
        master_test_crypto = Crypto(TEST_MASTER_PASS_FILE, TEST_MASTER_KEY_FILE)

    def test_create_master_password(self):
        test_input = 'test_master_password'

        output = create_master_password(test_input)

        assert output == test_input

# def test_initialize():
    # initialize(master_test_crypto, master_test_locker, TEST_DIR, TEST_PASS_FILE, TEST_MASTER_PASS_FILE)

    # def test_get_master(self):
        # get_master(master_test_crypto, master_test_locker)

