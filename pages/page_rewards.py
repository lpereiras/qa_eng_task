from playwright.sync_api import Page

class RewardPage:

  def __init__(self, page:Page):
    self.page = page
    self.first_reward = page.get_by_text("Redeem this Reward").first
    self.forfeit_points = page.get_by_role("link", name="forfeit all points")
    self.add_five = page.get_by_role("link", name="+5")
    self.add_fifteen = page.get_by_role("link", name="+15")
    self.claim_reward = page.get_by_role("button", name="Claim my rewards")

