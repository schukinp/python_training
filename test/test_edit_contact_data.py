# -*- coding: utf-8 -*-\

from model.contact import Contact

def test_edit_contact_data(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    app.contact.edit(Contact(firstname="Petr", lastname = "Petrov"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact) == len(new_contact)

