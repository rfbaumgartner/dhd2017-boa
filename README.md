# Skripts und Schemata für den DHd2017-Konferenzband

Dieses Repository enthält die Datenbasis des
[DHd2017](http://www.dhd2017.ch/)-Konferenzbandes, bestehend aus den
Transformationsskripten, die auf der Arbeit von Karin Dalziel beruhen.

Die korrigierten XML-Dateien und die Bilder zu den Beiträgen sind lokal gespeichert.

https://github.com/karindalziel/TEI-to-PDF


## Erstellung

Eine grobe Anleitung:

* dieses Projekt klonen/herunterladen
* Apache FOP beziehen (https://xmlgraphics.apache.org/fop/)
* Saxon-HE beziehen (http://saxon.sourceforge.net/#F9.7HE)
* config/config.sh anpassen, insb. FOP und Saxon referenzieren
* erforderliche Schriften verfügbar machen
* run.sh ausführen


## Korrektur der XML-Dateien

* Manuelle Auszeichnung der Bibliographie
* Manuelle Korrektur der Titel, um kursive Sequenzen korrekt darstellen zu können
* Positionierung der Fussnoten mit dem Skript `move-notes.py` (benötigt das Python-Modul beautifulsoup4): Die Dateien vor der Umwandlung müssen dazu in den Ordner `input/xml-source` gelegt werden und das Resultat erscheint in `input/xml`. Die genauen Pfade im Skript sollten vor dem Benutzen angepasst werden. 
* Korrektur der Beitragstypen und ergänzung einer `xml:id` pro Dokument