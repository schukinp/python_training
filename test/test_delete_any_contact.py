# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_delete_any_contact(app, db, check_ui):
    if len(db.get_contact_list_from_db()) == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    old_contacts = db.get_contact_list_from_db()
    group = random.choice(old_contacts)
    app.contact.delete_contact_by_id(group.id)
    new_contacts = db.get_contact_list_from_db()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(group)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
