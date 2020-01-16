# fügt json Datei ein
import json

# liest die bestehende Datenbank, mit dem Namen datenbank.txt ein
def datenbank_lesen():
    data = {}
    # exception handling hilft, falls ein Fehler auftreten würde
    try:
        with open('datenbank.txt', "r") as open_file:
            data = json.load(open_file)
    except:
        print("Fehler mit Datei!") # gibt die Fehlermeldung "Fehler mit Datei" aus
    finally:
        return data

# speichert einen neuen Eintrag von der HTML-Datei in die Datenbank ein
def eintrag_speichern(marke, farbe, rahmen, preis, zuschlag, verkaufspreis, spende):
    datenbank = datenbank_lesen()
    datenbank[marke] = {"marke": marke, "farbe": farbe, "rahmen": rahmen, "preis": preis, "zuschlag": zuschlag, "verkaufspreis": verkaufspreis, "spende": spende}   
    print(datenbank)
    # gibt an, dass eine neue Datei geschrieben wird, respektive der neue Datensatz in der Datenbank gespeichert wird
    with open('datenbank.txt', "w", encoding="utf-8") as open_file:
        json.dump(datenbank, open_file)

# mit der Methode "get", werden die eingetragenen Daten an die python-Datei übertragen
def eintrag_speichern_von_formular(form_request):
    print(form_request)
    marke = form_request.get('marke')
    farbe = form_request.get('farbe')
    rahmen = form_request.get('rahmen')
    preis = int(form_request.get('preis'))
    # hier wird mithilfe einer if-Schleife, der Preis berechnet, es bestehen variable Preise
    if preis<50: # bis 50.- ist der Zuschlag 5.-
        zuschlag = 5
        verkaufspreis = preis + 5
    elif preis<100: # bis 100.- ist der Zuschlag 10.-
        zuschlag = 10
        verkaufspreis = preis + 10
    else:
        zuschlag = preis*0.1 # über 100.- ist der Zuschlag jeweils 10%
        verkaufspreis = preis * 1.1
    spende = form_request.get('spende')
    # hier wird angegeben, dass alle erfassten und berechneten Informationen auch korrekt und vollständig übertragen werden
    eintrag_speichern(marke, farbe, rahmen, preis, zuschlag, verkaufspreis, spende) # auch der Zuschlag und der Verkaufspreis wird reingenommen

# hier wird ermöglicht, dass ein Fahrrad gesucht werden kann
# dies dient für eine spätere Erweiterung des Projektes, sodass der Kunde nach seinen Fahrrädern suchen kann
def eintrag_suchen(form_request):
    datenbank = datenbank_lesen()
    marke = form_request.get('marke')

    if marke in datenbank:
        return {marke: datenbank[marke]}
