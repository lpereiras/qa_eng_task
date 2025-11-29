from playwright.sync_api import Page

class AuthPage: 
  
  def __init__(self, page:Page):
    self.page = page
    self.user_email = page.get_by_role("textbox", name="Email*")
    self.user_password = page.get_by_role("textbox", name="Password*")
    self.user_password_confirmation = page.get_by_role("textbox", name="Password (again)*")
    self.signup_button = page.get_by_role("button", name="Sign Up")
    self.signin_button = page.get_by_role("button", name="Sign In")
    self.remember_me_checkbox = page.get_by_role("checkbox", name="Remember Me")

  def login(self, email: str, password: str):
    self.user_email.fill(email)
    self.user_password.fill(password)
    self.signin_button.click()