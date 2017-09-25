# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
        app.session.login(username="admin", password="secret")
        app.contact.new(Contact(firstname="Pavel", lastname="Shchukin", nickname="Junior", mobile="Email", email="schukinp@gmail.com"))
        app.session.logout()
