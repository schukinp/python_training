# -*- coding: utf-8 -*-

from model.group import Group
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " " #строка из набор букв и цифр
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]) #многократный выбор случайных символов из строки
    #выбор случайной длины не превышающей max


testdata = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 10), header=random_string("header", 20), footer=random_string("footer", 20))
for i in range(5)]


@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
#group - параметр, в который передаются тестовые данные, testdata - источник тестовых данных
#repr - текстовое представление тестовых данных в тесте. Можно записать как str()
#for x on testdata - цикл для каждого значения тестовых данных в переменной testdata
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)




