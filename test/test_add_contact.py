# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address="", homenumber="", mobilenumber="", email="", homepage="", dob_year="", notes="")] + [
    Contact(firstname="John", lastname="Smith",
            title="Software developer", company="Facebook", address="4324 Moorpark street",
            homenumber="6538434", mobilenumber="5434584",
            email="john.smith@facebook.com", homepage="www.facebook.com", dob_year="1980",
            notes="here is some note")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            title=random_string("title", 10),
            notes=random_string("notes", 20))
    for i in range(5)
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

