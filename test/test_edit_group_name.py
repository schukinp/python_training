# -*- coding: utf-8 -*-
from model.edit_group import EditGroup

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(EditGroup(new_name="Hello world"))
    app.session.logout()
