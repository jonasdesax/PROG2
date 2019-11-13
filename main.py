from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask("Velotag")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", name="Startseite")

@app.route("/hinzufuegen")
def hinzufuegen():
    return render_template("hinzufuegen.html", name="Velo hinzufügen")

if __name__ == "__main__":
    app.run(debug=True, port=5000)