from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.contact_session import SessionHelper
from fixture.contact import ContactHelper




class Application2:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/edit.php")

    def destroy(self):
        self.wd.quit()