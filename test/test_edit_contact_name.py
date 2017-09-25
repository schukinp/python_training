# -*- coding: utf-8 -*-\

from model.edit_contact import EditContact

def test_edit_contact_name(app):
    app.contact.edit(EditContact(new_firstname="Ivan", new_lastname = "Ivanov"))

