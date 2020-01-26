import pytest


NAMES = ['Wendy', 'Tinker Bell', 'Captain Hook.', 'Peter Pan', 'Lost Boys']


def test_type_data(get_set):
    """Проверка типа структуры данных"""
    assert isinstance(get_set, set)


@pytest.mark.parametrize('name', NAMES)
def test_item_on_set(get_set, name):
    """Проверка, ожидаемый элемент
    входит во множество
    """
    assert name in get_set


@pytest.mark.parametrize('name', NAMES)
def test_duplicate_get_set(get_set, name):
    """Проверка, множество не содержит дубликатов"""
    duplicate_get_set = get_set.copy()
    get_set.add(name)
    assert len(get_set) == len(duplicate_get_set)


@pytest.mark.parametrize('name', NAMES)
def test_remove_element(get_set, name):
    """Проверка, удаление элемента из множества"""
    duplicate_get_set = get_set.copy()
    get_set.remove(name)
    assert len(get_set) == (len(duplicate_get_set) - 1)


def test_clear_get_set(get_set):
    """Проверка, очистка множества"""
    get_set.clear()
    assert len(get_set) == 0
