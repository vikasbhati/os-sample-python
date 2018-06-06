from flask import Flask, render_template, session, request, redirect, abort, flash


application = Flask(__name__)

@application.route('/')
def hello():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@application.route("/hey/<string:name>")
def hey(name):
    quotes=["The limits of my language are the limits of my mind. All I know is what I have words for.",
           "The limits of my language are the limits of my mind. All I know is what I have words for."]
    
    quote="The limits of my language are the limits of my mind. All I know is what I have words for."
    return render_template(
        'test.html', **locals())

@application.route('/login', methods=['POST'])
def do_admin_login():
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!')
    return hello()

if __name__ == "__main__":
    application.run()
