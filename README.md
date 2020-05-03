# API for Course users
Visit browsable API at http://ec2-18-188-30-63.us-east-2.compute.amazonaws.com/api/

Back-end REST API created with Django and Django RFW to handle user information including login, course information and saved courses.

Made with Python, Django, Django Rest Framework, Vagrant, JSONField and deployed on AWS

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
