import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get('MONGO_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
DB_NAME = os.environ.get('DB_NAME')


app = Flask(__name__)
app.config
app.secret_key = SECRET_KEY
app.config["MONGO-DBNAME"] = DB_NAME
app.config["MONGO_URI"] = MONGO_URI


@app.route("/dashboard")
def dashboard():
   return render_template("dashboard.html", tasks=mongo.db.dashboard.find())



if __name__ == '__main__':
           app.run(host=os.environ.get('IP', '0.0.0.0'),              
           port=int(os.environ.get('PORT', 5000)),
            debug=True)
