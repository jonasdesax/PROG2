import json

def datenbank_lesen():
    data = {}
    try:
        with open('datenbank.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Fehler mit Datei!")
    finally:
        return data

def eintrag_speichern(marke, farbe):
    datenbank = datenbank_lesen()
    datenbank[marke] = {"marke": marke, "farbe": farbe}   
    print(datenbank)
    with open('datenbank.txt', "w", encoding="utf-8") as open_file:
        json.dump(datenbank, open_file)

def eintrag_speichern_von_formular(form_request):
    print(form_request)
    marke = form_request.get('marke')
    farbe = form_request.get('farbe')
    eintrag_speichern(marke, farbe)


def person_suchen(form_request):
    datenbank = datenbank_lesen()
    marke = form_request.get('marke')

    if marke in datenbank:
        return {marke: datenbank[marke]}

