import csv

import pytest

import config
from pages.product_page import ProductPage
from pages.products_page import ProductsPage

pytestmark = pytest.mark.ui


def get_search_data():
    data = []
    with open(config.DATA_DIR / "search_terms.csv", newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            data.append((row["term"], row["expect_results"] == "yes"))
    return data


def test_tc08_all_products(driver):
    pp = ProductsPage(driver).open()
    assert pp.get_title() == "ALL PRODUCTS"
    products = pp.get_products()
    assert len(products) > 0

    first = products[0]
    pp.view_product(first["id"])
    details = ProductPage(driver).get_details()
    assert details["name"] == first["name"]
    assert details["price"] == first["price"]
    for key in ["Category", "Availability", "Condition", "Brand"]:
        assert details.get(key), f"{key} not found: {details}"


@pytest.mark.parametrize("term, has_results", get_search_data())
def test_tc09_search_product(driver, term, has_results):
    pp = ProductsPage(driver).open()
    pp.search(term)
    assert pp.get_title() == "SEARCHED PRODUCTS"
    names = [p["name"] for p in pp.get_products()]
    if has_results:
        assert len(names) > 0, f"no results for {term}"
    else:
        assert len(names) == 0, f"got results for {term}: {names}"
