from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "superman_sucks"
mysql = MySQLConnector(app, 'email_validation')

@app.route("/")
def index():
    query = "SELECT * FROM emails"
    email_data = mysql.query_db(query)
    return render_template("index.html", email_data = email_data)

@app.route("/check_email", methods=["POST"])
def check_email():
    validator = True
    select_query = "SELECT email FROM emails WHERE email = :new_email"
    data = {
        "new_email": request.form["new_email"]
    }
    returned_email_data = mysql.query_db(select_query, data)
    if len(returned_email_data) > 0:
        flash("Email already exists. Please choose another name.")
        validator = False
    else:
        insert_query = "INSERT INTO emails (email, created_on) VALUES (:new_email, NOW());"
        mysql.query_db(insert_query, data)
    return redirect("/")

@app.route("/reset_db")
def reset_db():
    delete_query = "DELETE FROM emails" #Will delete ALL data in the database
    mysql.query_db(delete_query)
    return redirect("/")
    
app.run(debug=True)