from flask import Flask, render_template, redirect, request, session
from mysqlconnection import MySQLConnector
import random
app = Flask(__name__)
app.secret_key = "ugkjfdskgfskjdgjmvnhbhfvbhfbhf"

mysql = MySQLConnector(app, 'pokemans')

@app.route("/")          
def home():
        query = "SELECT * FROM pokemans"
        pokemans = mysql.query_db(query)  
        return render_template('index.html', pokemans = pokemans)

@app.route('/poke_data', methods=['POST'])          
def poke_data(): 
  query = "INSERT INTO pokemans (name, strength, type, health) VALUES (:poke_name, :strength, :type, :health)"
  data = {
    'poke_name': request.form['name'],
    'strength':  request.form['strength'],
    'type': request.form['type'],
    'health': request.form['health']
  }
  mysql.query_db(query, data)
  return redirect('/')

@app.route("/battle", methods=["POST"])
def battle():
  session["attacked"] = request.form["attack_button"]
  hurt = random.randint(1, 10)
  print hurt
  query = "SELECT health FROM pokemans WHERE name = :name"
  data = {
    "name": request.form["attack_button"]
  }
  current_health = mysql.query_db(query, data)[0]["health"]
  current_health -= hurt
  print current_health
  query2 = "UPDATE pokemans SET health = :health WHERE name = :name"
  data2 = {
    "health": current_health,
    "name": request.form["attack_button"]
  }
  mysql.query_db(query2, data2)
  return redirect("/")

@app.route("/choose_player", methods=["POST"])
def choose_player():
      session["player"] = request.form["choose_player"]
      return redirect("/")

@app.route("/reset", methods=["POST"])
def reset():
      session.clear()
      query = ("UPDATE pokemans SET health = 100")
      mysql.query_db(query)
      return redirect("/")
app.run(debug=True)