from selenium.webdriver.common.by import By

from pages.base_page import BasePage, qa


class SignupPage(BasePage):
    PATH = "/signup"

    FIELDS = {"first_name": "firstname", "last_name": "lastname", "company": "company",
              "address": "address1", "address2": "address2", "state": "state",
              "city": "city", "zipcode": "zipcode", "mobile_number": "mobile_number"}

    def fill_details(self, user):
        if user["title"] == "Mr":
            self.click((By.ID, "id_gender1"))
        else:
            self.click((By.ID, "id_gender2"))
        self.enter_text(qa("password"), user["password"])
        self.select_dropdown(qa("days"), value=user["birth_date"])
        self.select_dropdown(qa("months"), value=user["birth_month"])
        self.select_dropdown(qa("years"), value=user["birth_year"])
        for field in self.FIELDS:
            self.enter_text(qa(field), user[self.FIELDS[field]])
        self.select_dropdown(qa("country"), text=user["country"])

    def click_create_account(self):
        self.click(qa("create-account"))
