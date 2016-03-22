# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application2 import Application2

@pytest.fixture
def app(request):
    fixture = Application2()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="abra", lastname="kadabra", nickname="bum", title="Engineer", company="Wellsfargo", address="555 New York", homenumber="5555555", mobilenumber="6666666", email="abra.kadabra@wellsfargo.com", homepage="www.wellsfargo.com", dob_year="2000", notes="Some notes"))
    app.logout()

def test_add_new_contact(app):
    app.login(username="admin", password="secret")
    app.create_new_contact(Contact(firstname="Petrov", lastname="Ivanov", nickname="Zver", title="Developer", company="Citibank", address="333 Las Vegas", homenumber="6666666", mobilenumber="7777777", email="petrov.ivanov@gmail.com", homepage="www.citibank.com", dob_year="1994", notes="New notes"))
    app.logout()
