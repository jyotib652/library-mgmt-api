# library-mgmt-api

A REST API written in Django Rest Framework.



## Technologies used

- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org)
- [Swagger](https://swagger.io/)



## Functionalitis of the API

**Scenario**

There are two roles in the system;  `LIBRARIAN` and `MEMBER`

**As a User**

- I can signup either as `LIBRARIAN` and `MEMBER` using username and password
- I can login using username/password and get [JWT](https://jwt.io/introduction) access token

**As a Librarian**

- I can add, update, and remove Books from the system
- I can add, update, view, and remove Member from the system


**As a Member**


- I can view, borrow, and return available Books
- Once a book is borrowed, its status will change to `BORROWED`
- Once a book is returned, its status will change to `AVAILABLE`
- I can delete my own account



## Installation

- If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org)
- After doing this, confirm that you have installed virtualenv globally as well. If not, run this:

        $ pip3 install virtualenv
        
- Then, clone this repo from GIT to your PC
        
        $ git clone https://github.com/jyotib652/library-mgmt-api.git
        
- **Dependencies**

        1. Change Directory to the cloned repo directory by:
        
            $ cd library-mgmt-api
            
        2. Create and activate your virtual environment by:
        
            $ python3 -m venv venv
            $ source venv/bin/activate (for linux OS)
            
        3. Install the dependencies needed to run the app:

            $ pip3 install -r requirements.txt
            
            
        4. Apply all those migrations for your models:
            
           
            $ python3 manage.py makemigrations
            $ python3 manage.py migrate
           
            
            
- **Run the API**


    Start the server using this one simple command:
    
            $ python manage.py runserver
            
   You can now access the API service on your browser by visiting:
   
        http://localhost:8000/doc/
        


    ###### THE ENDPOINTS ARE:
    
    For the API Documentation(Swagger UI) please visit:
    
    
    
    http://localhost:8000/doc/ ,      
    http://localhost:8000/redoc/             
    
    


    
    *While Using the token, please add the string "Token" prefix before the token, like:*
    
    **Token XXXXXXXXXXYYYYYYYYYYYYYYYYYYYYYYZZZZZZZZZZZZZZZ**
    

