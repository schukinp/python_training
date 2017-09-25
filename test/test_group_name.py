# -*- coding: utf-8 -*-
def test_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group_name.change()
    app.session.logout()
