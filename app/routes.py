from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
@app.route('/index/<name>')
def index(name="what's is up!!"):
    return render_template('index.html',text=name)
