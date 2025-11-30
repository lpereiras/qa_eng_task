# DjangoCon(DJNGC): Bug Report

## Disclaimer

> To avoid repeat this step in every bug report, make sure the application is running at `http://localhost:3000/.`<br>
> You can check on how to initialize the application by following the execution steps at this repo: `https://github.com/ocrfin/qa_homework/.`<br>

### DJNGC_001: `Ponts Redeemed` & `Ponts remaining` counter not behaving as expected

**Description:**<br>
When trying to redeem one or more rewards, the application add 2 extra points for each selected reward.

1. Make sure to reset your points by click `forfeit all points`
2. Redeem one reward to update values (e.g. Tote Bag of Holding 2.75pts)
3. Notice the difference between what is expected (2.75pts), from what the application display to the final user (4.75pts/-4.75pts)

**QA Perspective:**<br>
Knowing that this is one of the most important product features, this defect has a high severity beacause it may result in our final user not being able to redeem all rewards that they should, causing a bad experience and a lack of trust in our product.

### DJNGC_002: Points Remaining shouldn't be negative

**Description:**<br>
If user doesn't have the required amount of points for some reward, the application display a negative amount when click`Redeem this Reward` option.

1. Make sure to reset your points by click `forfeit all points`
2. Redeem one reward to update values (e.g. Scroll of Infinite WiFi 3.75pts)
3. Notice that the `Ponts Remaining` counter will be updated to `-5.75`

**QA Perspective:**<br>
For this case, a negative amount of points doesn't have a real value to the final experience, and maybe can cause some missunderstanding about the rewards workflow. This information could be displayed in a popup telling how many points they should acquire before claim that reward.

### DJNGC_003: Typo error: `Ponts`

**Description:**<br>
The word Points were misswritten at application counters.

1. At the `Home Page`, notice that there's a typo error at `Ponts Redeemed` and `Ponts Remaining`

**QA Perspective:**<br>
While doesn't have a real system impact, it can decrease the confiability of our software by passing a image of unserious.

### DJNGC_004: `Add E-mail Address` doesn't register any data

**Description:**<br>
When trying to add another valid E-mail address to user profile, after fill the input and click `Add E-mail`, the application just reload the page without any visual feedback or action.

1. Click `Sign In` option and log in with valid credentials, e.g.:
   > email: someone@holistiplan.com  
   > password: bfx!wkp3zve3WUX*guq
2. Wait until you see the `Successfully signed in as someone@holistiplan.com.` message
3. Click `E-mail` button
4. Input a valid credential at Email* input
5. Click `Add E-mail` button

**QA Perspective:**<br>
While this defect doesn't directly affect the final experience, it can scale to a severe problem if we consider implement some feature about send confirmation to a secondary Email.

### DJNGC_005: `Forgot password?` option displayed twice at Sign In page

**Description:**<br>
When accessing the `Sign In` page there's two `Forgot your password?` option displayed to user.

1. Click `Sign In` option
2. Notice that application have two options for the same feature

**QA Perspective:**<br>
This defect have a low severity since both options work as expected, it's necessary to remove one of them for a better UI experience. I suggest the one close to `Sign In`, since it's the one who can cause some missclicks while trying to log In.

### DJNGC_006: `About` menu option throws user to an error

**Description:**<br>
When trying to access `About` page, the application leads the user to a page that doesn't exist

1. Access application `Home`
2. At the menu on top, click `About` option
3. Notice that the application will redirect the user to a `Page not found (404)` error

**QA Perspective:**<br>
Considering the content isn't ready to be in production, it should be a better approach to hide this menu option and deliver the feature when it's properly tested.
