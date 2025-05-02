Hej Världen

The Ultimate Django Course YouTube
Programming with Mosh
Mosh Hamedani

Python

- basics
- classes
- inheritance

Relational Databases

- tables
- columns
- rows
- relations

Django Fundamentals

- Free and open-source framework for building web apps with Python
- Includes:
  - Admin site
  - Object-relational mapper (ORM)
  - Authentication
  - Caching

Front-end - Client - web browser
Back-end - Server - data processing, validating business rules etc.

URL - Uniform Resource Locator - finds a resource on the internet (page, image, video, pdf)

the browser sends a request to the web server that hosts our web site
the web server takes the request, processes it, and sends a response back to the client

data exchange defined by protocol
HTTP - HyperText Transfer Protocol
defines how servers and clients can communicate

The server needs to decide how to package the response

1. generate page on server and return document in
   HTML - HyperText Markup Language - display web page

2. return the data needed and have the client generate the HTML page

Considered best practice - free up server to serve more clients

Tools for generating web page on the client:

- React
- Angular
- Vue

Tools for building backends on server:

- Django
- Asp.net Core (C#)
- Express (JS)

all endpoints represents the interface that clients use to talk to the server. The server provides an
API - Application Programming Interface
like buttons on a remote control

we will use Django to build API for online store
client applications can use this API to get or save the data
on the client side we can use React, Angular or plain JS which falls under front-end development which has nothing to do with Django

set up dev env
download/upgrade python to the latest version - python.org/downloads
python3 --version - to check version on Mac
pip3 install pipenv - dependecy management tool
install python extension in VS Code

cd to correct folder
mkdir _name_ - create folder
cd to folder
pip3 install pipenv
pip3 install django

pipenv shell

django-admin - to see available commands
django-admin startproject _name_
3 folders with same name

- top: created in terminal
- middle: for the project
- bottom: for the core of the application

NEW PROJECT:
django-admin startproject _name_ . - to use current directory to avoid extra folder/directory

**init**.py - defines directory as a package
asgi.py & wsgi.py - used for deployment
manage.py - wrapper around django-admin - going forward we use manage.py instead of django-admin so that settings for projects are taken into account
python3 manage.py runserver
optionally we can supply a portnumber (python3 manage.py runserver 9000)

NEW APP:
python3 manage.py startapp _name_ - to add new application

migrations folder - for generating database tables
admin module - define how the admin interface is going to look
apps module - configure the app
models module - define model classes to pull data from database and present to the user
tests module - for unit tests
views module - request handler (no template or HTML)

register in list of installed apps in settings.py

create a function in views.py
map view to a url so that when we get a request at that url; this function will be called

DEBUGGING IN VSCODE:
run code line by line to see exactly where something hasa gone wrong
click on play/bug icon on the left side
create a launch.json file so that vs code know how to run or debug the application
select python debugger > django in list
set breakpoint
step through
on left side inspect variable values
at each stage
no variables in watch window
add by clicking +
type x + enter
for instance
arrow over - jump over
arrow down - step into function

django-debug-toolbar
great tool especially for SQL

MODELS:
figure out what pieces of data we need to store
in a web store:
* products (title, description, price, inventory etc.)
* collection/category (title)
  + relationship between them
  + featured product relationship
(ID attribute is created automatically in Django)

* cart (created_at) - anonymous user
  + relationship with products or
* cartItem (quantity)

* customer (name, email)
* order (placed_at)
  + relationship customer
  + relatinship product or
* orderItem (quantity)

* tag (label)

organizing models in apps
a django project contains one or more apps
each app has their own data model

option 1: MONOLITH - single app called store with all entities
  (can be distributed and shared through pipenv install)
  problem: growing, encreased complexity, bloated with too many things

each app should do one thing and do it well

option 2: separate apps for
  Products - Product, Collection, Tag
  Customers - Customer
  Carts - Cart, CartItem
  Orders - Order, OrderItem
  problem: coupling, all apps depend on eachother, all apps have to be installed one by one, not self contained, new version of one app might cause breaking change in other app, are not useful without eachother

highly related features should be bundled together

option 3: middleground
  Tags - not specific to e-commerce application (Tag, TaggedItem)
  Store - (Product, Collection, Customer, Cart, CartItem, Order, OrderItem)
each app is self-contained, zero coupling, either or both can be used independently

CREATE APPS:
python manage.py startapp *name*

register in settings installed apps
create models for the apps
