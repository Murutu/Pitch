from flask import Flask
from flask_mail import Mail


# db =SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)

