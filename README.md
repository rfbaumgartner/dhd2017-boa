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
* Bilder eindeutig benennen und sicherstellen, dass sie in einem `<figure>`-Element eingebettet sind. Das Stylesheet kann sie andernfalls nicht finden. Dies stellt dann ein Problem dar, wenn die Bilder mit Text einen Absatz teilen.

## Wichtigste Änderungen ggü. 2016

* in `TEIcorpus_producer.xsl ` ist statt `name` neu jeweils `persName` zu verwenden, damit die Namen in den XML-Dateien der Beiträge gefunden werden können:  
statt  
`<xsl:copy-of select="name/node()"/></name>`  
verwende  
`<xsl:copy-of select="persName/node()"/></name>`  
und statt  
```<xsl:value-of select="replace(name/surname,'[^a-zA-Z0-9]','') "/>
<xsl:value-of select="replace(name/forename,'[^a-zA-Z0-9]','') "/>```  
verwende  
```<xsl:value-of select="replace(persName/surname,'[^a-zA-Z0-9]','') "/>
<xsl:value-of select="replace(persName/forename,'[^a-zA-Z0-9]','') "/>```

* in `xsl-fo-producer.xsl` sollten die Titel nicht mit `value-of` sondern mit `apply-templates` gesucht werden und Auszeichnungen in den Titeln verwenden zu können:  
statt  
`<xsl:value-of select="teiHeader/fileDesc/titleStmt/title"/>`  
verwende
`<xsl:apply-templates select="teiHeader/fileDesc/titleStmt/title"/>`  
für alle Änderungen vergleiche die Versionen [Commit 6e040cbc0dc024f3528a266294da95e494d0fb3b](https://github.com/rfbaumgartner/dhd2017-boa/commit/6e040cbc0dc024f3528a266294da95e494d0fb3b#diff-0ac4cb79ad033618eca039b9b6308508)

* Weiteres in `xsl-fo-producer.xsl`
    * ergänzt sind auch Teile für ein Rendering "bold italic" - das kann je nach Belieben auch weggelassen werden.
    * ergänzt ist das Handling für `<ref type="note">` für den Index der Fussnoten.  
(Eintrag `<xsl:when test="@type='note'"> ...` - Zeile 1571)
    * ergänzt ist das Handling für `<ptr target="http...">` für Links ohne eigenen Text.  
(Eintrag `<xsl:template match="ptr"> ...` - Zeile 1583)

## Disclaimer

Die Stylesheets finden nur, was in gewissen Mustern vorkommt und setzen es entsprechend. Da der Input grundsätzlich mehr Freiheiten lässt, als man mit den Stylesheets abbilden kann, muss man nach der Konvertierung kontrollieren, ob alles korrekt gesetzt wurde und allenfalls die Auszeichnung präzisieren oder das Stylesheet ergänzen.