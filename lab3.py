from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
registered_username=""
registered_password=""
#route to the index
# @app.route('/')
# def index():
#
#     return render_template('index.html')

@app.route('/register',methods=["POST","GET"])
def register():
    global registered_username,registered_password
    if request.method=="POST":
        #submitting the form
        registered_username=request.form["username"]
        registered_password=request.form["password"]
        return redirect(url_for("register"))

    else: #GET
        #show the webpage
        return render_template('register.html',username=registered_username,password=registered_password)
@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"
#lmao
if __name__=="__main__":
    app.run(debug=True)
