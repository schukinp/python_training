# -*- coding: utf-8 -*-\

from model.edit_contact import EditContact

def test_edit_contact_name(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(EditContact(new_firstname="Ivan", new_lastname = "Ivanov"))
    app.session.logout()
