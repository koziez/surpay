# [Surpay][docs]

Surpay is a polling app designed with Django and Mysql.


## Preparing MySQL database (assuming already installed):

1. `$ mysql -u root -p`   [enter root password]
2. `mysql> CREATE database djangodb;`
3. `mysql> CREATE USER 'djangouser'@'localhost' IDENTIFIED BY 'password';`
3. `mysql> GRANT ALL PRIVILEGES ON djangodb.* TO 'djangouser'@'localhost';`
5. `mysql> FLUSH PRIVILEGES;`
6. `mysql> EXIT;`

## Installing the application (option 1):

1. `$ git clone https://github.com/koziez/surpay`
2. `$ cd surpay`
3. `$ sudo pip3 install -r requirements.txt`
4. `$ django-admin.py startproject surpay`
5. `$ cp -r src/polls/ surpay/`
6. `$ cp -r src/static/ surpay/`
7. `$ cp src/surpay/* surpay/surpay/`
8. `$ cd surpay/surpay/`
9. `$ python3 manage.py makemigrations polls`
10. `$ python3 manage.py migrate`
11. `$ python3 manage.py createsuperuser`   [setup superuser account]
11. `$ python3 manage.py runserver`
(alternative) `$ python3 manage.py runserver {your-local-ip}:8000`    # share with others computers on local network

## Installing the application (option 2):

A much simpler option is to download or copy the setup.sh file from the repo. Running this file `./setup.sh` will automate the process previously stated in option 1. Be sure to modify permission allowing the script to be executable `chmod u+x setup.sh`. This script has been tested on Ubuntu Server 16.04.

## Getting started:

Upon running the application, you will be greated with the complete/ page. This is because there are currently no polls entered into the database. To begin adding questions and answers, login to the admin section using the superuser account entered during setup. The app is designed to only allow one vote per question per session.

## Admin mode:

When signed in as admin, you will not be allowed to vote, but you will be able to browse all of the questions and see their current results, which have been visualized using pie charts.

## Notes:

If you want to change any of the database options (dbname, user, password) you must also change the settings in surpay/surpay/settings.py before applying migrations.

This version is only meant to be a demo and is not intended to be a production release.
