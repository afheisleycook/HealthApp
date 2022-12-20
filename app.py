import sqlite3

import flask
from flask import(Flask, request, render_template,request,url_for,jsonify,redirect)
from sqlite3 import  connect
db = connect("app.db")

app = Flask(__name__)
@app.route("/",methods=["get"])
def Main():
    if request.method == 'GET':
        db = sqlite3.connect("./data/app.db")
        conn = db.cursor()
        db = connect("app.db")
        posts =conn.execute("select * from HEALTH")
        return  render_template("index.html",posts=posts)

@app.route("/post",methods=["post"])
def Post():
    subject = request.form["subject"]
    details = request.form["details"]
    scale = request.form["number"]
    db = conn = db.cursor()
    posts = conn.execute(f"insert into HEALTH({subject},{details},{scale})")
    return redirect("/")
app.run(host="0.0.0.0",static_folder="/static")
 