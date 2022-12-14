# [Django Project NewsPaper](http://127.0.0.1:8000/posts/)
## [Skillfactory](https://skillfactory.ru) FPW homework

## Content  
[1. Description](README.md#Description)  
[2. Case to solve](README.md#Case-to-solve)  
[3. Data info](README.md#Data-info)  
[5. Result](README.md#Result)    
[6. Conclusions](README.md#Conclusions) 

### Description
Five models with connections created and some requests applied using Django Shell.

Django server runs with templates, views, filters and tags. 
Getting accustomed to some built-in classes and libraries.
/posts/ pages with posts are added.

Filtration and pagination at posts list, edit, update and delete post are realised.

Identification, authentication and authorization are applied.

Signals, commands, logging, schedule.

Sending e-mails.

Synchronous and asynchronous task execution. Redis & Celery.
Sending e-mails by schedule.

Caching.

Custom commands for command line.

Admin panel customization.


:arrow_up: [to content](README.md#Content)


### Case to solve    
- Create relational database and work with it through Django Shell.
- Make views of the whole model elements in tab and of the every element as well with ListView and DetailView generics. Apply filters and tags.
- Create 'censor' filter.
- html-code to work at templates with views and forms.
- GET and POST parameters at HTTP-requests.
- DeleteView, UpdateView, CreateView generics.
- ModelForm, SignupForm.
- LoginRequiredMixin, PermissionRequiredMixin. Customization.
<p> </p>

- Two different ways to register and log in: full and via e-mail/social account.
- Add users to different groups via admin and registration. Exclusive permissions via admin and user upgrade.
- Check user permissions at views and templates.
<p> </p>

- Registration with confirmation.
- Sending e-mails by signals, by schedule.
- Dynamic permissions.
- Allauth library to sign in and log in.
<p> </p>

- Asynchronous task to send email after event.
- Raise the task and send email by schedule without main process interruption.
- Different scenarios of caching.
<p> </p>

- Custom console command via class Command.
- Custom admin panel models views with fields to display, filters, search and additional actions.


**Practice to**     
- describe models,
- create database,
- input data to database,
- fill connections between tables,
- receive data from connected tables,
- create views with generics,
- work with templates,
- routing,
- create own filters and tags,
- combine filtration and pagination on one page,
- add forms to edit and update objects, delete objects.
<p> </p>

- add different registration views and apply extra functionality at them.
- close add/change/delete views from users without permissions.
- open navigation in templates for users with permissions only.
- work with permissions at admin panel.
<p> </p>

- add subscribe/unsubscribe with e-mail confirmation.
- filter events and subscribers.
- add jobs, postponed and periodic jobs.
- close, redirect irrelevant urls at views, templates and navigation.
<p> </p>

- organize task queue on Redis server.
- cope with task queue by Celery.
- cash temporary the whole view and parts of templates. 
- cash object between savings. 
<p> </p>

- console command to show posts names by selected category.
- admin panel model display: model fields and properties at the table, filters by category and other m2m, m2o fields, search by related fields.
- action to add or diminish rating of post or comment with following author rating update.


:arrow_up: [to content](README.md#Content)


### Data info
No specific data required.
  

:arrow_up: [to content](README.md#Content)


### Result  
All input to Django Shell at [HomeWork_D2.txt](HomeWork_D2.txt) 

[News Portal](http://127.0.0.1:8000/posts/) updated, new pages added.

[Admin panel](http://127.0.0.1:8000/admin/) updated.


:arrow_up: [to content](README.md#Content)


### Conclusions  
Django is a powerful instrument to compose browser apps with well done helpful documentation. You should spend time to get accustomed but it is worth.

:arrow_up: [to content](README.md#Content)



Star ????????????????????????????????? my project if you like it or think it is useful
