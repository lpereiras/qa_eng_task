from playwright.sync_api import Page

class MenuPage: 

  def __init__(self, page:Page):
    self.page = page
    self.signup_link = page.get_by_role("link", name="Sign Up")
    self.signin_link = page.get_by_role("link", name="Sign In")
    self.home_link = page.get_by_role("link", name="Home")

  
