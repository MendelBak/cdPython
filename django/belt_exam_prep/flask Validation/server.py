
# <!-- THIS IS FROM VANESSA'S GIST FROM THE LECTURE -->


from flask import Flask, render_template, redirect, request, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ugkjfdskgfskjdgjmvnhbhfvbhfbhf"

mysql = MySQLConnector(app, 'pokemans')

@app.route('/')          
def home():
  query = "SELECT * FROM pokemans"
  # save all results from DB to variable
  pokemans = mysql.query_db(query)  

  # Pass all results to template
  return render_template('index.html', pokemans = pokemans)

@app.route('/poke_data', methods=['POST'])          
def poke_data(): 
  # Before query, run validations
  valid = True
  print type(request.form['health'])

  if int(request.form['health']) < 1:
    flash("Health cannot be less than 1.")
    valid = False

  # Querying DB to check to see if the name submitted exists
  check_name_query = "SELECT name FROM pokemans WHERE name = :name"
  check_name_query_data = {
    'name' : request.form['name']
  }

  #  Query runs here
  name_check_results = mysql.query_db(check_name_query, check_name_query_data)

  # If name is taken DB will return [{'name': 'Mendel'}]
  if len(name_check_results) > 0:
    flash("There can only be 1")
    valid = False
  
  # If passes all validations
  if (valid):
    # If name is NOT taken DB will return []
    # Insert new pokeman
    query = "INSERT INTO pokemans (name, strength, type, health) VALUES (:poke_name, :strength, :type, :health)"
    
    data = {
      'poke_name': request.form['name'],
      'strength':  request.form['strength'],
      'type': request.form['type'],
      'health': request.form['health']
    }

    mysql.query_db(query, data)
  
  return redirect('/')



# name unique
# health positive
app.run(debug=True)