import os 

class Config:
    SECRET_KEY = '27c1ef3f888be823ac7ac19bc9c3b41a'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    # Set above 2 variable in environment variable of system windows, linux
    '''
    after setting above to environment variable then set belows variable as 
    it is this file(flaskblog/config.py)
    
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

    '''
    MAIL_SERVER = 'smtp.gmail.com'                                     
    MAIL_PORT = 465
    MAIL_USER_TLS = False
    MAIL_USER_SSL = True
    MAIL_USERNAME = 'noreplyflask@gmail.com'
    MAIL_PASSWORD = 'qwer1234$'

