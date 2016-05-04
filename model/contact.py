from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname=None, nickname=None, title=None, company=None, address=None, homenumber=None, mobilenumber=None, worknumber = None, all_phones_from_home_page=None, email=None, email2=None, email3=None, all_emails_from_home_page=None, homepage=None, dob_year=None, notes=None, id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homenumber = homenumber
        self.worknumber = worknumber
        self.mobilenumber = mobilenumber
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.dob_year = dob_year
        self.notes = notes
        self.all_emails_from_home_page = all_emails_from_home_page
        self.all_phones_from_home_page = all_phones_from_home_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and\
               self.firstname == other.firstname or self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize