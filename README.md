October 23, 2024                  
##
![image](https://github.com/user-attachments/assets/c8782068-f3e1-4d4e-a4b2-6284b20ea582)

#### Welcome to TASKerise ...
##
Don't just prioritise, TASKerise:  https://taskerise-1ff1367ffa28.herokuapp.com/ 

## Table of contents
1. [UX Design](#ux-design)
2. [Agile Development](#agile-development)
3. [Deployment](#deployment)
4. [Features to Implement](#features-to-implement)
5. [Future Features](#future-features)
6. [Testing](#testing)
7. [Technologies](#technologies)
8. [Resources and References](#resources-and-references)
9. [Credits and Acknowledgements](#credits-and-acknowledgements)

##
## UX Design
Simple design created with Balsamiq to achieve Minumum Viable Product.  Future design will include icons for deleting and editing tasks, the ability to create subtasks and a pomodoro timer linked to your tasks.  Design incorporates responsive usability for all devices.
![image](https://github.com/user-attachments/assets/52747f73-8afb-4482-978a-5186ee0248fc)
- Desktop Design

![image](https://github.com/user-attachments/assets/a1d63185-670b-4606-ba57-2e021ad51d7b)
- Mobile Device Design

Taskerise will enable a user who has logged in to keep a catalogue of their current to do list.  They can quickly input a new task in the input field and press the <Add <Add Task>Task> button.  This new task will then appear in the list along with any other tasks they have still to do.  Additional details can be added (eg due date and a description) by clicking on the task which now works as a link to the edit task page.  Below are images of the Tasks page and edit task page taken from the website

![image](https://github.com/user-attachments/assets/4e03237c-cb29-4b09-8470-691fcd87cc8e)

## 

![image](https://github.com/user-attachments/assets/d3b17af0-a69c-4210-85d2-57f54e3044eb)


##
## Agile Development
The following Kaban board created in GitHub shows that after issues (user stories) were created they were added to the board in the To Do section.  From there they were moved to the In Progress so that work could begin implementing the code for that feature or issue.  Once completed the task was added to the Done area.  However it became apparent that some of the features could not be implemented for this update and so they have been added to the [Future Features](#future-features) section 
![image](https://github.com/user-attachments/assets/b4452532-3161-4dd4-b60d-5075f9c173d3)

User stories were created like this example below:  Further User Stories can be found in detail under the Issues Heading
![image](https://github.com/user-attachments/assets/5da92563-ac4f-4cd4-a5e3-c3088c5adbc4)

Labels were created to assign Low, Medium and High Priorities so that High priority tasks were given the preference
![image](https://github.com/user-attachments/assets/259c3e59-4400-4ca3-a34b-13d703d05bb0)


##  
## Deployment
To enable the full stack website to make use of PostGreSQL for users to create and edit their own tasks Heroku's cloud based platform was utilised
- Hidden files such as the database link and SECRET_KEY were added to the Config Variables section as the env.py file with this secret information could not be accessed.
![image](https://github.com/user-attachments/assets/423f8a66-2e59-479d-a26f-8df6d1ad19de)
- Heroku was added to ALLOWED_HOSTS
- Followed by connecting and deploying to a URL link
![image](https://github.com/user-attachments/assets/d1c51315-d004-415c-a6df-d98a7e18132e)
##
## Features to Implement
Also along with ensuring the program has uniform functionality and design it requires better CRUD functionality.  One example is on the edit task page.  A user who clicks to go back to the Task List page will lose any changes made.  Rather they should be asked if they would like to save or discard the changes.
##
## Future Features
As highlighted in the KABAN board I would like to add additional functionality such as adding a pomodoro timer, short cut keys, alternate motivational quotes and create subtasks

![image](https://github.com/user-attachments/assets/7b39b9dd-278e-4ba1-8fe2-76b7eb6cd0ea)
##
## Testing
### Automated tests
Automated tests were created for adding and editing tasks which were successful.

Further automated tests were created to evaluate authorisation checking.  The outcome was that an unauthorised user could hack someone's tasks deleting and editing them.  Additional code subsequently fixed this bug and the tests were successful.

The filenames are test_forms.py and test_views.py

### Code validation
HTML code was validated by inputing the code into https://validator.w3.org/

![image](https://github.com/user-attachments/assets/4f81de9e-ecef-4f3e-9003-1884a33f6a5a)

Python code was tested for PEP8 compliance using https://pep8ci.herokuapp.com/

![image](https://github.com/user-attachments/assets/87dd9024-743d-4041-9d21-2c94709745ca)

This made it easy to clean up the code as shown here:

![image](https://github.com/user-attachments/assets/05f50490-ea41-498b-962a-fd172e9cf9e1)

##
## Technologies
The following technologies were employed in the creation of TASKerise:
- HTML
- CSS
- Python
- Django
- Bootstrap 5 
- PostgreSQL
- GitHub
- Heroku
- Gitpod
##
## Resources and References
- Code Institute Full Stack Bootcamp Course
  - I think therefore I blog
  - SME sessions
- Djangoproject.com documentation
##
## Credits and Acknowledgements
### Code Institute
A big thank you to everyone at the Code Institute without whom I would not have dared to dream of the possibility of becoming a full-stack programmer.
Particular thanks to Alexander, Kevin, Martin and David for their enthusiasm and encouragement when all seemed too much :)
### Fellow Code Instituters
A massive shout out to my fellow members of the Berkshire Bootcamp.  You're all amazing and well done.  Thank you for your support and enthusiasm.

**More to come?**

Oh yes! 
---

`Happy taskerising!!`
