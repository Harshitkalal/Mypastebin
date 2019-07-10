# Mypastebin
Cloud based pastebin

![](https://i.imgur.com/Le0ewHm.png)
Mypatsebin is a cloud  text file stoarge which allows you to add,delete, and update data from anywhere in the world.

### Features
It allows you to:
 - Create new Paste 

  ![](https://i.imgur.com/Le0ewHm.png)

 - All Paste

   ![](https://i.imgur.com/oCsdlEG.png)

 - Detail Paste

   ![](https://i.imgur.com/T1i8OYG.png)


### Installing Django 

Either install from packages by typing these commands in your terminal
```
sudo apt-get update
sudo apt-get install python-django
```
You can confirm whether its installed or not by typing 
```
django-admin --version
```

Other way is installing by using pip 
```
sudo apt-get update
```
Install pip if you dont have by 
```
sudo apt-get install python-pip
```
Then install django by 
```
sudo pip install django
```

### Running the code 
Just go into the code directory and type 
```
python manage.py runserver
```
"My Paste" app will start on 127.0.0.1:8000 (Local Address).
 
### Applying Migrations on the Project 
Migrations are Django’s way of propagating changes you make to your models (adding a field, deleting a model, etc.) into your database schema. They’re designed to be mostly automatic, but you’ll need to know when to make migrations, when to run them, and the common problems you might run into.
Now suppose you want to change mypaste model and have your's you can simply change the code as you require and then run these commands
```
python manage.py makemigrations
python manage.py migrate 
python manage.py runserver
```
You can use *showmigration*  to list projects migration.
### Have Fun ! 

   
