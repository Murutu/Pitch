import os
class Config:
    '''
    General configuration parent class
    '''
    debug = True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/laca'
    
    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
class ProdConfig(Config):
     '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/laca'
class TestConfig(Config):
    '''
    Test configuration child class
    Args:
        Comfig: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/laca'
    
class DevConfig(Config):
    '''
    Development configuration child class
    Args:
         Comfig: The parent configuration class with General configuration settings
    '''
    SECRET_KEY = 'talk'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://peter:ozil@localhost/laca'
    DEBUG = True
    ENV = 'development'
         
        
   
    
config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}          
    
    