from flask import Flask,redirect, render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

#route to the index
@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=="POST":
        #submitting the form
        usernameFromForm=request.form["username"]
        passwordFromForm=request.form["password"]

    else: #GET
        #show the webpage
        return render_template('register.html')
@app.route('/db')
def debugPage():
    return f"username{usernameFromForm}"




