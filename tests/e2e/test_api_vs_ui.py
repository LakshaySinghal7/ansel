import pytest

from pages.products_page import ProductsPage
from utils.helpers import get_price

pytestmark = pytest.mark.e2e


def test_products_ui_vs_api(driver, api):
    api_data = {}
    for p in api.get_products().json()["products"]:
        api_data[p["id"]] = p
    ui_data = ProductsPage(driver).open().get_products()

    assert len(ui_data) == len(api_data)
    errors = []
    for p in ui_data:
        exp = api_data.get(p["id"])
        if exp is None:
            errors.append(f"{p['id']} missing in api")
        elif p["name"] != exp["name"] or p["price"] != get_price(exp["price"]):
            errors.append(f"{p['id']}: ui={p['name']} {p['price']} api={exp['name']} {exp['price']}")
    assert not errors, "\n".join(errors)
