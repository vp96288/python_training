# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", lastname="", nickname="", title="", company="", address="", homenumber="", mobilenumber="", email="", homepage="", dob_year="", notes="")] + [
    Contact(firstname=random_string("firstname", 10), lastname=random_string("lastname", 10),
            title=random_string("title", 10), company=random_string("company", 10), address=random_string("address", 20),
            homenumber=random_string("homenumber", 7), mobilenumber=random_string("mobilenumber", 7),
            email=random_string("email", 10), homepage=random_string("homepage", 20), dob_year=random_string("dob_year", 8),
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

