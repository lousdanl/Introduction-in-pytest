import random
import pytest


NUMBERS = [0, 1, 55, 99, 100]
NUMBERS_ID = [0, 3, 5, 8]


@pytest.mark.parametrize('number', NUMBERS)
def test_replacement_element(get_random_list, number):
    """ Проверка замены элемента
    в списке на указанное значение
    """
    ran_id = random.randint(0, 9)
    get_random_list.insert(ran_id, number)
    assert get_random_list[ran_id] == number


@pytest.mark.parametrize('number_id', NUMBERS_ID)
def test_deleted_element(get_random_list, number_id):
    """ Проверка длины списка
    после удаления элемента
    """
    list_length = len(get_random_list)
    del get_random_list[number_id]
    assert len(get_random_list) == (list_length-1)


def test_clear_list(get_random_list):
    """ Проверка длины списка
    после ощищения списка
    """
    get_random_list.clear()
    assert len(get_random_list) == 0


def test_even_numbers(get_random_list):
    """Проверка, после удаления нечетных чисел,
    значения в списке только четные
    """
    even_numbers = get_random_list.copy()
    for i in get_random_list:
        if i % 2 > 0:
            even_numbers.remove(i)
    if len(even_numbers) > 0:
        for i in even_numbers:
            assert i % 2 == 0
    else:
        print('All numbers were odd')


def test_sort_list(get_random_list):
    """Проверка корректной сортировки,
    следующее значение в списке больше предыдущего
    """
    get_random_list.sort()
    for number_id, number in enumerate(get_random_list):
        if number_id < (len(get_random_list)-1):
            assert get_random_list[number_id] <= get_random_list[number_id+1]
