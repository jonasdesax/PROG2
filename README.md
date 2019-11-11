# Ausgangslage

Als Organisator der Velobörse in Gossau, möchte ich gewisse Prozesse digitalisieren um so den Kunden Zeit zu ersparen. Konkret möchte ich die Veloabgabe so vereinfachen, dass die Kunden bereits im Voraus alle Daten Ihres Velos erfassen können und somit nur noch das Velo hinstellen müssen, statt darauf zu warten bis jemand Zeit hat das Velo zu erfassen. 
Zurzeit wird dieses Problem mit einem PDF-Dokument gelöst, welches per Email zugesendet werden muss, doch dies scheint der Community zu aufwendig zu sein, somit möchte ich das neu mit einer Webapplikation lösen.

# Projektidee

Mein Ziel ist es eine grafische, der Webseite angepasste, Lösung zu schaffen, welche den Kunden ermöglicht direkt alle Angaben online zu erfassen. Für die Eingabe wird ein Benutzerkonto verwendet, der User muss sich somit registrieren. Die Eingabe soll über eine Art Formular laufen und für jedes erfasste Fahrrad soll eine eindeutige ID vergeben werden, damit beim Verkauf nichts falsch läuft. Die gesamte Lösung ist vorallem für Kunden angedacht, welche mehrere Velos zum Verkauf anbieten möchten. Des Weiteren soll am Ende eine Art Quittung generiert werden, wo alle erfassten Fahrräder aufgelistet werden. Diese Quittung sollte perfekt auf ein A4-Format druckbar sein. 

# Pain Points

- Registrieren- und Anmelde-Button programmieren, sodass es sicher ist
- ID's vergeben für jedes einzelne erfasste Velo
- Quittung erstellen im A4-Format
- Formular für Kunde und Formular für mehrere oder ein Velo variabel anpassbar, mit "Zeile hinzufügen"-Button
- Speichern der eingegeben Daten in einer Textdatei
- Abrufen der Daten aus einer Textdatei

# Flowchart 1.1
![flowchart](Flowchart.png "Flowchart")
