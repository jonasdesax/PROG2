# Import der einzelnen verwendeten Modulen

from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

# Import der Datenbank
from libs import datenbank

# Upload Ordner definiert und Datentypen festgelegt
UPLOAD_FOLDER = '/static/velobilder'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# Benennung der Flaskanwendung und Auswahl des Ordners
app = Flask("Velotag")
app.config['/static/velobilder'] = UPLOAD_FOLDER

# Verknüpfung der index.html-Struktur mit der Flask App
@app.route("/")
@app.route("/index")

# gibt der Datei an, dass die Datensätze aus der Datenbank eingelesen werden sollen
def index():
    daten = datenbank.datenbank_lesen()
    return render_template("index.html", datenbank=daten)

# Verknüpfung des Formulars, welches ausgefüllt werden kann, mit der Datenbank
@app.route("/hinzuguegen", methods=['GET', 'POST'])
def hinzufuegen():
    if (request.method == 'POST'):
        datenbank.eintrag_speichern_von_formular(request.form)
        return redirect("/veloliste")

    return render_template("hinzufuegen.html") 

# Funktion um Bilder hochzuladen
# zurzeit noch fehlerhaft!
def upload_file():
    if (request.method == 'POST'):
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        print(file)
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['/static/velobilder'], filename))

# öffnet die Datenbank und gibt Sie in der HTML-Datei datenbank.html aus
@app.route("/veloliste")
def veloliste():
    daten = datenbank.datenbank_lesen()
    return render_template("datenbank.html", datenbank=daten)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
