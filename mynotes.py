from flask import Flask, render_template, request, session
#from flask_session.__init__ import Session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#mynotes = []

@app.route("/", methods=["GET", "POST"])
def index():
    if session.get("mynotes") is None:
        session["mynotes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["mynotes"].append(note)

    return render_template("index.html", mynotes=session["mynotes"])