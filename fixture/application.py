from selenium.webdriver.firefox.webdriver import WebDriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from fixture.delete_group import DeleteGroupHelper
from fixture.group_name import GroupNameHelper
from fixture.contact_name import ContactNameHelper
from fixture.delete_contact import DeleteContactHelper

class Application:

    def __init__(self):
        self.wd = WebDriver(capabilities={"marionette": False},
                            firefox_binary="C:/Program Files/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.delete_group = DeleteGroupHelper(self)
        self.group_name = GroupNameHelper(self)
        self.contact_name = ContactNameHelper (self)
        self.delete_contact = DeleteContactHelper(self)

    def open_homepage(self):
        # open homepage
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()