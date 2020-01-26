import random
import string
import pytest


@pytest.fixture(params=[10, 11, 12])
def get_random_list(request):
    ran_numbers = []
    for i in range(request.param):
        ran_numbers.append(random.randint(1, 100))
    return ran_numbers


@pytest.fixture
def get_set():
    names_set_from_book = {'Wendy', 'Tinker Bell', 'Captain Hook.', 'Peter Pan', 'Lost Boys'}
    return names_set_from_book


@pytest.fixture(scope='session')
def get_dictionary():
    test_user = dict(user_id='10', username='Test_0', email='test@gmail.com', city='Test_City', lang='ru')
    return test_user


@pytest.fixture(scope='session', params=[11, 12, 13, 14])
def get_random_string(request):
    return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(request.param))
