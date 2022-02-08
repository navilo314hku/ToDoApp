from flask import Flask,redirect, render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#route to the index
@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/register')
def register():
    return render_template('register.html')

