import pytest

from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.products_page import ProductsPage

pytestmark = pytest.mark.ui


def test_tc12_add_products_to_cart(driver):
    pp = ProductsPage(driver).open()
    pp.add_to_cart(1)
    pp.continue_shopping()
    pp.add_to_cart(2)
    pp.click_view_cart()

    cart_items = CartPage(driver).get_cart_items()
    assert [i["id"] for i in cart_items] == [1, 2]
    for i in cart_items:
        assert i["quantity"] == 1
        assert i["total"] == i["price"] * i["quantity"]


def test_tc13_product_quantity(driver):
    p = ProductPage(driver).open(1)
    p.set_qty(4)
    p.add_to_cart()
    p.click_view_cart()

    cart_items = CartPage(driver).get_cart_items()
    assert len(cart_items) == 1
    assert cart_items[0]["quantity"] == 4
    assert cart_items[0]["total"] == cart_items[0]["price"] * 4


def test_tc17_remove_from_cart(driver):
    p = ProductPage(driver).open(1)
    p.add_to_cart()
    p.click_view_cart()

    cart = CartPage(driver)
    assert len(cart.get_cart_items()) == 1
    cart.delete_item(1)
    assert cart.is_cart_empty()
