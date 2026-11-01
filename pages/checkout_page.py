from selenium.webdriver.common.by import By

from pages.base_page import BasePage, qa
from utils.helpers import get_price


class CheckoutPage(BasePage):
    PATH = "/checkout"
    DELIVERY_ADDR = (By.ID, "address_delivery")
    BILLING_ADDR = (By.ID, "address_invoice")
    ORDER_ROWS = (By.CSS_SELECTOR, "#cart_info tbody tr")
    COMMENT_BOX = (By.NAME, "message")
    PLACE_ORDER_BTN = (By.XPATH, "//a[contains(., 'Place Order')]")

    def get_delivery_address(self):
        return self.get_text(self.DELIVERY_ADDR)

    def get_billing_address(self):
        return self.get_text(self.BILLING_ADDR)

    def get_total(self):
        self.get_element(self.DELIVERY_ADDR)
        rows = self.get_elements(self.ORDER_ROWS)
        return get_price(rows[-1].text)

    def place_order(self, comment=""):
        self.enter_text(self.COMMENT_BOX, comment)
        self.click(self.PLACE_ORDER_BTN)


class PaymentPage(BasePage):
    PATH = "/payment"
    INVOICE_BTN = (By.XPATH, "//a[contains(., 'Download Invoice')]")

    def enter_card_and_pay(self, card):
        self.enter_text(qa("name-on-card"), card["name"])
        self.enter_text(qa("card-number"), card["number"])
        self.enter_text(qa("cvc"), card["cvc"])
        self.enter_text(qa("expiry-month"), card["month"])
        self.enter_text(qa("expiry-year"), card["year"])
        self.click(qa("pay-button"))

    def get_invoice_link(self):
        return self.get_element(self.INVOICE_BTN).get_attribute("href")
