# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="edit12313", lastname="edit1213", nickname="123edit", title="Manager", company="Chase", address="333 Los Angeles", homenumber="4444444", mobilenumber="9999999", email="editcontact@chase.com", homepage="www.chase.com", dob_year="1888", notes="Some new notes"))
    app.session.logout()
