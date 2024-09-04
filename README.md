# APIsCourseraBuilding
Main Steps
Create an environment:

Windows:

python -m venv env
Environment activate:

Windows:

.\env\Scripts\activate
Install Django:

Windows:

pip install django
Verify Django Version:

Windows:

python -m django version
Install Django Rest Framework:

Windows:

pip install djangorestframework
Start Project:

django-admin startproject <name> .
Create APP:

Windows:

python -m django startapp <name>
OR

Windows:

python manage.py startapp <name>
Run Server:

Windows:

python manage.py runserver
Migrations:

python manage.py migrate
Create Super User

python manage.py createsuperuser
Overview
In this project, your APIs need to make it possible for your end-users to perform certain tasks and your reviewer will be looking for the following functionalities.

The admin can assign users to the manager group

You can access the manager group with an admin token

The admin can add menu items

The admin can add categories

Managers can log in

Managers can update the item of the day

Managers can assign users to the delivery crew

Managers can assign orders to the delivery crew

The delivery crew can access orders assigned to them

The delivery crew can update an order as delivered

Customers can register

Customers can log in using their username and password and get access tokens

Customers can browse all categories

Customers can browse all the menu items at once

Customers can browse menu items by category

Customers can paginate menu items

Customers can sort menu items by price

Customers can add menu items to the cart

Customers can access previously added items in the cart

Customers can place orders

Customers can browse their own orders

Prepare the virtual environment and install all dependencies using the following commands.

cd LittleLemon

pipenv shell

pipenv install

python manage.py makemigrations

python manage.py migrate

python manage.py runserver

Then log into the Django admin panel and create superuser and user groups and randomly assign them into these groups, the same way you did in your own project. Examples of Good Feedback less The focus of your feedback should be on the functionality of the APIs.

Follow the prompts and look for the expected output. If you notice any errors in the functionality of any of the elements of the APIs, you will have the opportunity to provide guidance to your peers on how they might fix the error.

An example of good feedback would be:

“On the whole, the APIs performed as expected; however, customers couldn’t log in using their username and password and get access tokens. I would suggest reviewing the code you have written to ensure that the Djoser package was installed and configured correctly. You could revisit the video, Introduction to Djoser library for better authentication in Module 3, lesson 2.
