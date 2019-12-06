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

def eintrag_speichern(marke, farbe, rahmen, preis, zuschlag, verkaufspreis, spende):
    datenbank = datenbank_lesen()
    datenbank[marke] = {"marke": marke, "farbe": farbe, "rahmen": rahmen, "preis": preis, "zuschlag": zuschlag, "verkaufspreis": verkaufspreis, "spende": spende}   
    print(datenbank)
    with open('datenbank.txt', "w", encoding="utf-8") as open_file:
        json.dump(datenbank, open_file)

def eintrag_speichern_von_formular(form_request):
    print(form_request)
    marke = form_request.get('marke')
    farbe = form_request.get('farbe')
    rahmen = form_request.get('rahmen')
    preis = int(form_request.get('preis'))
    if preis<50:
        zuschlag = 5
        verkaufspreis = preis + 5
    elif preis<100:
        zuschlag = 10
        verkaufspreis = preis + 10
    else:
        zuschlag = preis*0.1
        verkaufspreis = preis * 1.1
    spende = form_request.get('spende')
    eintrag_speichern(marke, farbe, rahmen, preis, zuschlag, verkaufspreis, spende)


def person_suchen(form_request):
    datenbank = datenbank_lesen()
    marke = form_request.get('marke')

    if marke in datenbank:
        return {marke: datenbank[marke]}
