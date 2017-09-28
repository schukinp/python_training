# -*- coding: utf-8 -*-
from model.group import Group
def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Test"))
    app.group.edit(Group(name="New name"))

#def test_edit_group_header(app):
   #app.group.edit(Group(header="New header"))