from model.group import Group
from model.contact import Contact
import random

def test_del_contact_from_group(app, db):
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    if len(old_groups) == 0:
        app.group.create(Group(name = "test"))
    if len(old_contacts) == 0:
        app.contact.create(Contact(firstname = "test"))
    contacts_in_group = db.get_contact_in_groups()
    if len(contacts_in_group) != 0:
        contact = random.choice(contacts_in_group)
        app.contact.remove_contact_from_group(contact)