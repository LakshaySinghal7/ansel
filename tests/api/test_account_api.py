import pytest

from utils.data_factory import make_user

pytestmark = pytest.mark.api


def test_api07_verify_login_valid(api, reg_user):
    res = api.verify_login(reg_user["email"], reg_user["password"]).json()
    assert res["responseCode"] == 200
    assert res["message"] == "User exists!"


def test_api08_verify_login_no_email(api):
    res = api.verify_login(password="Test@12345").json()
    assert res["responseCode"] == 400
    assert res["message"] == "Bad request, email or password parameter is missing in POST request."


def test_api09_delete_verify_login(api):
    res = api.verify_login(method="DELETE").json()
    assert res["responseCode"] == 405
    assert res["message"] == "This request method is not supported."


def test_api10_verify_login_invalid(api):
    res = api.verify_login("wrong_user_123@mailinator.com", "WrongPass1").json()
    assert res["responseCode"] == 404
    assert res["message"] == "User not found!"


def test_api11_12_create_delete_account(api):
    u = make_user()
    res = api.create_account(u).json()
    assert res["responseCode"] == 201
    assert res["message"] == "User created!"

    res = api.delete_account(u["email"], u["password"]).json()
    assert res["responseCode"] == 200
    assert res["message"] == "Account deleted!"

    res = api.verify_login(u["email"], u["password"]).json()
    assert res["responseCode"] == 404


def test_api13_update_account(api, reg_user):
    updated = dict(reg_user)
    updated["city"] = "Lucknow"
    res = api.update_account(updated).json()
    assert res["responseCode"] == 200
    assert res["message"] == "User updated!"
    assert api.get_user(reg_user["email"]).json()["user"]["city"] == "Lucknow"


def test_api14_get_user_by_email(api, reg_user):
    res = api.get_user(reg_user["email"]).json()
    assert res["responseCode"] == 200
    assert res["user"]["email"] == reg_user["email"]
    assert res["user"]["name"] == reg_user["name"]
    assert res["user"]["city"] == reg_user["city"]
