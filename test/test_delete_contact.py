# -*- coding: utf-8 -*-
from model.contact import Contact

def test_delete_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    app.contact.delete()
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) - 1 == len(new_contact)
