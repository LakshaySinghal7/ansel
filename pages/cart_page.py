from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from utils.helpers import get_price


class CartPage(BasePage):
    PATH = "/view_cart"
    CART_TABLE = (By.ID, "cart_info_table")
    CART_ROWS = (By.CSS_SELECTOR, "#cart_info_table tbody tr[id^='product-']")
    EMPTY_CART = (By.ID, "empty_cart")
    CHECKOUT_BTN = (By.CSS_SELECTOR, ".check_out")

    def get_cart_items(self):
        self.get_element(self.CART_TABLE)
        cart_items = []
        for row in self.get_elements(self.CART_ROWS):
            cart_items.append({
                "id": int(row.get_attribute("id").split("-")[1]),
                "name": row.find_element(By.CSS_SELECTOR, ".cart_description h4").text.strip(),
                "price": get_price(row.find_element(By.CSS_SELECTOR, ".cart_price").text),
                "quantity": int(row.find_element(By.CSS_SELECTOR, ".cart_quantity").text.strip()),
                "total": get_price(row.find_element(By.CSS_SELECTOR, ".cart_total").text),
            })
        return cart_items

    def delete_item(self, pid):
        self.click((By.CSS_SELECTOR, f"#product-{pid} .cart_quantity_delete"))
        self.wait.until(EC.invisibility_of_element_located((By.ID, f"product-{pid}")))

    def is_cart_empty(self):
        return self.is_displayed(self.EMPTY_CART)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)
