from flask import Flask, render_template,session


application = Flask(__name__)

@application.route('/')
def hello():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Hello Boss!"

@application.route("/hey/<string:name>")
def hey(name):
    return render_template(
        'test.html',name=name)

if __name__ == "__main__":
    application.run()
