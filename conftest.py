import pytest
import pytest_html
from selenium import webdriver

import config
from api.client import ApiClient
from utils.data_factory import make_user


@pytest.fixture
def driver():
    opts = webdriver.ChromeOptions()
    if config.HEADLESS:
        opts.add_argument("--headless=new")
    opts.add_argument("--window-size=1366,900")
    drv = webdriver.Chrome(options=opts)
    # block ads
    drv.execute_cdp_cmd("Network.enable", {})
    drv.execute_cdp_cmd("Network.setBlockedURLs", {"urls": config.AD_URLS})
    yield drv
    drv.quit()


@pytest.fixture(scope="session")
def api():
    return ApiClient(config.BASE_URL)


@pytest.fixture
def user(api):
    u = make_user()
    yield u
    api.delete_account(u["email"], u["password"])


@pytest.fixture
def reg_user(api):
    u = make_user()
    res = api.create_account(u).json()
    assert res["responseCode"] == 201, f"user not created: {res}"
    yield u
    api.delete_account(u["email"], u["password"])


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed and "driver" in item.funcargs:
        drv = item.funcargs["driver"]
        folder = config.REPORT_DIR / "screenshots"
        folder.mkdir(parents=True, exist_ok=True)
        drv.save_screenshot(str(folder / f"{item.name}.png"))
        rep.extras = getattr(rep, "extras", []) + [pytest_html.extras.png(drv.get_screenshot_as_base64())]
