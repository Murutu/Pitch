from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy

# db =SQLAlchemy()

def create_app(config_name):
    
    app = Flask(__name__)

