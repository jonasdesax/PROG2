from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

from libs import datenbank

UPLOAD_FOLDER = '/static/velobilder'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask("Velotag")
app.config['/static/velobilder'] = UPLOAD_FOLDER

@app.route("/")
@app.route("/index")
def index():
    daten = datenbank.datenbank_lesen()
    return render_template("index.html", datenbank=daten)

@app.route("/hinzuguegen", methods=['GET', 'POST'])
def hinzufuegen():
    if (request.method == 'POST'):
        datenbank.eintrag_speichern_von_formular(request.form)
        return redirect("/veloliste")

    return render_template("hinzufuegen.html") 

def upload_file():
    if (request.method == 'POST'):
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        
        print(file)
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['/static/velobilder'], filename))



@app.route("/veloliste")
def veloliste():
    daten = datenbank.datenbank_lesen()
    return render_template("datenbank.html", datenbank=daten)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
