from flask import Flask
from flask import render_template

app = Flask("Telefonbuch")

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html', name="Jonas")

if _name_ == "_main_":
    app.run(debug=True, port=5000)