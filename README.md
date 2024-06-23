# `Moment`
The application is available for viewing [here]().

![Moment Responsive Image]()
## Introduction
## Business/Social Goals
## UX Goals
## User Stories

| Id | User Story | Label | User Story Testing |
| ----- | ----- | ----- | ----- |
## Wireframes
![Moment Wireframe]()
## Strategy
## Target Audience
## Key Information Deliverables
## Features
## Structure 
## Models
Below is a simple ERD for `moment`'s models.

![Moment ERD]()
## Views & Templates
## Scope of Application
## Aesthetics
## Technologies
1. HTML5/ Django Templates - Used for structuring and content.
2. CSS3 - Used for adding styles to the content for legibility and aesthetic appeal.
3. Vanilla Javascript - For adding basic interactivity and dynamically setting URLs.
4. FontAwesome/Bootstrap icons - used for icons.
4. FontAwesome/Bootstrap icons - used for icons.
5. Emojipedia - used for emojis.
6. Firefox Developer Tools - used for debugging the website during production.
7. Lighthouse - An extension I used for testing the performance, accessibility, best practices and SEO of my site (result shown under debugging below).
8. GitHub - For code storage, version control and deployment.
9. Git - For commiting through the terminal and pushing to GitHub for storage.
8. GitHub - For code storage, version control and deployment.
9. Git - For commiting through the terminal and pushing to GitHub for storage.
10. VSC - The IDE I developed the project in.
11. Balsamiq - For a clear understanding of the structure I wanted my application to follow. The project has since deviated slightly from the design for improved user experience.
12. Color Contrast Accessibility Validator - check legibility of my text on different backgrounds for better accessibility.
13. W3C Markup Validation Service - to validate my HTML for potential errors.
14. W3C CSS Validation Service - to validate my CSS code for potential errors.
15. JSHint - for checking and validating my JS code. 
16. Pep8 - for Python code validation and best practices formatting.
17. Freeformatter CSS Beautify - to ensure I formatted my CSS correctly.
18. Beautifier.io - to beautify my JS. 
19. BeFunky Collage Maker - to create the responsive image.

## Testing & Debugging
This section outlines procedures for manual testing. For automated testing, please see all files `test*.py`.

- ## Manual Testing
| Feature | Expected Outcome | Testing Procedure | Result | Remark |
|---|---|---|---|---|

- ## Automated Testing
## Accessibility & Performance
### Lighthouse
### Colour Accessibility Validator
### HTML Validation
### CSS Validation
### JSHint Validation
# Deployment
The application is deployed on Heroku through Git Hub and is available for viewing in the link at the top of this README.md document. To deploy a Heroku project, please refer to the guide below.

## Foreword
There are some general requirements when it comes to setting up your application and its files: 
- Your dependencies must be placed in the requirements.txt file.
- You must strictly adhere to the correct folder structure expected by Django's settings.
- In Django's settings.py file, setting Debug = True in development will display a detailed errors page if the application comes across an error hindering template rendering. It will also allow the collection of static files (stylesheets, images, and javascript files automatically). Setting Debug = False will display standard error pages under the same conditions and will not update any changes to static files.

In Heroku, this is configured under `Config Vars`, as `COLLECT_STATIC`, with the value of either:
  - `0` for blocking automatic collection
  - `1` for enabling automatic collection.

_Note: Do not commit to GitHub with Debug = True. Always set Debug = False before committing to avoid exposing personal details._

You will need two-factor verification set up to enable log in.

### Step 1: Create an App on Heroku
Log onto your Heroku dashboard using your username and password, and confirm the access code in the two-factor verification app of your choosing.

Create a new Heroku app:
![New Heroku App]()

You will be asked to pick a name and region for your app before clicking `Create app` on the next page.
![New App Options]()

### Step 2: Connect to GitHub
Once you've created your app, go to the `Deploy` tab at the top.

Select the middle box with GitHub's logo to connect your Heroku app to a GitHub Repository.

If prompted, authorize Heroku to access your GitHub account.
At the bottom, enter the name of the repository you wish to deploy to, and click Connect.
![Connect GitHub to Heroku]()

### Step 3: Automatic Deploy (Optional)
Under `Automatic Deploys`, choose a branch from your GitHub repository that Heroku will watch for changes.

Enable automatic deploys by clicking `Enable Automatic Deploys`. With this, every push to the selected branch will automatically deploy a new version of your app.

### Step 4: Settings
When you create the app, you will need to add the `heroku/python` buildpack in the Settings tab. 

### Step 5: Deploy Your Masterpiece
If you've enabled automatic deploys, any push to the selected branch will automatically deploy your application.

If you prefer to deploy manually or want to deploy a branch without enabling automatic deploys, go to `Manual deploy`, select the branch, and click `Deploy Branch`.

### Step 6: Where is my Application?
Your application will have a similar look to the following Heroku URL configuration: (https://*.herokuapp.com) and can be found after clicking the `Open App` button on your dashboard in the top right corner.

![Open App]()

## Forking a GitHub Repository
To make changes to your repository without changing its original state, you can make a copy of it via `fork`. This ensures the original repository remains unchanged. 

Steps:
1. Click into the GitHub repository you want to fork.
2. Click `Fork` in the top right-hand side of the top bar, and this should take you to a page titled `Create a new fork`.
3. You can now work in this copy of your repository without making changes to the original.

## Cloning a GitHub Repository
Cloning a repository essentially means downloading a copy of your repository that can be worked on locally. This method allows for version control and backup of code.

Steps:
1. Click on the GitHub repository you want to clone.
2. Click on the `Code` button.
3. Copy the link in the dropdown.
4. Open a terminal within your VSC (or whatever IDE you choose to use).
5. In the terminal type 'git clone' and paste the URL.
6. Press Enter - you now have a cloned version of your GitHub repository.

# Credits
# Acknowledgements