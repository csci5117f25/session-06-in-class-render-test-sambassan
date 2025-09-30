from flask import Flask, redirect, render_template, request, session
import db, os

app = Flask(__name__)
db.setup()
app.secret_key = os.environ['FLASK_SECRET']

@app.route('/')

@app.route('/<name>')
def hello(name=None):
    if name and name != 'favicon.ico':
        session['name'] = name
    current_name = session['name']
    return render_template('hello.html', name=current_name, guestbook=db.get_guestbook())

@app.post('/submit') 
def submit():
    name = request.form.get("name")
    text = request.form.get("message")
    db.add_post(name, text)
    return redirect('/')
