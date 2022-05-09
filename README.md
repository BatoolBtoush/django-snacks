# **Lab: Intro to Django**

## **Feature Tasks and Requirements**
- Create web site in Django with 2 pages
- home page
- about page
- create views/urls/templates as needed for home and about pages
- use ancestor template to contain navigation elements

<br>

## **Implementation Notes**

Typical Steps to Start Django Project:


1. create poetry project (django-snacks)


2. cd into the poetry project into (django-snacks)


3. activate the poetry shell, using this command:
    ```
    poetry shell
    ```


4. install Django, by running this command: 
    ```
    poetry add django
    ```

5. create django project by running this command:
    ```
    django-admin startproject snacks_project
    ```


6. cd into the django project (snacks_project)


7. open vs code inside the django project (snacks_project)


8. This command will be run in two cases:
    ```
    python manage.py migrate
    ```

	- when we first create a new project --> this will migrate some things to the data base, and create a data base for you

	- when we create a new model, or a set of new modesl, or when we change somethings in an existant model. Just to reflect the new added things on the data base



9. create an admin (a superuser) of the project
	```
    python manage.py createsuperuser
	```
    

10. run the server, via this command:
	```
    python manage.py runserver
    ```


11. Create an application by running this command:
	```
    python manage.py startapp (snacks)
    ```

	inside (snacks) i will also create a file, called: *-urls.py*
	

12. after creating (snacks):
	go to *-settings.py*in (django-snacks) and add the app (snacks) in the installed apps as a string



13. now create our first model inside (snacks) in the file *-model.py*.

	you can see in the file, theres an import for models from django.db
	this tells me that the models (classes) i'm about to create must inherit from this module
	after creating a class and having inherit from(models.Model) --> this will be a table inside our db



14. after creating the app and a model, follow these steps:
    - makemigrations ---> prepare the changes that would happen to the db
	```
    python manage.py makemigrations
    ```
	- now we actually applied the new changes (new model or table) on the db
	```
    python manage.py migrate
    ```
		


15. run the server again, via this command:
	```
    python manage.py runserver
    ```
	if the newly added changes don't appear, make sure you do the next step (16)


 
16. create a folder called (templates) inside the parent django project(django-snacks)



17. go to *-settings.py* in (django-snacks) and add to the TEMPLATES dictionary, the directory of the templates, as such:
    >'DIRS': [ BASE_DIR / 'templates'],


18. create html files in (templates) folder:
    - base.html
    - about.html


19. create views, by going to *-views.py* in (snacks) directory, and importing --> from django.views.generic import TemplateView
and writing classes to view html files, and give the pages names


20. then go to *-urls.py* in (snacks), to import and write out this:
    ```
    from .views import HomePageView
    urlpatterns = [
        path('', HomePageView.as_view(), name='home'),
       ]
    ```


21. i need to create a url for the view in order to render it, this is done by going to* -urls.py* in (django-snacks), to import and write out this:
    ```
    from django.urls import include
       path('', include('snacks.urls')),
    ```


