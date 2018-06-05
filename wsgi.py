from flask import Flask, render_template


application = Flask(__name__)

@application.route('/')
def home():
    return "Hello World!"

@application.route("/hey/<string:name>")
def hey(name):
    return render_template(
        'test.html',name=name)

if __name__ == "__main__":
    application.run()
