from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


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
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))