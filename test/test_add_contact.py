# -*- coding: utf-8 -*-

from model.contact import Contact

def test_add_contact(app):
        old_contacts = app.contact.get_contact_list()
        contact = Contact(firstname="Pavel", lastname="Shchukin", nickname="Junior", mobile="9211111111", email="schukinp@gmail.com")
        app.contact.create(contact)
        new_contacts = app.contact.get_contact_list()
        assert len(old_contacts) + 1 == len(new_contacts)
        old_contacts.append(contact)
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(old_contacts, key=Contact.id_or_max)




