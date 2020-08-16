# Throttle
Requirements :
LANGUAGE: Python 3.6.5 ,
FRAMEWORK : Django Latest Version
DATABASE : sqlite3

Steps to Execute Project:
1) Install VirtualEnv : pip install virtalenv
2) Create VirtualEnv : virtualenv venv
3) Install requirements : Navigate to~~~~ requirements file path and execute the following command.
                pip install -r requirements.txt          

Project Details :
1) Created 2 custom management commands ,one is to create Superadmin user with 
credentials (username :admin ,password: 'admin'). Execute the following commands to create superuser.
        - python manage.py makemigrations
        - python manage.py migrate
        - python manage.py superuser
    After executing the above 3 commands a database will be created with superuser to access the django
    administration.
2) Another custom management command is used to create the dummyusers into the created models. Execute
the following command to create 5 dummy users.
        - python manage.py dummyusers
3) Run the following command to run server.
                python manage.py runserver
4) Login with the Admin credentials and enter "http://127.0.0.1:8000/api/all_users/" to display the 
get user information as specified in the json file.
            api url : {local host}/api/all_users/
      