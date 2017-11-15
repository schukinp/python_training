# -*- coding: utf-8 -*-\

from model.contact import Contact
import random

def test_edit_contact_data(app, db, check_ui):
    if len(db.get_contact_list_from_db()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    old_contacts = db.get_contact_list_from_db()
    new_data = Contact(firstname="Petr", lastname="Petrov")
    contact = random.choice(old_contacts)
    app.contact.edit_contact_by_id(contact.id, new_data)
    new_contacts = db.get_contact_list_from_db()
    assert len(old_contacts) == len(new_contacts)
    index = old_contacts.index(contact)
    old_contacts[index] = new_data
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)

