from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key="hello"#T5

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database.sqlite3'
#users is the table we are using
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
class users(db.Model):
    _id=db.Column("id",db.Integer,primary_key=True)#the id for each row(unique)
    name=db.Column(db.Text())
    password=db.Column(db.Text())
    #password=db.Column(db.Text())#object attribute

    def __init__(self,name,password):
        self.name=name
        self.password=password
        #self.password=password
def validlogin(login_username,login_password):
    requiredUsrObject=users.query.filter_by(name=login_username).first()
    if (requiredUsrObject):
        if (requiredUsrObject.password==login_password):
            print("return True from validlogin()")
            return True
    else:
        print("return False from validlogin()")
        return False
registered_username=""
registered_password=""
@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=="POST":
        login_username=request.form["username"]
        login_password=request.form["password"]
        if validlogin(login_username,login_password):
            return redirect(url_for("loginSuc"))
        else:
            return redirect(url_for("login"))
    else:#get
        return render_template("login.html")

@app.route('/loginSuc')
def loginSuc():
    return "login successfully"
@app.route('/register',methods=["POST","GET"])
def register():
    global registered_username,registered_password
    if request.method=="POST":
        #submitting the form
        registered_username=request.form["username"]
        registered_password=request.form["password"]

        print(f"registered_username: {registered_username}")
        print(f"registered_password: {registered_password}")

        #found_user=users.query.filter_by(name=registered_username).first()#find the first user with name==registered_username
        newUser=users(registered_username,registered_password)#create a new user object with the registered data
        db.session.add(newUser)#like staging area
        db.session.commit()#like git commit, add to database
        #print("commit new user to db")
        return redirect(url_for("view"))
    else: #GET
        #show the webpage
        return render_template('register.html',username=registered_username,password=registered_password)
@app.route("/view")
def view():
    # s=""
    # ListOfUsers=users.query.all()
    # for i in range(1,len(ListOfUsers)+1):
    #     print(i)
    # print(f"type of users is {type(users)}")
    # print(f"type of users.query.first() {type(users.query.first())}")
    # print(f"type of values=users.query.first().name is: {type(users.query.first().name)} ")

    return render_template("view.html",usersFromBE=users.query.all())
@app.route("/clearDB")
def clearDB():
    db.drop_all()
    db.create_all()
    flash("You have clear the database successfully","info")
    return render_template("view.html",usersFromBE=users.query.all())



    #return render_template("view.html",values=users.query.all().)

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
