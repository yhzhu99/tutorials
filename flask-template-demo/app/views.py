from app import app
from flask import render_template

@app.route('/')
def index():
    user={'nickname': 'Shangzhe'}
    title='Home'
    return render_template("index.html",title=title,user=user)