import pytest

from playwright.sync_api import sync_playwright

base_url = "http://localhost:3000"

@pytest.fixture(scope='session')
def browser():
  with sync_playwright() as b:
    browser = b.firefox.launch(headless=True)
    yield browser
    browser.close()

@pytest.fixture
def page(browser):
  page = browser.new_page()
  page.set_viewport_size({ "width": 1920 , "height": 1080 })
  page.goto(base_url)
  yield page
  page.close()