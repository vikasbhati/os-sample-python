from flask import Flask, render_template
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

@application.route("/hey")
def hey():
    return render_template(
        'test.html')

if __name__ == "__main__":
    application.run()
