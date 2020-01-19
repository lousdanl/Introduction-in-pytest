import random
import pytest


@pytest.fixture
def get_random_list():
    ran_numbers = []
    for i in range(10):
        ran_numbers.append(random.randint(1, 100))
    return ran_numbers





