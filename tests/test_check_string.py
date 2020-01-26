import pytest

NEW_VALUE = ['o', 'E', 's', 'm', 'A', '7', 'X']


@pytest.mark.parametrize('new_value', NEW_VALUE)
def test_add_value(get_random_string, new_value):
    """Проверка, длина строки увеличивается
    при добавлении нового элемента
    """
    first_string = get_random_string
    get_random_string += new_value
    assert len(get_random_string) == (len(first_string) + 1)


def test_string_isalnum(get_random_string):
    """Проверка, строка состоит из букв и цифр
    """
    assert get_random_string.isalnum()


def test_string_islower(get_random_string):
    """Проверка, строка состоит не только из символов
    в нижнем регистре
    """
    assert not get_random_string.islower()


def test_extract_nbr(get_random_string):
    """Проверка, выделение цифр из строки"""
    just_number = ''
    for i in get_random_string:
        if i.isdigit():
            just_number += i
    assert just_number.isdigit


def test_isspace(get_random_string):
    """Проверка, состоит ли строка из
     неотображаемых символов
    """
    assert not get_random_string.isspace()
