import pytest


NEW_ID = [11, 12, 13, 14]
NEW_NAME = ['Test_1', 'Test_2', 'Test_3', 'Test_4']


def test_count_value_keys(get_dictionary):
    """Проверка, кол-во ключей равно кол-ву значений"""
    assert len(get_dictionary.values()) == len(get_dictionary.keys())


@pytest.mark.parametrize('new_value', NEW_ID)
def test_update_id(get_dictionary, new_value):
    """Проверка изменения значения в словаре"""
    new_dictionary = {'user_id': new_value}
    get_dictionary.update(new_dictionary)
    assert get_dictionary.get('user_id') == new_value


@pytest.mark.parametrize('new_value', NEW_NAME)
def test_update_name(get_dictionary, new_value):
    """Проверка изменения значения в словаре"""
    new_dictionary = {'username': new_value}
    get_dictionary.update(new_dictionary)
    assert get_dictionary.get('username') == new_value


def test_add_value(get_dictionary):
    """Проверка добавления элемента в словарь"""
    get_dictionary['country'] = 'Test_Country'
    assert get_dictionary.get('country') == 'Test_Country'


def test_add_emtpy_value(get_dictionary):
    """Проверка добавления ключа без значения"""
    assert get_dictionary.setdefault('age') is None
