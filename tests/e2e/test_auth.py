import uuid

from conftest import base_url

from pages.page_auth import AuthPage
from pages.page_menu import MenuPage

from playwright.sync_api import Page, expect

# TC-001: Sign Up successfully
def test_sign_up_with_valid_credentials(page: Page):
  user_email = f"testqa_{uuid.uuid4()}@holistiplan.com.br"
  user_pwd = "test_pwd12345*"
  
  expect(page).to_have_title("holistiplan")

  MenuPage(page).signup_link.click()
  expect(page).to_have_url(f"{base_url}/accounts/signup/")

  expect(AuthPage(page).user_email).to_be_visible()
  AuthPage(page).user_email.fill(user_email)

  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password.fill(user_pwd)
  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password_confirmation.fill(user_pwd)

  expect(AuthPage(page).signup_button).to_be_enabled()
  AuthPage(page).signup_button.click()

  expect(page).to_have_url(f"{base_url}/accounts/confirm-email/")
  expect(page.get_by_text(f"Confirmation email sent to {user_email}")).to_be_visible()

# TC-002: Sign In successfully
def test_sign_in_with_valid_credentials(page: Page):
  expect(page).to_have_title("holistiplan")

  MenuPage(page).signin_link.click()
  expect(page).to_have_url(f"{base_url}/accounts/login/")

  expect(AuthPage(page).user_email).to_be_visible()
  AuthPage(page).user_email.fill("someone@holistiplan.com")
  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password.fill("bfx!wkp3zve3WUX*guq")

  AuthPage(page).remember_me_checkbox.click()
  expect(AuthPage(page).remember_me_checkbox).to_be_checked()

  expect(AuthPage(page).signin_button).to_be_enabled()
  AuthPage(page).signin_button.click()

  expect(page.get_by_text("Successfully signed in as someone@holistiplan.com.")).to_be_visible()
  expect(page).to_have_url(f"{base_url}/users/1/")
  
