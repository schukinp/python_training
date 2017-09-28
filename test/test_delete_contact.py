# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    app.contact.delete()
