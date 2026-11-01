import pytest

pytestmark = pytest.mark.api

NOT_SUPPORTED = "This request method is not supported."


def test_api01_get_products(api):
    r = api.get_products()
    res = r.json()
    assert r.status_code == 200
    assert res["responseCode"] == 200
    assert len(res["products"]) > 0
    assert {"id", "name", "price", "brand", "category"} <= res["products"][0].keys()
    assert r.elapsed.total_seconds() < 5


def test_api02_post_products(api):
    res = api.get_products(method="POST").json()
    assert res["responseCode"] == 405
    assert res["message"] == NOT_SUPPORTED


def test_api03_get_brands(api):
    res = api.get_brands().json()
    assert res["responseCode"] == 200
    for b in res["brands"]:
        assert "id" in b and "brand" in b


def test_api04_put_brands(api):
    res = api.get_brands(method="PUT").json()
    assert res["responseCode"] == 405
    assert res["message"] == NOT_SUPPORTED


@pytest.mark.parametrize("name", ["top", "tshirt", "jean"])
def test_api05_search_product(api, name):
    res = api.search_product(name).json()
    assert res["responseCode"] == 200
    assert len(res["products"]) > 0


def test_api06_search_without_param(api):
    res = api.search_product().json()
    assert res["responseCode"] == 400
    assert res["message"] == "Bad request, search_product parameter is missing in POST request."
