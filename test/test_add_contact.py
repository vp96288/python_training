# -*- coding: utf-8 -*-
from model.contact import Contact

def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="abra", lastname="kadabra", address="123 Troost avenue 123, Studio city", homenumber="5555555", worknumber="342424", mobilenumber="6666666", email="abra.kadabra@wellsfargo.com", email2="sadfs@fasdfa.asdf", email3="asfsfd@asdfasdf.asdfasdf", homepage="www.wellsfargo.com", dob_year="2000", notes="Some notes")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_new_contact(app):
#    old_contacts = app.contact.get_contact_list()
#    contact = Contact(firstname="Petrov", lastname="Ivanov", nickname="Zver", title="Developer", company="Citibank", address="333 Las Vegas", homenumber="6666666", mobilenumber="7777777", email="petrov.ivanov@gmail.com", homepage="www.citibank.com", dob_year="1994", notes="New notes")
#    app.contact.create(contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) + 1 == len(new_contacts)
#    old_contacts.append(contact)
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
