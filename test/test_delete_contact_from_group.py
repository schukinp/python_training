from fixture.orm import ORMfixture
from model.group import Group
from model.contact import Contact

import random

db = ORMfixture(host='127.0.0.1', name='addressbook', user='root', password='')


def test_delete_contact_from_group(app):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(firstname="Russel", lastname="Westbrook"))
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Test"))
        old_contacts = db.get_contact_list()
        old_groups = db.get_group_list()
        contact = random.choice(old_contacts)
        group = random.choice(old_groups)
        old_contacts_in_group = db.get_contacts_in_group(group)
        if len(db.get_contacts_in_group(group)) == 0:
            app.contact.add_contact_to_group(contact, group)
        else:
            contact = random.choice(old_contacts_in_group)
        old_contacts_in_group_update = db.get_contacts_in_group(group)
        app.contact.delete_contact_from_group(contact, group)
        new_contacts_in_group = db.get_contacts_in_group(group)
        assert len(old_contacts_in_group_update) - 1 == len(new_contacts_in_group)
        old_contacts_in_group_update.remove(contact)
        assert sorted(old_contacts_in_group_update, key=Contact.id_or_max) == sorted(new_contacts_in_group, key=Contact.id_or_max)
