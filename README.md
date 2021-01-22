# My Study Plan
https://mystudyplan.netlify.app/

Back-end REST API created with Django and Django RFW to handle user information including login, course information and saved courses.

Made with Python, Django, Django Rest Framework, Vagrant, JSONField and deployed on AWS

## Setup:
1) install Vagrant, Virtualbox, Python3 and Pip, complete any associated install.
https://www.virtualbox.org/
https://www.vagrantup.com/docs/installation/
https://www.python.org/downloads/


2) Run `vagrant up` then `vagrant ssh` in the project directory on the terminal


3) Enter `cd /vagrant` and then activate the Python virtual environment by entering `source ~/env/bin/activate` on the terminal


4) After the virtual env is up, install all associated packages by running `pip install -r requirements.txt`

5) Run server locally by entering `python3 manage.py runserver 0.0.0.0:8000
***Note***
You will need to generate a secret key to run this locally. 
Please place `secret_key` in /course_planner/course_planner_secrets/secrets_file to run locally

## End points:
`/profile/`: register profile (post), view profile for authenticated user (get)

`/profile/{id}`: update profile (put), delete profile (delete)

`/login/`: to obtain auth token (get)

`/course-items/`: to view all courses associated with authenticated profile (get), create new course items (post)

`/course-items/{id}`: update course item (put), delete course item (delete)

`/course-items/?semester_query={query}`: get course items associated with the logged in user and the associated semester id (get)

`/semesters/`: create new semesters for the associated user (post), view semesters for authenticated user (get)

`/semesters/{id}`: update semester info (put), delete semester (delete)


Front end located at: https://github.com/billzyc/studyplan-client
