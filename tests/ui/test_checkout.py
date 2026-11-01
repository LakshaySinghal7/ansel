import pytest
import requests

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage, PaymentPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.data_factory import card_details

pytestmark = pytest.mark.ui


def test_tc16_place_order(driver, reg_user):
    u = reg_user
    LoginPage(driver).open().login(u["email"], u["password"])

    p = ProductPage(driver).open(2)
    p.add_to_cart()
    p.click_view_cart()
    cart = CartPage(driver)
    total = sum(i["total"] for i in cart.get_cart_items())
    cart.click_checkout()

    cp = CheckoutPage(driver)
    for addr in [cp.get_delivery_address(), cp.get_billing_address()]:
        for val in [u["firstname"] + " " + u["lastname"], u["address1"], u["city"],
                    u["country"], u["mobile_number"]]:
            assert val in addr, f"{val} not in address: {addr}"
    assert cp.get_total() == total

    cp.place_order("test order")
    pay = PaymentPage(driver)
    pay.enter_card_and_pay(card_details())
    assert pay.get_msg("order-placed") == "ORDER PLACED!"

    cookies = {c["name"]: c["value"] for c in driver.get_cookies()}
    r = requests.get(pay.get_invoice_link(), cookies=cookies, timeout=30)
    assert r.status_code == 200
    assert str(total) in r.text
