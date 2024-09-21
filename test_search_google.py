import pytest
from selene import browser, be, have

def test_search(browser_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('User-oriented Web UI browser tests in Python'))
    #browser.close()


