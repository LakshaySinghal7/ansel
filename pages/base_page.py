from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

import config


def qa(name):
    return (By.CSS_SELECTOR, f"[data-qa='{name}']")


class BasePage:
    PATH = "/"

    LOGGED_IN = (By.XPATH, "//a[contains(., 'Logged in as')]")
    LOGOUT = (By.XPATH, "//a[contains(., 'Logout')]")
    DELETE_ACC = (By.XPATH, "//a[contains(., 'Delete Account')]")
    CONTINUE_SHOPPING = (By.CSS_SELECTOR, "#cartModal .close-modal")
    VIEW_CART = (By.XPATH, "//div[@id='cartModal']//a[contains(., 'View Cart')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.TIMEOUT)

    def open(self):
        self.driver.get(config.BASE_URL + self.PATH)
        return self

    def get_element(self, loc):
        return self.wait.until(EC.visibility_of_element_located(loc))

    def get_elements(self, loc):
        return self.driver.find_elements(*loc)

    def click(self, loc):
        self.wait.until(EC.element_to_be_clickable(loc)).click()

    def enter_text(self, loc, txt):
        el = self.get_element(loc)
        el.clear()
        el.send_keys(txt)

    def get_text(self, loc):
        return self.get_element(loc).text.strip()

    def select_dropdown(self, loc, value=None, text=None):
        dd = Select(self.get_element(loc))
        if value is not None:
            dd.select_by_value(value)
        else:
            dd.select_by_visible_text(text)

    def is_displayed(self, loc, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(loc))
            return True
        except TimeoutException:
            return False

    def get_logged_user(self):
        if not self.is_displayed(self.LOGGED_IN):
            return None
        return self.get_text(self.LOGGED_IN).replace("Logged in as", "").strip()

    def logout(self):
        self.click(self.LOGOUT)

    def delete_account(self):
        self.click(self.DELETE_ACC)

    def get_msg(self, name):
        return self.get_text(qa(name))

    def click_continue(self):
        self.click(qa("continue-button"))

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING)
        self.wait.until(EC.invisibility_of_element_located(self.CONTINUE_SHOPPING))

    def click_view_cart(self):
        self.click(self.VIEW_CART)
