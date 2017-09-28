class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        # add new contact
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def edit(self, new_contact_data):
        wd = self.app.wd
        self.select_contact()
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_contact_value("firstname", contact.firstname)
        self.change_contact_value("lastname", contact.lastname)
        self.change_contact_value("nickname", contact.nickname)
        self.change_contact_value("mobile", contact.mobile)
        self.change_contact_value("email", contact.email)

    def change_contact_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def select_contact(self):
        wd = self.app.wd
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()

    def delete(self):
        wd = self.app.wd
        self.select_contact()
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        wd.switch_to_alert().accept()
        wd.find_element_by_link_text("home")

    def count (self):
        wd = self.app.wd
        return len(wd.find_elements_by_name("selected[]"))

