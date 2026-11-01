from selenium.webdriver.common.by import By

import config
from pages.base_page import BasePage
from utils.helpers import get_price


class ProductPage(BasePage):
    INFO = (By.CSS_SELECTOR, ".product-information")
    QTY = (By.ID, "quantity")
    ADD_BTN = (By.CSS_SELECTOR, ".product-information button.cart")

    def open(self, pid):
        self.driver.get(f"{config.BASE_URL}/product_details/{pid}")
        return self

    def get_details(self):
        lines = [l.strip() for l in self.get_text(self.INFO).splitlines() if l.strip()]
        details = {"name": lines[0]}
        for l in lines[1:]:
            if l.startswith("Rs."):
                details["price"] = get_price(l)
            elif ":" in l:
                k, v = l.split(":", 1)
                details[k.strip()] = v.strip()
        return details

    def set_qty(self, qty):
        self.enter_text(self.QTY, str(qty))

    def add_to_cart(self):
        self.click(self.ADD_BTN)
