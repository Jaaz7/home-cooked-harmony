# Home Cooked Harmony
**A django-based blog where you can share your favourite recipes and engage with the community.**
<br><br>
<img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/0bb6b13d-add8-459c-8ccc-7185cc8186d7" width=90% height=90%>
<br>
**[Visit the live project here.](https://home-cooked-harmony-33e620becec5.herokuapp.com/)**

---
# Table of Contents
- ### [User Experience (UX)](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#user-experience-ux-1)
  - [Project Goals](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#project-goals)
  - [Agile Methodology](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#agile-methodology)
  - [Target Audience](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#target-audience)
  - [Visitor](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#visitor)
  - [Registered User](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#registered-user)
- ### [Design](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#design-1)
  - [Colors](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#colors)
  - [Images and Patterns](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#images-and-patterns)
  - [Entity-Relationship Diagram (ERD)](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#entity-relationship-diagram-erd)
  - [Typography](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#typography)
  - [Wireframes](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#wireframes)
  - [Database Scheme](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#database-scheme)
- ### [Security Features](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#security-features-1)
- ### [Features](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#features-1)
  - [Existing Features](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#existing-features)
  - [Features Left to Implement](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#features-left-to-implement)
- ### [Technologies Used](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#technologies-used-1)
- ### [Deployment](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#deployment-1)
  - [Local Cloning](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#local-cloning)
  - [Forking The Github Repository](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#forking-the-github-repository)
  - [Elephant SQL Database](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#elephant-sql-database)
    [Cloudinary](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#cloudinary)
  - [Deploying To Heroku](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#deploying-to-heroku)
- ### [Testing](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#testing-1)
- ### [References](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#references-1)
  - [Docs](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#docs)
  - [Content](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#content)
  - [Acknowledgements](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#acknowledgements)

---
## User Experience (UX)
### Engaging and Intuitive Interface:
Home Cooked Harmony offers a good user experience with a user-friendly interface.

### Personalized Recipe Discovery:
Users can search by number of servings, by preparation time or do a free search.

### Community Interaction:
Users can share their own recipes and comment culinary tips, enriching the overall blogging experience.

### Visual Appeal:
Users are encouraged to upload visually appealing images. When adding a post, users are prompted with clear instructions pased as "criteria" for uploading an organized post, this includes where to put the ingredients and measurements. Users have a rich text editor to customize their own formatting. If the website has many posts and comments, users will find it easy to navigate with organized pagination buttons. This ensures a visually informative browsing experience.

### Multi-Device Accessibility:
Optimized for all devices, the website ensures a smooth experience, whether users are planning their meals on a desktop or browsing recipes on a mobile device.

  - ### Project Goals
    The aim of my recipe blog project is to craft an engaging and user-friendly online space where gastronomy enthusiasts can discover and share          their experiences. Highlighting the diverse and rich world of cooking
    through visually appealing recipe displays and comprehensive, easy instructions. The project is designed to inspire users to create 
    their culinary experiences.

  - ### Agile Methodology
    Agile methodology facilitated the prioritization and organization of tasks. It guided the writing of User Stories and the effective use of            Project Boards on Github.
    - Project Board is set to public.
    - Project Board was utilized to track User Stories in the "Todo", "In Progress" and "Done" columns.
    - Labels were added to indicate importance, such as "Must do".
    - <details><summary>User Stories' Issues (click to expand)</summary>
      <br>
      User Story: View for authenticated users
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/00b62259-e24f-4893-8a7a-40acae0b49f8" width=100% height=100%>
      User Story: Post Submission
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/0d1b4f8c-ff1a-40fb-a3c7-8e0b6799c809" width=100% height=100%>
      User Story: user comments view
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/1b321380-a4bf-4280-a0c3-de1bd63e0ba7" width=100% height=100%>
      User Story: Create view for user that aren't logged in
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/57d81cc3-9ec4-4a48-8a0f-a00bfa4d5f43" width=100% height=100%>
      User Story: login and logout validation
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/a92c8250-0d48-4a68-85bf-d524772ed91f" width=100% height=100%>
      </details>
    - <details><summary>Project Board (click to expand)</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/fbc2ebed-9566-4ded-a2ba-b5268563969e" width=100% height=100%>
      </details>

  - ### Target Audience
    - Culinary beginners who want to easily find quick recipes.
    - Food enthusiasts eager to explore a diverse world of recipes.
    - Home cooks looking for an intuitive platform to find and share recipes.
    - Visitors who want a quick search to get a recipe done.
    - Smartphone users desiring the ability to access recipes on-the-go.
    - Couples and families wanting to discover new meal ideas for home dining.
    - Community-minded individuals keen on sharing and commenting their favorite recipes and tips.
    - Health-conscious eaters searching for nutritious meal options.
    
  - ### Visitor
    - Intuitive navigation.
    - View recipes in homepage, also in detailed version.
    - Search button for quick find.
    - View comments.
    - Clear specifications for registration, with detailed error messages if any encountered.

  - ### Registered User
    - All visitor points above.
    - Smooth but strict signup allowing to a secure and personalized user account.
    - Easy login page with clear error messages if any encountered.
    - Access to posting recipes.
    - Acess to posting comments.
    - Ability to like posts.
    - Ability to edit their own posts.

---
## Design
  - ### Colors
    <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/0f8e360e-f737-47e6-857c-016e3f914813" width="100%" height="100%">
  - ### Images and Patterns
    <details><summary>Click here to expand</summary>
    <br>Favicon<br><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/6e1751a7-8955-46e3-abe1-53bb38fcb04d" width="10%" height="10%"><br><br>
    Homepage background<br><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/c69b5ead-661a-41e7-978d-44e2419d2f2a" width="30%" height="30%"><br><br>
    Post image placeholder<br><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/49ca73cc-6544-4cab-b6c4-1f8ee345c47e" width="30%" height="30%"><br><br>
    Login page background<br><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/56777ace-4eea-41e6-8b07-d52d543a6ee6" width="30%" height="30%"><br><br>
    Register page background<br><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/8ebeae7c-bcb6-4d6c-9f9b-239b3fe5995e" width="30%" height="30%"></details>
  - ### Entity-Relationship Diagram (ERD)
    Field type nomenclature is that of SQL.
    The "Likes" table is a field from the Post table, however since it's a many-to-many field,
    creating a separate table in the ERD allows for better visibility. It's also viewed as a separate table in Elephant SQL.<br><br>
    <details><summary>Click here to expand</summary><img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/1e5f9656-5558-4c41-8a61-523d59903ae2" width="60%" height="60%"></details>
  - ### Typography
    - Post title font: PlayFair Display.
    - Post description font: Open Sans.
  - ### Wireframes
  - ### Database Scheme
    Models
    - AllAuth User Model<br>
      Django Allauth, the User model is the default user model provided by the Django authentication system.
      The User entity has a one-to-many relationship with the Post identity.<br><br>
    - Post Model<br>
      A model created for the purpose of storing post information in an online database.<br><br>
    - Comment Model<br>
      A model created for the purpose of storing comment information in an online database.

---
## Security Features
  - User Authentication

---
## Features
  - ### Existing Features
  - ### Features Left to Implement

---
## Technologies Used
  - 

---
## Deployment
  - ### Local Cloning
  - ### Forking the Github Repository
  - ### Elephant SQL Database
  - ### Cloudinary
  - ### Deploying to Heroku

---
## Testing

---
## References
  - ### Docs
    - 
  - ### Content
    - All code and content were written by Jaaziel do Vale.
    - Orange chef hat favicon image [source](https://icons8.com/icon/LZnCmNzYfzAk/chef-hat).
    - Rest of images were powered by DALL-E [Bing Chat](https://www.bing.com/search?showconv=1&q=bing%20AI&sf=codex3p&form=MA13FV), an Artificial Intelligence (AI).
  - ### Acknowledgements