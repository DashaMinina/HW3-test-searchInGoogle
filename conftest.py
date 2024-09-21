import pytest
from selene import browser, be, have


@pytest.fixture(scope="session")
def browser_size():
    browser.config.driver_name = "chrome"
    browser.config.window_height = 1000
    browser.config.window_width = 800


@pytest.fixture(scope="session")
def browser_open():
    browser.open('https://www.google.com')
    yield
    browser.close()