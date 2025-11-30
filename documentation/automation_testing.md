# DjangoCon(DJNGC): Automated Test Cases

## Disclaimer

Make sure you have initialized the application by following the execution steps at: `https://github.com/ocrfin/qa_homework/.`<br>
You may face some trouble while running all tests or debugging with `PWDEBUG=1` option, that will probably came from `node` container. Log output error example:
```bash
node        | Proxy error: socket hang up
django      |  * Restarting with watchdog (inotify)
node        | <e> [webpack-dev-server] [HPM] Error occurred while proxying request localhost:3000/ to http://django:8000/ [ECONNRESET] (https://nodejs.org/api/errors.html#errors_common_system_errors)
```
>In this case, rerun the tests with `pytest --lf` to see their execution. 

### TC-001: Sign Up successfully
  Given a user wants to Sign up for our system  
  When they fill in the required fields with valid credentials  
  Then click at `Sign Up >>` button  
  Then the application should redirect user to `localhost:3000/accounts/confirm-email/`

### TC-002: Sign In successfully
  Given user have valid credentials and wants to `Sign In`  
  When they fill in the required fields with valid credentials  
  Then click at `Sign In` button  
  Then the application should show `Successfully signed in as someone@holistiplan.com.` message

### TC-003: Redeem and claim a reward
  Given a user with valid credentials wants to claim a reward  
  When they have enough points to redeem it  
  Then click `Redeem this Reward` button  
  Then click `Claim my rewards` button  
  Then the application should shows `You successfully claimed the following rewards: INCREDIBLE_REWARD` message

### TC-004: Add bonus points with different options
  Given a user wants to add bonus points  
  When clicking `+5` or `+15` option  
  Then the application should add the respective points to `Ponts Remaining` counter  

### TC-005: Forfeit all points
  Given a user wants to reset their bonus points  
  When clicking `forfeit all points` option  
  Then the application should reset the points  
  Then `forfeit all points` option should not be visible
