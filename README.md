# Project Manager

## Setup

- Clone the repo
- Execute `cd project_manager`
- Install [virtualenv](https://gist.github.com/frfahim/73c0fad6350332cef7a653bcd762f08d)
- Execute `virtualenv env`
- Activate virtual environment using `source env/bin/activate`
- Install required packages using `pip install -r requirement.txt`
- Make migrations `python manage.py makemigrations`
- Migrate the db changes `python manage.py migrate`
- Run the server `python manage.py runserver`

## Using the project management application

### Create Admin account
Stop the runserver using `cntl+c` and Run `python manage.py createsuperuser` to create admin account in django framework
 - Give email id `admin@xyz.com`
 - Password: `admin123`
 - Confirm again the same password
 - Run the server again `python manage.py runserver`

Navigate to http://localhost:8000/admin/ and Login using the admin account

### Create other users
Click on Users in admin Home page to create new user
 - Enter username and password
 - Click save
 
### Create Project
Click on Project in admin Home page to create new project
 - Enter name, description, start and end date
 - Click Save
 
### Create Task
Click on Task in admin Home page to create new task
 - Enter name, description
 - Select the project from the dropdown
 - Select the assignee from the dropdown 
 - Click Save
 
### Access the Projects and tasks
- Navigate to http://localhost:8000/projects/ to list the created projects
- Click on particular project name to see the deatails of the project
- In Project details view click on particular task name to see the deatails of the task
