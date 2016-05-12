# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_modify_firstname_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname = "test"))
    old_contacts = db.get_contact_list()
    random_index = random.choice(old_contacts)
    contact = Contact(firstname="Hello")
    contact.id = random_index.id
    app.contact.modify_contact_by_id(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

#def test_modify_group_name(app, db):
#    if len(db.get_group_list()) == 0:
#        app.group.create(Group(name = "test"))
#    old_groups = db.get_group_list()
#    random_group = random.choice(old_groups)
#    group = Group(name="New group")
##    group.id = random_group.id
#    app.group.modify_group_by_id(group)
#    new_groups = db.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_modify_lastname_contact(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname = "test"))
#    old_contacts = app.contact.get_contact_list()
#    app.contact.modify_first_contact(Contact(lastname="New lastname"))
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
