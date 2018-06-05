from flask import Flask, flash, redirect, render_template, request, session, abort
import os

application = Flask(__name__)

@application.route('/')
def home():
    return "Hello World!"

@application.route("/hey/<string:name>")
def hey(name):
    return render_template(
        'test.html',name=name)

@app.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return home()

if __name__ == "__main__":
    application.secret_key = os.urandom(12)
    application.run()
