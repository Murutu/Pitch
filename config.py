import os
class Config:
    '''
    General configuration parent class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/laca'