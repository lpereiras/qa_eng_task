from conftest import base_url

from pages.page_auth import AuthPage
from pages.page_menu import MenuPage
from pages.page_rewards import RewardPage

from playwright.sync_api import Page, expect

# TC-003: Redeem and claim a reward
def test_redeem_and_claim_reward(page: Page):
  select_reward = page.locator(f'[data-reward-id="6"]')

  expect(page).to_have_title("holistiplan")

  MenuPage(page).signin_link.click()
  expect(page).to_have_url(f"{base_url}/accounts/login/")

  AuthPage(page).login("someone@holistiplan.com", "bfx!wkp3zve3WUX*guq")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  RewardPage(page).add_fifteen.click()

  expect(RewardPage(page).claim_reward).to_be_disabled()
  select_reward.click()

  page.wait_for_timeout(2000)

  expect(RewardPage(page).claim_reward).to_be_enabled()
  RewardPage(page).claim_reward.click()

  expect(page.get_by_text("You successfully claimed the following rewards: T-Shirt +2")).to_be_visible()

# TC-004: Add bonus points with different options
def test_add_bonus_points_5(page: Page):
  ponts_remaining = page.get_by_text("15", exact=True)

  expect(page).to_have_title("holistiplan")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  expect(RewardPage(page).add_five).to_be_enabled()
  RewardPage(page).add_five.click()

  expect(ponts_remaining).to_be_visible()

# TC-004: Add bonus points with different options
def test_add_bonus_points_15(page: Page):
  ponts_remaining = page.get_by_text("25", exact=True)

  expect(page).to_have_title("holistiplan")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  expect(RewardPage(page).add_fifteen).to_be_enabled()
  RewardPage(page).add_fifteen.click()

  expect(ponts_remaining).to_be_visible()  

# TC-005: Forfeit all points
def test_forfeit_all_points(page: Page):
  expect(page).to_have_title("holistiplan")

  MenuPage(page).signin_link.click()
  expect(page).to_have_url(f"{base_url}/accounts/login/")

  AuthPage(page).login("someone@holistiplan.com", "bfx!wkp3zve3WUX*guq")
  expect(MenuPage(page).home_link).to_be_visible()
  MenuPage(page).home_link.click()

  expect(RewardPage(page).forfeit_points).to_be_visible()
  RewardPage(page).forfeit_points.click()

  expect(RewardPage(page).forfeit_points).not_to_be_visible()