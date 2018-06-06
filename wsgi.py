from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

from random import randint

import os


application = Flask(__name__)
application.secret_key = os.urandom(12)


@application.route('/')
def hello():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return hey("")

@application.route("/hey/<string:name>")
def hey(name):
    quotes=["The limits of my language are the limits of my mind. All I know is what I have words for.",
           "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
           "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
           "'To understand recursion you must first understand recursion..' -- Unknown",
           "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
           "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
           "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    
    randomNumber = randint(0,len(quotes)-1) 
    quote=quotes[randomNumber]
    return render_template(
        'test.html', **locals())

@application.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return hello()

@application.route("/logout")
def logout():
    session['logged_in'] = False
    return hello()

if __name__ == "__main__":
    
    application.run()
