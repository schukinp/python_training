# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
        old_contact = app.contact.get_contact_list()
        app.contact.create(Contact(firstname="Pavel", lastname="Shchukin", nickname="Junior", mobile="Email", email="schukinp@gmail.com"))
        new_contact = app.contact.get_contact_list()
        assert len(old_contact) + 1 == len(new_contact)


