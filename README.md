# awwards 
## Author  
  
>[Victor-Kigen](https://github.com/kigensky)  
  
# Description  
This is an application that looks works like the awwards web application
  
##  Live Link  
 Click [View Site](kigen-awwards.herokuapp.com/)  to visit the site
 
 ## Screenshot
 
 <img src="https://raw.githubusercontent.com/kigensky/awwards/main/awwards/static/awwards/Screenshot from 2021-06-01 19-40-16.png" width="900px" height="440px">

## User Story  
  
* View posted projects and their details
* Post a project to be rated/reviewed
* Rate/ review other users' projects
* Search for projects 
* View projects overall score
* View my profile page 
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/kigensky/awwards.git
```
##### Navigate into the folder and install requirements  
 ```bash 
cd awwards pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations awwards 
python manage.py makemigrations users
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 3.2.2](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [vickigen@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/kigensky/pic-galery/blob/main/LICENCE)  
* Copyright (c) 2021 **Victor Kigen**