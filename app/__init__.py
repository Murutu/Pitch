from flask import Flask
from flask_mail import Mail

def create_app(config_name):
    
    app = Flask(__name__)

