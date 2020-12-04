import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/dashboard")
def dashboard():
    workouts = mongo.db.workouts.find()
    return render_template("dashboard.html", workouts=workouts)


#registering users
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
 # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"email" : request.form.get("signup_email").lower(),
            "username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "firstname" : request.form.get("firstname"),
            "lastname" : request.form.get("lastname"),
            "email" : request.form.get("signup_email").lower(),
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "profile_image": request.form.get("profile_image"),
             }
        mongo.db.users.insert_one(register)

        if  "profile_image" in request.files:
            profile_image = request.files["profile_image"]
            mongo.save_file(profile_image.filename, profile_image)

        # check newuser cookie session
        session["user"] = request.form.get("username").lower()
        flash("Registration successful, please login")
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        return redirect(url_for("dashboard", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    users = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
   
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))

@app.route("/logout")
def logout(): 
    #remove user from session cookies
    flash("you have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


#adding workout to mongo DB
@app.route("/add_workout", methods=["GET", "POST"])
def add_workout():
    if request.method == "POST":
        workout = { 
            "workout_type": request.form.get("workout_type"),
            "workout_distance": request.form.get("workout_distance"),
            "workout_metric": request.form.get("workout_metric"),
            "workout_duration_h": request.form.get("workout_duration_h"),
            "workout_duration_m": request.form.get("workout_duration_m"),
            "workout_date": request.form.get("workout_date"),
             "workout_description": request.form.get("workout_description"),
             "created_by": session["user"]  
        }
        mongo.db.workouts.insert_one(workout)

        
    categories = mongo.db.categories.find().sort("workout_type", 1)
    return render_template("add_workout.html", categories=categories)


if __name__ == '__main__':
           app.run(host=os.environ.get('IP', '0.0.0.0'),              
           port=int(os.environ.get('PORT', 5000)),
            debug=True)