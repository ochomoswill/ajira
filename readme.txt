Django Install

Set up a development structure:

$ mkdir uonProject
$ cd uonProject
$ virtualenv envProject or $ virtualenv -p /usr/bin/python3.5 envProject

$ source envProject/bin/activate

You should see (envProject) before your prompt, (envProject)$, indicating that your virtualenv is activated.

To deactivate the virtualenv:

$ deactivate

Then reactivate once you’re ready to start developing again.

With your virtualenv activated, install Django with Pip:

$ pip install django==1.8.1

You can check the version by running the following commands:

$ python
>>> import django
>>> django.get_version()
'1.8.1'
>>>

Project setup

Setup Django project

$ django-admin.py startproject ajira

This creates a new directory called “my_django18_project” with the basic Django directory and structures:

├── manage.py
└── my_django17_project
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

Version control

Before you start any developing, place your project under version control. First, add a .gitignore file within your “django18_project” directory, which prevent unnecessary files from being added to the git repository.

Add the following to the file:

env
*.DS_Store
*.pyc
__pycache__

Now initialize (or create) a new Git repo and add your changes to staging and then to the repo.

$ git init
$ git add -A
$ git commit -am "initial"
$ git commit -m "first commit"
$ git remote add origin https://github.com/ochomoswill/ajira.git
$ git push -u origin master



Start Project
===================================================
$ django-admin startproject aura_cms




Creating App
===================================================
$ python manage.py startapp ajiriwa
$ python manage.py startapp mwajiri


Connecting to MySQL_Db
===================================================
In CMD

pip install wheel
pip install pymysql


In settings.py

import pymysql
pymysql.install_as_MySQLdb()


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cms',
        'HOST': 'localhost',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '',
    }
}

#accessing db terminal

$ mysql -u root -p test_db

http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm

Creating Models
===================================================

Change your models (in models.py).

Include App('blog') in the settings.py

Run python manage.py makemigrations blog - to create migrations for those changes
Run python manage.py migrate - to apply those changes to the database.


Runserver
===================================================
$ python manage.py runserver


Creating an Admin User
===================================================

$ python manage.py createsuperuser

from .models import Post - add on admin.py
