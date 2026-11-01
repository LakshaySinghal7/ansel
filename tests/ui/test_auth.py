import pytest

from pages.login_page import LoginPage
from pages.signup_page import SignupPage

pytestmark = pytest.mark.ui


def test_tc01_register_user(driver, user):
    lp = LoginPage(driver).open()
    lp.signup(user["name"], user["email"])

    sp = SignupPage(driver)
    sp.fill_details(user)
    sp.click_create_account()
    assert sp.get_msg("account-created") == "ACCOUNT CREATED!"

    sp.click_continue()
    assert sp.get_logged_user() == user["name"]

    sp.delete_account()
    assert sp.get_msg("account-deleted") == "ACCOUNT DELETED!"


def test_tc02_login_valid(driver, reg_user):
    lp = LoginPage(driver).open()
    lp.login(reg_user["email"], reg_user["password"])
    assert lp.get_logged_user() == reg_user["name"]


def test_tc03_login_invalid(driver):
    lp = LoginPage(driver).open()
    lp.login("wrong_user_123@mailinator.com", "WrongPass1")
    assert lp.get_login_error() == "Your email or password is incorrect!"
    assert lp.get_logged_user() is None


def test_tc04_logout(driver, reg_user):
    lp = LoginPage(driver).open()
    lp.login(reg_user["email"], reg_user["password"])
    lp.logout()
    assert driver.current_url.endswith("/login")
    assert lp.get_logged_user() is None


def test_tc05_register_existing_email(driver, reg_user):
    lp = LoginPage(driver).open()
    lp.signup("Another User", reg_user["email"])
    assert lp.get_signup_error() == "Email Address already exist!"
