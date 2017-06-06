from flask import Flask,render_template
from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/dashboard/')
def dashboard():
    return render_template("dashboard.html",topics=TOPIC_DICT)

    
@app.errorhandler(500)
def page_not_found(e):
    return "Oops,looks like we're knocked out",500

if __name__ == "__main__":
    app.run()
