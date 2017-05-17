# Django Install

Set up a development structure:

``` sh
$ mkdir uonProject
$ cd uonProject
$ virtualenv -p /usr/bin/python3.5 envProject
$ source envProject/bin/activate
```

You should see ` sh (envProject)` before your prompt, `sh (envProject)$ `, indicating that your virtualenv is activated.

To deactivate the virtualenv:

``` sh
$ deactivate
```

Then reactivate once you’re ready to start developing again.

With your virtualenv activated, install Django with Pip:

``` sh
$ pip install django==1.8.1
``` 

You can check the version by running the following commands:
``` sh
$ python
>>> import django
>>> django.get_version()
'1.8.1'
>>>
``` 

# Project setup

Setup Django project

``` sh
$ django-admin.py startproject ajira
```

Creating App
===================================================

``` sh
$ python manage.py startapp ajiriwa
$ python manage.py startapp mwajiri
```


Connecting to MySQL_Db
===================================================

``` sh
$ pip install wheel
$ pip install pymysql
``` 


In settings.py

``` python
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
```

accessing db terminal:

``` sh
$ mysql -u root -p test_db
``` 
http://g2pc1.bu.edu/~qzpeng/manual/MySQL%20Commands.htm


Creating Models
===================================================

Change your models (in models.py).

Include App('ajiriwa' and 'mwajiri') in the settings.py

Run `sh $ python manage.py makemigrations blog`- to create migrations for those changes
Run `sh $ python manage.py migrate` - to apply those changes to the database.


Runserver
===================================================

``` sh
$ python manage.py runserver
``` 


Creating an Admin User
===================================================
``` sh
$ python manage.py createsuperuser
```

`python from .models import Post` - add on admin.py
