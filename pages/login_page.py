from selenium.webdriver.common.by import By

from pages.base_page import BasePage, qa


class LoginPage(BasePage):
    PATH = "/login"
    LOGIN_ERR = (By.CSS_SELECTOR, ".login-form p")
    SIGNUP_ERR = (By.CSS_SELECTOR, ".signup-form p")

    def login(self, email, password):
        self.enter_text(qa("login-email"), email)
        self.enter_text(qa("login-password"), password)
        self.click(qa("login-button"))

    def signup(self, name, email):
        self.enter_text(qa("signup-name"), name)
        self.enter_text(qa("signup-email"), email)
        self.click(qa("signup-button"))

    def get_login_error(self):
        return self.get_text(self.LOGIN_ERR)

    def get_signup_error(self):
        return self.get_text(self.SIGNUP_ERR)
