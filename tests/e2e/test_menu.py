import re

from playwright.sync_api import Page, expect

def test_has_title(page: Page):
  expect(page).to_have_title(re.compile("holistiplan"))
