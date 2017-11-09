from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import md5
app = Flask(__name__)
app.secret_key = "superman_sucks"
mysql = MySQLConnector(app, 'the_wall')

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    validator = False
    #query DB to see if name already exists
    register_query = "SELECT username FROM users WHERE username = :username"
    register_data = {
        "username" : request.form["username"]
    }
    register_results = mysql.query_db(register_query, register_data)

    #validation begins here
    if len(register_results) > 0:
        flash("Oops. Another user has that username. Please choose another.")
        return redirect("/")
    else: #if username doesn't already exist, insert it into the DB, creating a new user account.

        #Request the password form data in order to hash it, and then insert it into the DB as a hash, not as cleartext. During login, it will compare the hash of the submitted login password against the one stored in the db(the one we are currently inserting).
        unhashed_password = request.form["password"]
        hashed_password = md5.new(unhashed_password).hexdigest()

        register_query2 = "INSERT INTO users (username, password) VALUES (:username, :password);"
        register_data2 = {
            "username" : request.form["username"],
            "password" : hashed_password
        }
        register_final = mysql.query_db(register_query2, register_data2)
        flash("Congrats, you have successfully created your user account!")
        return redirect("/")   

@app.route("/login", methods=["POST"])
def login():
    validator = False
    #requesting the form data for password, currently unhashed.
    unhashed_password = request.form["password"]
    print unhashed_password
    #hashing the password and saving it into a new variable
    hashed_password = md5.new(unhashed_password).hexdigest()
    print hashed_password
    login_query = "SELECT * FROM USERS WHERE username = :username AND password = :password"
    login_data = {
        "username": request.form["username"],
        #The password was hashed a few lines above.
        "password": hashed_password
    }
    print login_data
    #This session variable (name_of_user) will be used to greet the user upon login to The Wall
    session["name_of_user"] = request.form["username"]
    login_results = mysql.query_db(login_query, login_data)
    print login_results
    if len(login_results) > 0:
        session["user_id"] = login_results[0]["id"]
        validator = True
        #This code is good, but irrevelevant, since the SQL query will ONLY return something if the username and password are correct, since that's how the SQL SELECT query is structured in the WHERE clause. Therefore, simply checking if the length of the returned value is greater than one is enough to verify that the username and passwords are exactly the same as in the DB. 
        # for credential in login_results:
        # if credential["username"] == login_data["username"]:
        #     validator = True
        # if credential["password"] == login_data["password"]:
        #     validator = True
    if validator != True:
        flash("Your username or password was incorrect. Please try again.")
        return redirect("/")
    elif validator == True:
        return redirect("/wall_page")

@app.route("/wall_page")
def wall_page():
    post_select_query = "SELECT content, created_at FROM posts;"
    post_select_results = mysql.query_db(post_select_query)
    return render_template("wall_page.html", post_select_results = post_select_results)

@app.route("/post_submit", methods=["POST"])
def post_submit():
    submit_query = "INSERT INTO posts (content, users_id, created_at, updated_at) VALUES (:new_post, :user_id, NOW(), NOW());"
    submit_data = {
        "new_post": request.form["new_post"],
        "user_id": session["user_id"]
    }
    submit_final = mysql.query_db(submit_query, submit_data)
    return redirect("/wall_page")
      







app.run(debug=True)