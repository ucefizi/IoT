# IoT

To test the project, you need Python 3 installed along withe the Django packages
Run "$ python manage.py makemigrations" to generate migrations,
 "$ python manage.py migrate" to generate the DataBase file (SQLite 3)
and "$ python manage.py createsuperuser" to create an admin for the administration site.
Fill the DB with data to test the platform fully


##NB:
In case "makemigrations" doesn't detect any changes, run "$ python manage.py makemigrations receive" tp create migrations for the receive app