from flask import Flask, session, render_template, redirect, request
import random
app = Flask(__name__)
app.secret_key = "becauseImBatman"

@app.route("/")
def index():
    # session.clear()
    if not "total_gold" in session:
        session["total_gold"] = 0
    if not "log" in session:
        session["log"] = []
    return render_template("/index.html")

@app.route("/process_money", methods=["POST"])
def process_money():
    if request.form["location"] == "farm":
        print "Farm selected" # for debugging
        session["new_gold"] = random.randint(10, 20)
        print "random amomunt of gold is", session["new_gold"] # for debugging
        session["total_gold"] += session["new_gold"]
        session["log"].append("You gained " + str(session["new_gold"]) + " gold")
    elif request.form["location"] == "cave":
        print "cave selected" #for debugging
        session["new_gold"] = random.randint(5, 10)
        print "random amount of gold is ", session["new_gold"] #for debugging
        session["total_gold"] += session["new_gold"]
        session["log"].append("You gained " + str(session["new_gold"]) + " gold" )
    elif request.form["location"] == "house":
        print "House selected" #for debugging
        session["new_gold"] = random.randint(2, 5)
        print "random amount of gold is ", session["new_gold"] #for debugging
        session["total_gold"] += session["new_gold"]
        session["log"].append("You gained " + str(session["new_gold"]) + " gold" )
    elif request.form["location"] == "casino":
        print "Casino selected" #for debugging
        session["new_gold"] = random.randint(-50, 50)
        print "random amount of gold is ", session["new_gold"] #for debugging
        session["total_gold"] += session["new_gold"]
        session["log"].append("You gained " + str(session["new_gold"]) + " gold" )
    return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
    session.clear()
    return redirect("/")

app.run(debug=True)