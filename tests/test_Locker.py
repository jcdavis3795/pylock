from models.Locker import Locker
from tests.config_tests import TEST_PASS_FILE

test_locker_create = Locker('test_create_service', 'test_create_user', TEST_PASS_FILE)
test_locker_create_2 = Locker('test_create_service_2', 'test_create_user_2', TEST_PASS_FILE)
test_locker_read = Locker('test_read_service', 'test_read_user', TEST_PASS_FILE)
test_locker_fail = Locker('test_read_service_fail', 'test_read_user_fail', TEST_PASS_FILE)
test_locker_update = Locker('test_update_service', 'test_update_user', TEST_PASS_FILE)
test_locker_delete = Locker('test_delete_service', 'test_delete_user', TEST_PASS_FILE)


def test_create():
    test_create_password = 'test_password'
    test_create_password_2 = 'test_password_2'
    test_create_fail_password = 'credentials_already_exist'

    test_login = test_locker_create.create(test_create_password)
    test_login_2 = test_locker_create_2.create(test_create_password_2)
    test_login_3 = test_locker_create.create(test_create_fail_password)

    assert test_login and test_login_2 == 'login created', test_login_3 == 'credentials already exist'


def test_read():
    test_read_password = 'read_this_password'

    test_locker_read.create(test_read_password)
    test_read_success = test_locker_read.read()
    test_read_fail = test_locker_fail.read()

    assert test_read_success == test_read_password, test_read_fail == 'credentials invalid'


def test_update():
    test_update_password = 'update_this_password'
    test_password_updated = 'updated_test_password'

    test_locker_update.create(test_update_password)
    test_update_success = test_locker_update.update(test_password_updated)
    test_update_fail = test_locker_fail.update(test_password_updated)

    assert test_update_success == 'credentials updated', test_update_fail == 'credentials invalid'


def test_delete():
    test_delete_password = 'delete_this_password'
    test_locker_delete.create(test_delete_password)

    success_response = test_locker_delete.delete()

    response = test_locker_delete.read()

    assert success_response == 'deletion successful', response == 'credentials invalid'
