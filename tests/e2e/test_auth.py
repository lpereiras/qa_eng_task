import re
import uuid

from pages.page_auth import AuthPage
from pages.page_menu import MenuPage
from playwright.sync_api import Page, expect

def test_signup_with_valid_credentials(page: Page):
  random_email = f"testqa_{uuid.uuid4()}@holistiplan.com.br"
  
  expect(page).to_have_title(re.compile("holistiplan"))

  MenuPage(page).signup_link.click()
  expect(page).to_have_url(re.compile("http://localhost:3000/accounts/signup/"))

  expect(AuthPage(page).user_email).to_be_visible()
  AuthPage(page).user_email.fill(random_email)

  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password.fill("test_pwd12345*")
  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password_confirmation.fill("test_pwd12345*")

  expect(AuthPage(page).signup_button).to_be_enabled()
  AuthPage(page).signup_button.click()

  expect(page).to_have_url(re.compile("http://localhost:3000/accounts/confirm-email/"))
  expect(page.get_by_text(f"Confirmation email sent to {random_email}")).to_be_visible()

def test_sign_in_with_valid_credentials(page: Page):
  expect(page).to_have_title(re.compile("holistiplan"))

  MenuPage(page).signin_link.click()
  expect(page).to_have_url(re.compile("http://localhost:3000/accounts/login/"))

  expect(AuthPage(page).user_email).to_be_visible()
  AuthPage(page).user_email.fill("someone@holistiplan.com")
  expect(AuthPage(page).user_password).to_be_visible()
  AuthPage(page).user_password.fill("bfx!wkp3zve3WUX*guq")

  AuthPage(page).remember_me_checkbox.click()
  expect(AuthPage(page).remember_me_checkbox).to_be_checked()

  expect(AuthPage(page).signin_button).to_be_enabled()
  AuthPage(page).signin_button.click()

  expect(page.get_by_text("Successfully signed in as someone@holistiplan.com.")).to_be_visible()
  expect(page).to_have_url(re.compile("http://localhost:3000/users/1/"))








  # Sign In
  # page.get_by_role("textbox", name="Email*")
  # page.get_by_role("textbox", name="Password*")
  # get_by_role("link", name="Forgot your password?") opt.1
  # get_by_role("link", name="Forgot Password?") opt.2
  # get_by_role("button", name="Sign In")
