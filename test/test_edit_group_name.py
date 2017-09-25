# -*- coding: utf-8 -*-
def test_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit()
    app.session.logout()
