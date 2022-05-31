from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
<<<<<<< HEAD
def index(name="what's is up!!"):
    return render_template('index.html',text=name)
=======
def index(name="Hello World"):
    return render_template("index.html.jinja", text=name)

>>>>>>> c0eee68a93d3045fc4c9492194fbd6e22de452b0
