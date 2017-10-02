# -*- coding: utf-8 -*-
from model.group import Group

def test_edit_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.edit(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

#def test_edit_group_header(app):
   #app.group.edit(Group(header="New header"))