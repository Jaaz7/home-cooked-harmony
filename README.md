# Home Cooked Harmony
**A full-stack, django-based blog application designed for sharing your favourite recipes and engage with the community.**
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
  - [Cloudinary](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#cloudinary)
  - [Deploying To Heroku](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#deploying-to-heroku)
- ### [Testing](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#testing-1)
- ### [References](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#references-1)
  - [Documentation](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#docs)
  - [Inspirational Resources]()
  - [Tools]()
  - [Content](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#content)
  - [Acknowledgements](https://github.com/Jaaz7/home-cooked-harmony/tree/main?tab=readme-ov-file#acknowledgements)

---
## User Experience (UX)
### Engaging and Intuitive Interface:
Home Cooked Harmony offers a good user experience with a user-friendly interface.

### Personalized Recipe Discovery:
Users can filter by number of servings, preparation time or through a free-form search.

### Community Interaction:
Users can share their own recipes and comment culinary tips, enriching the overall blogging experience.

### Visual Appeal:
Users are encouraged to upload visually appealing images. When adding a post, users are prompted with clear instructions passed as "criteria" for uploading an organized post, this includes where to put the ingredients and measurements. Users have a rich text editor to customize their own formatting. If the website has many posts and comments, users will find it easy to navigate with organized pagination buttons. This ensures a visually informative browsing experience.

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
    - Smooth but strict signup allowing to a secure user account.

  - ### Registered User
    - All visitor points above.
    - Easy login page with clear error messages if any encountered.
    - Access to posting recipes.
    - Access to posting comments.
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
    - <details><summary>Homepage Desktop</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/29aba06a-511e-4de2-a5ac-ce699b55ce27" width="80%" height="80%">></details>
    - <details><summary>Post Details Desktop</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ef678282-5b98-4093-a5a0-b21fd72cae83" width="80%" height="80%">></details>
    - <details><summary>Homepage Mobile</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/a7ee9b8b-e2cd-4b99-b803-42547f851fc2" width="50%" height="50%">></details>
    - <details><summary>Login Page Desktop</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/eb473803-db20-49b6-b7f7-94faa840f8a6" width="80%" height="80%">></details>
    - <details><summary>Login Page Mobile</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/46f7bbd3-55a9-414e-80c0-46ff55a2b2a3" width="50%" height="50%">></details>
    - <details><summary>Register Page Desktop</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ee1ba273-9d39-4e46-8cb6-2e877fc13eb1" width="80%" height="80%">></details>
    - <details><summary>Register Page Mobile</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/b8a96964-2687-469e-9d89-0786d9510715" width="50%" height="50%">></details>
  - ### Database Scheme
    Models
    - AllAuth User Model<br>
      Django AllAuth, the User model is the default user model provided by the Django authentication system.<br><br>
    - Post Model<br>
      A model created for the purpose of storing post information in an online database.<br><br>
    - Comment Model<br>
      A model created for the purpose of storing comment information in an online database.

---
## Security Features
  - User Authentication
    Django AllAuth is a popular authentication and authorization library for Django, which provides a set of features for managing user                   authentication, registration, login and logout.<br><br>
  - Login Decorator
    I use the login_required decorator for the following views: add_post, logout_view, delete_post, delete_comment, like_post and edit_post.
    This ensures backend protection and enhances user experience: if the user tries to access any of these views previously mentioned but they're not logged in, they are redirected to the login page.<br><br>
  - CSRF Protection
    CSRF stands for Cross-Site Request Forgery. It's a type of attack where a malicious website can make requests to a different website where the               user is authenticated. Django has a built-in protection mechanism that ensures any submitted form request comes from the authenticated user, not an imposter, and this protection is actively enforced.

---
## Features
  - User authentication.
  - Rich text editor, bringing more formatting freedom to the user.
  - Free-search option, as well as filtering by number of servings and preparation time.
  - Registered users can add posts.
  - Registered users can like and dislike a post.
  - Registered users can comment under a post.
  - Pagination is included in views/templates where objects are dynamic, this includes posts (homepage&search), and comment sections.
  - Registered users can edit and delete their posts.
  - Registered users can delete their comments.
  - ### Existing Features
    - <details><summary>Homepage&Navigation Bar</summary>
      <br>For visitors<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/76f7d05a-6ed2-48e1-b1bf-8ad9e921bdcc" width="80%" height="80%"><br>
      <br>For Registered users the navigation bar changes<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/1e3c9999-01b9-416c-bd48-6a3b671e2487" width="80%" height="80%"></details>
    - <details><summary>About Section</summary>
      <br>The about section only appears in the home page<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/18552a51-fecc-4e6d-86d3-df89fed4e5a1" width="50%" height="50%"></details>
    - <details><summary>Search Section</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/ba643e35-387d-4e88-b54c-290c9351127a" width="50%" height="50%"></details>
    - <details><summary>Footer&Socials</summary>
      <br>It features a copyright message and social media buttons<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/8e908dfc-7885-4b42-91b4-3b7f1f5da7a8" width="100%" height="100%"></details>
    - <details><summary>Login Page</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/4ea84cbb-3dbb-4a40-80c4-01b41c03de4b" width="80%" height="80%"></details>
    - <details><summary>Register Page</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/3c6695c0-55ad-4076-8cae-b72cd47ec13b" width="80%" height="80%"></details>
    - <details><summary>Detailed Post Page</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/b7443551-733b-4275-8585-3f8b08adb266" width="80%" height="80%"></details>
    - <details><summary>Edit, Delete and Like Buttons in Detailed Post Page</summary>
      <br>What the post owner sees<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/f5cd4ff8-c1e4-4fae-ba9e-9fa08fd84de1" width="30%" height="30%">
      <br>What non-authors see<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/a82bafa8-4519-46cd-8030-6ae3baac587f" width="30%" height="30%"></details>
    - <details><summary>Comment Section</summary>
      <br>For visitors<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/3840c4c9-397d-47c8-8a88-31a499fdae28" width="70%" height="70%">
      <br>For authenticated users<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/01ee79c2-47bd-4888-9c3d-d6949749a1a5" width="70%" height="70%"></details>
    - <details><summary>Edit and Delete buttons and Like Counter in the Homepage</summary>
      <br>What post authors see<br><br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/4bdf34a2-792d-4ec1-b90d-b9676c45bed0" width="70%" height="70%">
      <br>Like counter display is availabe for all users and visitors in the homepage<br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/79ce2131-8cf6-4716-8190-8a6f54fbb3ad" width="20%" height="20%"></details>
    - <details><summary>Add Post Page</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/194b6cc2-6358-403f-ae4d-74dd7a9dd4fc" width="80%" height="80%"></details>
    - <details><summary>Edit Post Page</summary>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/413ad1ee-911c-4e3c-b2bc-76c994fe849e" width="80%" height="80%"></details>
    - <details><summary>Modals</summary>
      <br>There are 4 modals in total, two for defensive programming (deleting posts&comments and logout), and two informative ones. This is one example, they are explored in the TESTS.md file<br><br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/dbadef70-ead0-480b-9632-c37de4d2634b" width="40%" height="40%"></details>
    - <details><summary>Alerts</summary>
      <br>There is a multitude of messages, one for every CRUD action and some informative ones for user experience enhancement. This is one example, they are explored in the TESTS.md file<br><br>
      <img src="https://github.com/Jaaz7/home-cooked-harmony/assets/130407877/4734028e-e442-4e0a-9fac-fb55b7d439ca" width="100%" height="100%"></details>
  - ### Features Left to Implement
    - Profile picture for the user.
    - Way to recover the password.
    - User dashboard.
    - Account deletion option.
    - Custom server error pages.

---
## Technologies Used
  - ### Languages
    - [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - [CSS3](https://en.wikipedia.org/wiki/CSS)
    - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
  - ### Databases
    - [ElephantSQL](https://www.elephantsql.com/) - PostgreSQL.
    - [Cloudinary](https://cloudinary.com/) - Cloud-based service for image storage.
  - ### Frameworks
    - [Bootstrap](https://getbootstrap.com/) - Provides a collection of HTML, CSS, and JavaScript-based design.
    - [jQuery](https://jquery.com/) - For efficient JavaScript manipulation.
  - ### Libraries
    - [Fontawesome](https://fontawesome.com/) - Provides vector icon sets for the blog.
    - [TinyMCE](https://www.tiny.cloud/) - A WYSIWYG (What You See Is What You Get) rich text editor.
  - ### Programs
    - [VS Code](https://code.visualstudio.com/) - To write code.
    - [GitHub](https://github.com/) - For repository hosting.
    - [Django Template Language (DTL)](https://docs.djangoproject.com/en/4.2/ref/templates/language/) - Template engine that works very similar to Jinja2.
    - [Heroku](https://www.heroku.com/) - Used as the cloud-based platform to deploy the website.
    - [Google Fonts](https://fonts.google.com/) - Import main font the website.
    - [WireframeSketcher](https://wireframesketcher.com/) - Used to create wireframes and schemes.
    - [Am I Responsive](https://ui.dev/amiresponsive) - Show the website on a range of devices.
    - [Git](https://git-scm.com/) - Version control.
    - [JSHint](https://jshint.com/) - Used to validate JavaScript.
    - [W3C Markup Validation Service](https://validator.w3.org/) - Used to validate HTML.
    - [CSS Validation Service](https://jigsaw.w3.org/css-validator/) - Used to validate CSS.
    - [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used to validate Python.
    - [Coolors](https://coolors.co/efecca-a9cbb7-f7ff58-ff934f-5e565a) - Color Scheme.

---
## Deployment
  - ### Local Cloning
    <details><summary>Click here to expand</summary>
    ‎1. Log in to GitHub and locate GitHub Repository home-cooked-harmony.
    <br><br>
    ‎2. Click on the green code button, select clone with HTTPS, SSH or GitHub CLI and copy the link shown.
    <br><br>
    ‎3. Open the terminal in your IDE and change the current working directory to the location you want to use for the cloned directory.
    <br><br>
    ‎4. Change the current working directory to the location where you want the cloned directory to be created.
    <br><br>
    ‎5. Type <pre><code>git clone</code></pre> and then paste The URL copied in step 2.
    <br><br>
    ‎6. Set up a virtual environment navigating into your project with <pre><code>cd path/to/project</code></pre> and running the command <pre><code>python3 -m venv venv</code></pre> replace the second "venv" with any name you want. Activate your virtual environment with:  (in Linux OS) <pre><code>source venv/bin/activate</pre></code>
    <br>
    ‎7. Install dependencies with <pre><code>pip3 install -r requirements.txt</pre></code>Your local clone has been created.</details>
  - ### Forking the Github Repository
    <details><summary>Click here to expand</summary>
    ‎1. Log in to GitHub and locate GitHub Repository home-cooked-harmony.
    <br><br>
    ‎2. At the top of the Repository, under the main navigation, Click "Fork" button. Your fork has been created. You can locate it in your repositories section.</details>
  - ### Elephant SQL Database
    <details><summary>Click here to expand</summary>
    ‎1. Create account and click Create New Instance to start a new database.
    <br><br>
    ‎2. Provide a name.
    <br><br>
    ‎3. Select the Tiny Turtle plan.
    <br><br>
    ‎4. Select the Region and Data Center closest to you.
    <br><br>
    ‎5. Once created you can access the new database configuration to view the database URL and API key.</details>
  - ### Cloudinary
    <details><summary>Click here to expand</summary>
    ‎1. Create account and you'll find your API key in your Cloudinary dashboard 
    at Cloudinary Dashboard.
    <br><br>
    ‎2. Copy the API environment variable but take out the start "CLOUDINARY_URL".</details>
  - ### Deploying to Heroku
    <details><summary>Click here to expand</summary>
    ‎1. Log in to Heroku or create a new account.
    <br><br>
    ‎2. On the main page click "New" and select "Create new app".
    <br><br>
    ‎3. Choose your unique app name and select your region.
    <br><br>
    ‎4. Click "Create app".
    <br><br>
    ‎5. On the next page find "settings" and locate "Config Vars".
    <br><br>
    ‎6. Add necessary config vars which ideally are in an env.py file and being ignored to github by a .gitignore file.<br>Click "Reveal Config Vars" and add the 'SECRET_KEY' which can be any key you create.<br>I'm using two API keys, ElephantSQL and Cloudinary.<br>Therefore 'DATABASE_URL' and 'CLOUDINARY_URL' are also added.
    <br><br>
    ‎7. If choosing another database applies, comment out the default Django database configuration and make migrations with <pre><code>python3 manage.py makemigrations</pre></code> and <pre><code>python3 manage.py migrate</pre></code>
    <br>
    ‎8. Add Heroku to allowed hosts in settings.py. <pre><code>ALLOWED_HOSTS=[".herokuapp.com"]</pre></code>
    <br>
    ‎9. Add and freeze dependencies to requirements.txt file with command <pre><code>pip3 freeze --local > requirements.txt</pre></code>careful to only do this with a virtual environment activated in a local IDE, to potentially avoid pushing hundreds of unwanted and unused dependencies.
    <br><br>
    ‎10. Add a Procfile by running <pre><code>echo web: gunicorn myproject.wsgi > Procfile</pre></code>where "myproject" is the name of your Django project.
    <br><br>
    ‎11. Select GitHub as deployment method and search for your repository and link them together.
    <br><br>
    ‎12. Make sure debug is set to false in settings.py before deploying. <pre><code>DEBUG = False</pre></code>
    <br>
    ‎13. Scroll down and select "Enable Automatic Deploys", Click to deploy.
    <br><br>
    ‎14. Your website is deployed and linked to your GitHub account. This means that running <pre><code>git push</pre></code>from your IDE will reflect in the newest version of your app in production.</details>

---
## Testing
  ### Refer to the [TESTS.md](https://github.com/Jaaz7/home-cooked-harmony/blob/main/TESTS.md) file for a detailed testing documentation.
---
## References
  - ### Documentation
    - [Python 3.11.7 documentation](https://docs.python.org/3.11) - Official Python documentation, used for language syntax and library reference.
    - [Django 5.0.1 documentation](https://django.readthedocs.io/en/stable/contents.html) - Comprehensive guide for Django framework used in the          project.
    - [PostgreSQL 5.4 documentation](https://www.postgresql.org/docs/15/sql-commands.html) - This documentation was important for performing commands 
    in the database, eg. retrieving field types from tables.
    - [Bootstrap Template](https://github.com/StartBootstrap/startbootstrap-blog-post) - A front-end template that values responsiveness.
  - ### Inspirational Resources
    - [Django tutorials from Codemy](https://www.youtube.com/@Codemycom/featured) - A video series by John Elder, providing practical Django         development skills.
    - Code Institute's "I Think Therefore I Blog" walkthrough project - Provided a foundational understanding of blog development in Django.
  - ### Tools
    - [Brave search engine](https://search.brave.com/) - Primary search engine used for research and troubleshooting.
  - ### Content
    - All code and content were written by Jaaziel do Vale.
    - Orange chef hat favicon image [source](https://icons8.com/icon/LZnCmNzYfzAk/chef-hat).
    - Rest of images were powered by DALL-E [Bing Chat](https://www.bing.com/search?showconv=1&q=bing%20AI&sf=codex3p&form=MA13FV), an Artificial Intelligence (AI).
  - ### Acknowledgements
    - Mentor Mitko Bachvarov for providing mentorship and feedback.
    - Slack community and tutors for help and observations.
    - Stephanie Herz for helping me populate the blog, posting recipes that have her own flair. (The pictures are original content too!)