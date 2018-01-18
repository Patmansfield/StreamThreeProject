# Django app - Stream Three Project


## News Revolution - Overview

### Application description:

My stream Three Project is a Technology News web application utilising the python based Django framework.   

### Purpose:

The purpose of the web application is to provide a fictitious news web site which provides current news topics, engaging forums, interesting blogs and 
a online store to purchase subscriptions and News Revolution merchandise.

### Construction:
 
 The site consists of a landing page whereby you have the carousel providing dynamic viewing of current topics.  Scrolling down
 you can find three introductory articles which once a successful registration has been completed via the registration page
 you can navigate to the full article which has the Disqus comment function to raise or continue on with any comments.  
 
 The Blog component allows the site administrator / editor to convey a current view of hot topics which viewers can add comments 
 via the Disqus function.
 
 The Forum component allows the viewer to become more engaged with topics as they can add threads with or without a poll 
 or add a new post to a current thread.  
 
 A subscription is gain upon successfully registering from which further purchases can be made via the Magazines or Products
 application.  
 
 Finally there is a Contact Us page to assist anyone who wants to make contact with the News Revolution team.
 
 ### Technologies:
 
 Django is the python based foundation framework that this application is built on.  The application has various other technologies 
 included to increase the design and functionality.  
 - **Bootstrap** 
    - Used to implement clean and responsive forms and functions to the application content.
 - **Disqus**
    - A Javascript based community platform giving viewers the function to add comments to articles or topics.
 - **Stripe**
    - An online payment handling application used as a part of the login / subscription component of my web application.
 - **PayPal**
    - Another online payment handling application implemented to handle on product and magazine payments.
 - **JQuery**
    - A javascript library used in both the carousel component as well as the scrollTop function that reduces the size
    of the carousel upon scrolling away from the top of the page.
 - **Prostgres**
    - The SQL database that I used to store vital information.  Using a externally hosted database via Heroku meant a more
    secure application as the database information isn't stored with the application code.
 - **Flatpages**
    - A simple inbuilt Django function that allowed me to display simple or 'flat' html page such as my Contact Us page that
    can be easily setup and edited via the admin interface.
    
 ### Getting up and going:
 
 1. First step is to clone the project from GitHub - <pre> git clone https://github.com/Patmansfield/StreamThreeProject.git
 2. Once you have your virtual environment up and running the carry out the required packages installation - <pre> pip install -r requirements.txt
 3. From the terminal initiate the local server - <pre> python manage.py runserver
 4. To view the application navigate in the browser to - <pre> localhost:8000
    
 ### Testing:
 
 The testing component of the web application included the testing suite included in the Django framework.  I utilised the 
 test case for the account app from the we_are_social app and I also added a url test to cover navigation.  I also included a test case in the
 blog app to check the use of the model as well as the url.  When carrying out these tests I had to comment out the OS.environ
 variable that directed the application to use the Postgres database so that the tests would use the local database as I had
 difficulties getting the test to launch when using the Postgres database.  
 
 I was not able to construct a test to test my javascript code, I think more due to the fact that the code is more a function
 as oppose to a process that produces a result.  I did test that the function worked on various screen sizes and I also discovered
 the function wasn't really required on smaller screens in the mobile display this is why I added a media property to the classes.
 
 I also test the responsiveness of the site by testing on the Google Chrome Developer Tool to replicate various screen sizes as well
 I checked responsiveness and functionality on other browsers such as Safari and Firefox.  
 
 ### Deployment:
  
 I carried out the deployment by utilising the online hosting Platform Heroku.  After committing the code to the GitHub repository I then
 connected it to the Heroku app. It can be viewed at the following hyperlink (www.google.ie).
 
 
    
   