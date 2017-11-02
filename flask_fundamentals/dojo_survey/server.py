from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form_results', methods=['POST'])
def form_results():
    
    #This is one way of defining the variables.

    # name = request.form['name']
    # select_location = request.form['dojo_location']
    # favorite_language = request.form['favorite_language']
    # comment = request.form['comment'] 


# This is another way of defining the variables, in a dictionary. Make sure to remember to call the value of the dict in the results html document, or itll return the keys. (form_data.)
    data = {
        "name": request.form['name'],
        "dojo_location": request.form['dojo_location'],
        "favorite_language": request.form["favorite_language"],
        "comment": request.form["comment"]
    }

    return render_template("results.html", form_data = data) #form_data variable assigned the form data that has been collected in the dictionary above. This is to send the data to the results html page.


app.run(debug=True)