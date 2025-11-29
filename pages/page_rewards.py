from playwright.sync_api import Page

class RewardPage:

  def __init__(self, page:Page):
    self.page = page
    self.first_reward = page.get_by_text("Redeem this Reward").first
    
    
