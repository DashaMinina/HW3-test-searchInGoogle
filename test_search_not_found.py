import pytest
from selene import browser, be, have
def test_search_negative(browser_size, browser_open):
    browser.element('[name="q"]').should(be.blank).type('liugutgcgvlj').press_enter()
    browser.element('[id="search"]').should(have.text('По запросу liugutgcgvlj ничего не найдено.'))