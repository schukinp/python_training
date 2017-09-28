# -*- coding: utf-8 -*-\

from model.contact import Contact

def test_edit_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Ivan", lastname="Ivanov"))
    app.contact.edit(Contact(firstname="Petr", lastname = "Petrov"))

