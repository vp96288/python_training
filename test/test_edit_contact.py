# -*- coding: utf-8 -*-
from model.contact import Contact

def test_modify_firstname_contact(app):
    app.contact.modify_first_contact(Contact(firstname="New firstname"))

def test_modify_lastname_contact(app):
    app.contact.modify_first_contact(Contact(lastname="New lastname"))