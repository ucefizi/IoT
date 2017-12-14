# IoT

To test the project, you need Python 3 installed along withe the Django packages and PostgreSQL
You can find installation instructions for PostgreSQL here:
## Windows:
http://www.postgresqltutorial.com/install-postgresql/
## Linux:
https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04
Run "$ python manage.py makemigrations" to generate migrations,
"$ python manage.py migrate" to generate the DataBase tables
and "$ python manage.py createsuperuser" to create an admin for the administration site.
Fill the DB with data to test the platform fully


##NB:
In case "makemigrations" doesn't detect any changes, run "$ python manage.py makemigrations receive" tp create migrations for the receive app
