from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.helpers import get_price


class ProductsPage(BasePage):
    PATH = "/products"
    TITLE = (By.CSS_SELECTOR, ".features_items h2.title")
    SEARCH_INPUT = (By.ID, "search_product")
    SEARCH_BTN = (By.ID, "submit_search")
    PRODUCT_CARDS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")

    def get_title(self):
        return self.get_text(self.TITLE)

    def search(self, name):
        self.enter_text(self.SEARCH_INPUT, name)
        self.click(self.SEARCH_BTN)

    def get_products(self):
        product_list = []
        for card in self.get_elements(self.PRODUCT_CARDS):
            pid = card.find_element(By.CSS_SELECTOR, ".productinfo a.add-to-cart").get_attribute("data-product-id")
            name = card.find_element(By.CSS_SELECTOR, ".productinfo p").text.strip()
            price = card.find_element(By.CSS_SELECTOR, ".productinfo h2").text
            product_list.append({"id": int(pid), "name": name, "price": get_price(price)})
        return product_list

    def add_to_cart(self, pid):
        card = self.get_element((By.XPATH, f"//a[@data-product-id='{pid}']/ancestor::div[@class='product-image-wrapper']"))
        self.driver.execute_script("arguments[0].scrollIntoView({block:'center'});", card)
        ActionChains(self.driver).move_to_element(card).perform()
        self.click((By.CSS_SELECTOR, f".product-overlay a[data-product-id='{pid}']"))

    def view_product(self, pid):
        self.click((By.CSS_SELECTOR, f"a[href='/product_details/{pid}']"))
