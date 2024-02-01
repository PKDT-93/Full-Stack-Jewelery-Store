# Full Stack Jewelery Store Application

**Instructions:** 
 
This project uses an SQLite database running on the django framework. 

# Quickstart guide :rocket:

## Install some dependencies

To run the project, Python must be installed on your system. Once it is installed, download the code/zip file and extract the `jewelryDatabase` folder. Once extracted, open your terminal and navigate to it's path. 

Once you have naviated to /jewelryDatabase, please do the following:

1. Type `python3 -m venv env` in terminal to prepare the python virtual environment.

2. Once you have created the virtual environment type `source env/bin/activate` in terminal to activate the virtual environment. On windows machines type `env\Scripts\activate`.

3. Once you are in the virutal environment type `python -m pip install Django` in terminal to install the Django framework. 

4. This project requires `django-bootstrap-v5` & `pymysql` in order to run, you may install any dependencies by typing `pip install (dependency name)`. To see all dependencies, please view the `requirements.txt` file.
   
4. To run the server type `python manage.py runserver`.

5. Navigate to http://127.0.0.1:8000/ in your web browser to access the server.

## Login Guide

1. In order to log into the application you may type `python manage.py createsuperuser` to create a manager account. Alternatively you may use `admin`/`123` as the username/password. This will show you the manager view.

2. To see the staff view, you may use `employee/cpsc471project` as the username/password to login. If logged in as a manager, you may navigate to the Employees tab in the navbar and click on the Add/Update Employee login button to add a new user. Click save and ensure that the "staff" is checked in the checkbox in the next page and then save again.

## Additional Information

- The templates folder contains all webpage loadouts. With customer, employee, home page, item/inventory/supplier, navbar and purchase pages in the root directory. Additional functions for each category will be located within subfolders. 

- To view the database you may use DB Browser for SQLite `https://sqlitebrowser.org`or install the SQLite Explorer extension for VSCode and open the `FinalProject.db` file in `/jewelryDatabase`. 
  
- All tables are contained as class objects in the `models.py` file along with their properties and attributes. 
  
- The `urls.py` file will contain all urls requests and patterns for the program and the `views.py` file contains all webpage scripting and raw SQL queries.


