System requirements: python version 3.9.9, django version 3.2.9

from "CS443 - Project 1" folder, open terminal and enter the following commands:
        cd mysite
        pip install django-crispy-forms
        pip install django-hitcount
        python manage.py makemigrations
        python manage.py migrate
        python manage.py runserver

*So long as the server is running you can navigate to view webpages*

to navigate to admin site enter url: localhost:8000/admin/
        admin username: admin
        admin password: user1234

to navigate to main site enter url: localhost:8000/login/
        user username: admin
        user password: user1234

to stop the server type "CTRL-C" in the terminal