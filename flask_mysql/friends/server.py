from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app, 'friendsdb')

@app.route("/")
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template("index.html", friends = friends)

@app.route("/add_friend", methods=["POST"])
def add_friend():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES(:first_name, :last_name, :occupation, NOW(), NOW())"
    form_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "occupation": request.form["occupation"]
    }
    mysql.query_db(query, form_data)
    return redirect("/")




app.run(debug=True)