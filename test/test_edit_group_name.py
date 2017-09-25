# -*- coding: utf-8 -*-
from model.edit_group import EditGroup

def test_edit_group_name(app):
    app.group.edit(EditGroup(new_name="Hello world"))

