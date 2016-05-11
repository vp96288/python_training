from model.contact import Contact
import random
import string

constant = [
    Contact(firstname="firstname1", lastname="lastname1", title="title1", company="company1", address="address1",
            homenumber="1111111", mobilenumber="2222222",
            email="email1@email.com", homepage="homepage1", dob_year="1980",
            notes="notes1")
]

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