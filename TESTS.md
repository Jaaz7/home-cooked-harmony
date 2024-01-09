## Extensive Manual Testing Document for Home Cooked Harmony<br>
Return to [README](README.md)

---
## Table of Contents
- ### [Responsiveness Testing]()
- ### [Code Validation]()
  - [HTML Validation]()
  - [CSS Validation]()
  - [JavaScript Validation]()
  - [Python Validation]()
- ### [Bugs]()
  - [Resolved Bugs]()
  - [Unresolved Bugs]()
- ### [Features Testing]()

---
## Responsiveness Testing
- <details><summary>Desktop PC</summary>
  <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/541a8fea-8af4-4595-bfcc-2de365b68b6c" width="80%" height="80%"></details>
- <details><summary>Tablet iPad Pro</summary>
  <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/247e34c4-69da-4bd9-8b4f-43cfa8fce8e4" width="50%" height="50%"></details>
- <details><summary>Mobile Phone Samsung Galaxy S8+</summary>
  <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/d4b1acee-869e-4f7e-a0da-759ae1e0f6e7" width="35%" height="35%"></details>
---
## Code Validation
- ### HTML Validation
  - <details><summary>Homepage</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ec290b1c-0990-440c-b555-dc3dcdfa2776" width="80%" height="80%"></details>
  - <details><summary>Post Details</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/50f65586-30e3-49f8-855f-c7e9a814eb99" width="80%" height="80%"></details>
  - <details><summary>Edit Post</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/3185316c-81a0-464b-b3f6-e944f68abffd" width="80%" height="80%"></details>
  - <details><summary>Add Post</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ee2408e1-f5e6-4ee9-b28a-3b2d55a0a851" width="80%" height="80%"></details>
  - <details><summary>Login</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/2f119d9e-2b1e-4de3-b4f7-c8dd7f59334c" width="80%" height="80%"></details>
  - <details><summary>Register</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ddf6cc87-513e-4d83-9517-587c3b82b756" width="80%" height="80%"></details>
  - <details><summary>Search Results</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/368d7564-4e3b-462f-a440-10d9279d9428" width="80%" height="80%"></details>
- ### CSS Validation
  - <details><summary>styles.css</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/6cc1da0e-4d4e-4e1b-8a54-0effc7774696" width="80%" height="80%"></details>
- ### JavaScript Validation
  - <details><summary>scripts.js</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/807d1edb-f879-48a6-aaf2-916b0e0382d0" width="80%" height="80%"></details>
- ### Python Validation
  - <details><summary>Admin.py</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/5f6a8441-4f04-40a7-8e56-d9eae173f7ad" width="80%" height="80%"></details>
  - <details><summary>Forms.py</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/078d15d3-b837-462b-a3d8-195ec36319e8" width="80%" height="80%"></details>
  - <details><summary>Models.py</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/b46e33de-9ff8-451c-a799-f4daf1b8d7ee" width="80%" height="80%"></details>
  - <details><summary>Settings.py</summary>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/d232301a-d82f-4583-bbf7-49e670f26537" width="80%" height="80%"></details>
  - <details><summary>Views.py</summary>
    <br>I couldn't fix the following flags<br>
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/fab37f1a-97e3-4a96-b859-52910094bccb" width="80%" height="80%"></details>

---
## Bugs
- ### Resolved Bugs
  - Solved a bug where I could see other people's delete buttons for comments.
  - Solved a bug where the pagination buttons wouldn't stay on the bottom of coments in post details, so I had to move it to a less desired spot.
  - Fixed an issue where the header would cover part of the page in mobile versions, this happened because I have a fixed header. Solved the issue by using javascript to dynamically get the pixels from the header and adding it to the main page, also when the navigation bar is toggled in a dropdown menu in lower screen sizes.
- ### Unresolved Bugs
  - When registering, the message "This password is too short. It must contain at least 8 characters." appears two times.
---
## Features Testing

| Page          | User Action   | Expected Result  | Notes            |
|---------------|---------------|------------------|------------------|
| Home Page     |               |                  |                  |
|               | Click on Page name | Redirect to Home Page | PASS        |
|               | Click on Register button | Redirect to Register page | PASS |
|               | Click on Login button | Redirect to Login page | PASS |
|               | Click on Post Details | Redirect to Post Details page | PASS |
|               | Click on pagination buttons | Redirect to Next or Previous Page Number| PASS |
|               | Click on search | Redirect to Search page | PASS |
|               | Click on social links in footer | Open new tab with the correct link | PASS |
|               | Click on search by servings | Redirect to Search page | PASS |
|               | Click on search by preptime | Redirect to Search page | PASS |
|                | No posts available | Show message saying no posts available | PASS |
|                | No preptime or servings available | Show message saying no posts available | PASS |
| Home Page (User Logged In)  |                 |          |  |
|               | After Login | Login Page cannot be accessed | PASS |
|               | Click on Add Recipe | Redirect to Add Post page | PASS |
|               | Click on Edit Post | Redirect to Edit Post page | PASS |
|               | After Login | Username is displayed in navigation bar | PASS |
|               | Click on Delete Post | Open Modal for post deletion | PASS |
| Login Page    |               |                  |                  |
|               | Click Login Button | Create account and redirects to Home page | PASS |
| Register Page     |               |                  |                  |
|               | Click Register User | Creates new account and redirects to login page | PASS |
|               | Tries password less than 8 characters | show error | PASS |
|               | Tries existing username | show error | PASS |
|               | Passwords don't match | show error | PASS |
|               | Forget to fill any field | show error | PASS |
|               | Click Sign In if you have an account | Redirect to Login page | PASS |
|               | Click Register User | Creates new account and redirects to login page with success message | PASS |
| Post Details Page  |                  |                  |                  |
|               | Click like button | show modal to register or login | PASS |
|               | Click on pagination comment buttons | Redirect to Next or Previous Page Number| PASS |
|               | clicks on ligon link in the comment section | Redirects to login page | PASS |
| Post Details (User Logged In)  |                  |                  |                  |
|               | Click on like button | likes post | PASS |
|               | Click on add comment | comment is added | PASS |
|               | If author click on edit post | Redirects to edit post page | PASS |
|               | Click to delete comment | show modal to deletes comment | PASS |
| Logout Page   |                  |                  |                  |
|               | Click on Log Out button | modal asks to confirm | PASS |
| Add Post Page |                  |                  |                  |
|               | click on add post without filling everything | modal informs about it | PASS |    
| Edit Post Page |                  |                  |                  |
|               | tries to edit a post which they're not the author | shows message and redirects to home page | PASS |  
| Login Page |                  |                  |                  |
|               | click register link | Redirects to register page | PASS |
|                | User correctly inputs information | login | PASS |
|                | User submits faulty username or password | show error | PASS |
|               | User tries to login but they're already logged in | show error | PASS |
| Search Page |                  |                  |                  |
|               | Click on pagination buttons | Redirect to Next or Previous Page Number| PASS |
|               | Click on search | Redirect to Search page | PASS |
|               | Click on search by servings | Redirect to Search page | PASS |
|               | Click on search by preptime | Redirect to Search page | PASS |
|                | No posts available | Show message saying no posts found | PASS |
|                | No preptime or servings available | Show message saying no posts available | PASS |



---
Return to [README](README.md)