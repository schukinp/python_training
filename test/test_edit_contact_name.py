# -*- coding: utf-8 -*-
def test_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit()
    app.session.logout()
