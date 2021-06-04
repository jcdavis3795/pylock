from models.Crypto import Crypto
from tests.config_tests import TEST_PASS_FILE, TEST_PASS_KEY_FILE

test_crypto = Crypto(TEST_PASS_FILE, TEST_PASS_KEY_FILE)


def test_encrypt():
    r = test_crypto.encrypt()

    assert r == 'file encrypted'


def test_decrypt():
    r = test_crypto.decrypt()

    assert r == 'file decrypted'
