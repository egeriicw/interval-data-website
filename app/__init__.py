from flask import Flask
 
myApp = Flask(__name__)
myApp.debug = True
from app import views