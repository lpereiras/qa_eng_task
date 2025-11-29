# DjangoCon(DJNGC): Automated Test Cases

### TC-001: Sign Up successfully : check
  Given a user wants to Sign up for our system  
  When they fill in the required fields with valid credentials  
  Then click at `Sign Up >>` button  
  Then the application should redirect user to `localhost:3000/accounts/confirm-email/`

### TC-002: Sign In successfully : check
  Given user have valid credentials and wants to `Sign In`  
  When they fill in the required fields with valid credentials  
  Then click at `Sign In` button  
  Then the application should shows `Successfully signed in as someone@holistiplan.com.` message

### TC-003: Redeem and claim a reward : almost check
  Given a user with valid credentials wants to claim a reward  
  When they have enough points to redeem the desired one  
  Then click at `Redeem this Reward` button followed by clicking on `Claim my rewards`  
  Then the application should shows `You successfully claimed the following rewards: INCREDIBLE_REWARD` message


### TC-004: Add bonus points with different options
  Given a user with valid credentials wants to add more points  
  When clicking at `+5` or `+15` option  
  Then the application should add the respective points to `Ponts Remaining` counter  

### TC-005: Update `Name of User`

### TC-006: Forfeit all points 

  Menu
  get_by_role("link", name="Sign In")
  get_by_role("link", name="Sign Up")
  get_by_role("link", name="Home")

  Sign In
  page.get_by_role("textbox", name="Email*")
  page.get_by_role("textbox", name="Password*")
  get_by_role("link", name="Forgot your password?") opt.1
  get_by_role("link", name="Forgot Password?") opt.2
  get_by_role("button", name="Sign In")

  Sign Up
  get_by_role("textbox", name="Email*")
  get_by_role("textbox", name="Password*")
  get_by_role("textbox", name="Password (again)*")
  get_by_role("button", name="Sign Up »")

  Home
  page.get_by_role("button", name="Claim my rewards")
  page.get_by_test_id('data-reward-id="2"')
  page.get_by_role("link", name="+5") or get_by_role("link", name="+15")
  page.get_by_role("link", name="forfeit all points")
