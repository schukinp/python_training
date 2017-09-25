class DeleteGroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        # open groups page
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def delete(self):
        wd = self.app.wd
        self.open_groups_page()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("delete").click()
        self.return_to_groups()

    def return_to_groups(self):
        # return to groups page
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()