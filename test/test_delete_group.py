# -*- coding: utf-8 -*-
def test_delete_group(app):
    app.session.login(username="admin", password="secret")
    app.delete_group.delete()
    app.session.logout()