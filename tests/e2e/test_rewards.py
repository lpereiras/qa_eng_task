import re

from pages.page_auth import AuthPage
from pages.page_menu import MenuPage
from pages.page_rewards import RewardPage
from playwright.sync_api import Page, expect

def test_redeem_and_claim_reward(page: Page):
  expect(page).to_have_title("holistiplan")

  MenuPage(page).signin_link.click()
  expect(page).to_have_url("http://localhost:3000/accounts/login/")

  AuthPage(page).login("someone@holistiplan.com", "bfx!wkp3zve3WUX*guq")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  RewardPage(page).first_reward.click()

def test_add_bonus_points(page: Page):
  expect(page).to_have_title("holistiplan")

  MenuPage(page).signin_link.click()
  expect(page).to_have_url("http://localhost:3000/accounts/login/")

  AuthPage(page).login("someone@holistiplan.com", "bfx!wkp3zve3WUX*guq")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  expect(page.get_by_role("link", name="+5")).to_be_visible()
  page.get_by_role("link", name="+5").click


def test_forfeit_all_points(page: Page):
  pass