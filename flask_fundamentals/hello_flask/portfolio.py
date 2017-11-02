from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/projects')
def hello_world():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')



app.run(debug=True)