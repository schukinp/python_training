# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
        app.contact.create(Contact(firstname="Pavel", lastname="Shchukin", nickname="Junior", mobile="Email", email="schukinp@gmail.com"))


