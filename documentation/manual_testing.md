# DjangoCon(DJNGC): Bug Report

## Disclaimer

> To avoid repeat this step in every bug report, make sure that you're running the application in your local environemnt at `http://localhost:3000/.`<br>
> You can check on how to initialize the application by accessing this repo: `https://github.com/ocrfin/qa_homework/.`

### DJNGC_001: `Points Redeemed` & `Point remaining` counter not behaving as expected

**Description:**<br>
While trying to redeem one of the rewards, the application add or deduce 2 extra points depending on the case for each selected reward.

1. Make sure to reset your points by clicking on `forfeit all points`
2. Redeem one reward to update values (e.g. Tote Bag of Holding 2.75pts)
3. Notice the difference between what is expected, from what the application display to the final user

**Considerations:**<br>
Knowing that this is one of the most important features from the product, this defect has a high severity beacause it may result in our final user not being able to redeem all rewards that they should, causing a bad experience and a lack of trust in our product.

### DJNGC_002: Points Remaining shouldn't be negative

**Description:**<br>
The application allows the final users to click at the `Redeem this Reward` option, even if they don't have any points available

1. Make sure to reset your points by clicking on `forfeit all points`
2. Redeem one reward to update values (e.g. Scroll of Infinite WiFi 3.75pts)
3. Notice that the `Ponts Remaining` counter will be updated to `-5.75`

**Considerations:**<br>
For this case, a negative amount of points doesn't have a real value for the final experience, and maybe can cause some missunderstanding about the rewards workflow. (e.g. Some client thinking that they can redeem some rewards and earn points to cover it
later).

### DJNGC_003: Typo error at `Ponts`

**Description:**<br>
The word Points have a typographical error

1. At the `Home Page`, notice that the word Points were misswritten

**Considerations:**<br>
While doesn't have a real impact at the system, it can impact the confiability of our software by passing a image of suspicious
since this is a quick adjust to make

### DJNGC_004: `Add E-mail Address` doesn't register the info as expected

**Description:**<br>
When trying to add another E-mail address to user profile, after clicking on `Add E-mail` button, the application just reload the page without any visual feedback or action

1. Click on `Sign In` option and log in with valid credentials, e.g.:
   > email: someone@holistiplan.com  
   > password: bfx!wkp3zve3WUX*guq
2. Wait until you see the `Successfully signed in as someone@holistiplan.com.` message
3. Click on `E-mail` button

**Considerations:**<br>
While the defect doesn't directly affect the user final, if we consider implement some feature that send a confirmation about the rewards, this can scale to a more severe problem

### DJNGC_005: `Forgot password?` option displayed twice in Sign In page

**Description:**<br>
When accessing the `Sign In` page there's two `Forgot your password?` option displayed to the user

### DJNGC_006: About page aren't integrated with the expected content

**Description:**<br>
When trying to access the `About` menu option, the application doesn't display any information

1. Access system `Home`
2. At the menu on top, click in the `About` option
3. Notice that the application will redirect the user for a Page not found (404) error

**Considerations:**<br>
Considering that this specific content are not ready yet to be on production, it should be a better approach to hide this menu option,
and just deliver the feature when its properly ready
