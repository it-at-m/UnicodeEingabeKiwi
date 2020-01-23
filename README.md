# Virtuelles Keyboard (KIWI) #

## Hintergrund ##
*KIWI* (**Ki**nderleicht **W**ortbestandteile **i**ntegrieren) ist eine Eingabehilfe, welche der komfortablen und effizienten Eingabe von Zeichen aus dem Zeichenvorrat *Lateinische Zeichen in Unicode* dient. Zeichen mit Diakritika (z.B. Ẫ, D̂, Ģ, und M̂) oder nicht deutschen Ursprungs (z.B. ð, ø oder þ) findet man auf herkömmlichen deutschen Tastaturen in der Regel nicht. KIWI macht alle Zeichen aus dem Zeichensatz *Lateinische Zeichen in UNICODE* leicht auffindbar und eingebbar. In KIWI können mittels herkömmlicher Tastatur z.B. Namen mit diakritischen Zeichen einfach eingegeben und dann mittels Copy & Paste in beliebige (Fach-)Anwendungen übernommen werden. Der Zeichensatz *Lateinische Zeichen in UNICODE* ist insbesondere für Namen natürlicher und juristischer Personen sowie bei Adressen relevant. 

*Lateinische Zeichen in Unicode* ist ein Standard, der von der [Koordinierungsstelle für IT-Standards (KOSIT)](https://www.xoev.de/) im Auftrag des [IT-Planungsrats](https://www.it-planungsrat.de/) erstellt wurde. Zusammengefasst wird darin für die deutsche öffentliche Verwaltung verbindlich definiert, was unter Unicode-konformer Verarbeitung mindestens verstanden wird. Mit der [Entscheidung 2014/04](http://www.it-planungsrat.de/DE/Entscheidungen/2014/13_Sitzung/13_Sitzung_Entscheidungen.html) hat der IT-Planungsrat in seiner 13. Sitzung den Zeichensatz *Lateinische Zeichen in UNICODE* festgelegt, der von IT-Verfahren in der Bundesrepublik Deutschland unterstützt werden muss.

Siehe auch:
* [Wikipedia](https://de.wikipedia.org/wiki/Lateinische_Zeichen_in_Unicode)
* [KOSIT](https://www.xoev.de/detail.php?gsid=bremen83.c.4813)

## Vorausetzungen für den Build ##
*Hinweise*: 
* Für die Entwicklung oder das Bauen der Anwendung ist Linux von Vorteil, da dort einige der notwendigen Tools über das Paketmanagement zur Verfügung stehen und nicht einzeln heruntergeladen werden müssen. 
* Alle Tools müssen im Pfad (Umgebungsvariable *PATH*) erreichbar sein. Unter Windows empfiehlt es sich darum den Build aus der GIT-Shell heraus aufzurufen.

Die folgenden Tools sind für einen Build mindestens notwendig:

1. Installation vom [GIT](https://git-scm.com/)
2. Installation von [Maven](https://maven.apache.org/) und [Java](https://www.java.com/)
3. Installation von [Node.js LTS](https://nodejs.org/)
4. Installation von [Bower](https://bower.io/)
5. Installation von [Polymer 2](https://polymer-library.polymer-project.org/2.0/docs/install-2-0)
6. Installation von [Patch](http://savannah.gnu.org/projects/patch/) (Windows: [Patch für Windows](http://gnuwin32.sourceforge.net/packages/patch.htm)) (a)

Wenn eine Weiterentwicklung angestrebt wird, dann empfehlen sich darüber hinaus zusätzlich die folgenden Tools:

7. Installation von [ESlint](https://eslint.org/) und *eslint-plugin-html*
8. Installation vom [Mocha](https://mochajs.org/)
9. Installation von [bower-license](https://www.npmjs.com/package/bower-license) und [license-checker](https://www.npmjs.com/package/license-checker)
10. Installation von Google Chrome oder Chromium, da dieser Web-Browser sich am besten zum Debuggen eignet.
11. Installation von [Python 3](https://www.python.org/), für die Hilfesskripte.

 (a) Nicht notwendig, wenn unter Windows mit der GIT-Shell gearbeitet wird.

## TL;DR ##
### Testen ###
Hier gibt es eine Demo, die kein offizieller Service der Stadt München ist, aber zum Ausprobieren trotzdem gut eignet: [https://it-at-m.github.io/KiwiDemo/](https://it-at-m.github.io/KiwiDemo/) Für eine professionelle Nutzung empfehlen wir eine Installation auf einem eigenen, dedizierten Server.


### Bauen zu Entwicklungszwecken oder zum Ansehen ##
*Hinweis*: Für das Deployment empfiehlt sich ein echter Build (siehe Kapitel *Für Deployment / Betrieb*), weil damit weitere Dinge automatisiert werden.

Vorgehen:

1. *mvn clean install* ausführen, damit die Dependencies aufgelöst werden (Das Build-Ergebnis wird aber nicht direkt verwendet.)
2. *polymer serve* ausführen.
3. (Web-)Browser mit der URL aufrufen, die auf der Kommandozeile angegeben wird.


### Für Deployment / Betrieb ###
Vorgehen:

1. *mvn clean install* ausführen.
2. *jar xvf target/kiwi-polymer-1.0.0-SNAPSHOT.jar* ausführen.
3. Im entpackten Verzeichnis *static* sind zwei Versionen von KIWI enthalten, die im *DocumentRoot* eines Web-Servers deployed werden können
    * *es6-root-test*: Version für Tests 
    * *es6-root-optimized*: Optimierter Code 

## Lizenzierung und Copyright ##
© Copyright 2019 – it@M

*Kiwi* ist lizenziert unter der *European Union Public Licence (EUPL)*.

## Namen ##
Der Namen dieser Software ist *KIWI*, im Programmcode wird jedoch durchgängig der Projektname *VirtualKeyb* verwendet. Nur an der Benutzeroberfläche ist durchgängig von *KIWI* die Rede.

## Builds ##

Das Build-System basiert auf Maven und integriert die für einen erfolgreichen Build einer Anwendung notwendigen Schritte bzw. notwendigen Aufrufe der Tools. Damit verschiedene konkurrierende Ziele eines Builds bedient werden können sind verschiedene Maven-Profile definiert.

### Maven-Profile ###
* *with-tests*:
    * Startet einen Build, der anschließend Unit-Tests ausführt.
    * Wenn dieses Profil aktiviert wird, so muss gleichzeitig das Profil *with-build* deaktiviert werden.
* *with-es-lint*:
    * Integriert *eslint* in den Build.
* *with-build*: (Standardmäßig aktiviert)
    * Führt auch *polymer build* aus und entfernt die Font-Referenzen auf Google-Server

### Release-Builds ###

#### Reproduzierbarkeit ####

Die verwendente Version 2 von Polymer setzt auf [Bower](https://bower.io/) auf. Bower erlaubt Stand Juli 2019 nicht, die Dependencies (genauer deren Version) zu pinnen. Viel mehr setzt Bower auf [Semantic Versioning](https://semver.org/lang/de/), bei dem der Ersteller der Komponenten anhand der vergebenen dreiteilige Versionsnummer dokumentiert, ob und wie kompatibel eine Version der Komponente mit einer anderen Version ist. Die Syntax der Versionsbezeichnungen für Polymer (und auch *npm*; in Verwendung für ein paar nur dort verfügbare Polyfills; dort kann die Version aber sehr wohl gepinnt werden!) kann in einem [Stack-Overflow-Artikel](https://stackoverflow.com/questions/19030170/what-is-the-bower-and-npm-version-syntax) nachgelesen werden. Zusammengefasst: Ein Build kann nicht zu 100% reprodziert werden. Aus diesem Grund gibt es zur Hilfe bei der Identifikation der Version neben der Version eine Build-Nummer. 

Da es nicht ausreicht, auf Basis der Version aus dem Versionkontrollsystem eine alte Version neu zu bauen, sollte man das Build-Ergebnis archvieren. Dazu empfiehlt sich die Archvierung des folgenden Artefakts: *~/.m2/repository/de/muenchen/uc/kiwi-polymer/1.0.0-SNAPSHOT/kiwi-polymer-1.0.0-SNAPSHOT.jar*, wobei die Versionsbezeichnungen und die Build-Nummer in den Dateinamen aufgenommen werden sollte.

### Tests ausführen ###

1. Starten des in der Polymer-CLI eingebauten Web-Servers in diesem Verzeichnis.
    * I.d.R. wird hier unter [Localhost auf Port 8081](http://localhost:8081) ein Web-Server gestartet. In nachfolgenden Beschreibungen wird davon ausgegangen.
2. Starten eines Test-Builds
    * Hinweis: Leider muss man sich zu Beginn eines Builds entscheiden, ob das Ergebnis ein Release-Build oder ein Test-Build (= Build für die Durchführung von Tests) sein soll. In der Folge kann daraus ohne einen vollständigen (Re-)Build kein Release-Build angestossen werden.

    mvn clean install -Pwith-test 2>&1 | tee m.out

3. Starten eines Web-Browsers, navigieren zur URL [http://localhost:8081/test/polymer/index.html](http://localhost:8081/test/polymer/index.html).
    * Hinweis: Durch Zugriff im Web-Browsers auf die oben genannten URL werden die (Unit-)Tests im Browser ausgeführt und die Testergebnisse angezeigt.

### Dependencies ###

Sowohl *bower* als auch *npm* benutzen [semantic versioning](https://semver.org/lang/de/) und die gleiche Syntax für Versionsbezeichnungen, die [hier](https://stackoverflow.com/questions/19030170/what-is-the-bower-and-npm-version-syntax) und [hier](https://docs.npmjs.com/about-semantic-versioning) schön beschrieben ist.

#### *bower*-Dependencies ####

* Es dürfen nur Dependencies der Version V2.x.x verwendet werden, da Dependencies mit > V2.x.x. inkompatible Änderungen enthalten. 
* Mit folgendem Kommando kann geprüft werden, ob *bower*-Dependencies veraltet sind:

    bower list

#### *npm*-Dependendies ####

* Mit folgendem Kommando kann geprüft werden, ob *npm*-Dependencies veraltet sind:

    npm outdated

## Running ##

### Log-Level ### 
* Der Standard-Logleve von KIWI ist "WARN". 
* Um den Loglevel zu ändern kann im Localstorage der Key *loglevel* angelegt werden, der dann einen der anderen Levels enthält: *TRACE*, *DEBUG*, *INFO*, *WARN*, *ERROR*.

### Lokaler Web-Server für Entwicklungs- und Testarbeiten ###
* Im Verzeichnis *VirtualKeyboard* das Kommand *polymer serve* ausführen.

### Docker container lokal ###
* Lokalen docker container starten: *docker run -it --name virtkeyb -p 8080:80 virtkeyb-docker-local*
* Mit Browser navigieren zu *http://localhost:8080/*

### Deployment auf Web-Server ###
* Die Anwendung besteht nur aus statischen Dateien, die auf einem [Apache HTTPD](https://httpd.apache.org/) im *DocumentRoot* gehostet werden können.
* Die Anwendung kann nach einem erfolgreichen Build der Zip-Datei *~/.m2/repository/de/muenchen/uc/kiwi-infrastructur-lhm/1.0.0-SNAPSHOT/kiwi-infrastructur-lhm-1.0.0-SNAPSHOT-web.zip* entnommen werden.
* Damit die Anwendung einfach das Caching steuern kann, muss der Apache Web-Server wie folgt konfiguriert werden:
    * HTTPS-Zertifikat passend zur Domain
    * [AllowOverride-Direktive](https://httpd.apache.org/docs/2.4/de/mod/core.html#allowoverride) auf *All* setzen.
        * Die lokale Konfiguration ist in der ZIP-Datei in *.htaccess* enthalten.
    * Die Module *[mod_expires](https://httpd.apache.org/docs/current/mod/mod_expires.html)*, *[mod_deflate](https://httpd.apache.org/docs/current/mod/mod_deflate.html)* und *[mod_rewrite](https://httpd.apache.org/docs/current/mod/mod_rewrite.html)* aktivieren.


## Design-Entscheidungen ##

### Struktur (Aufbau) der App ###
* Die Anwendung, die an der GUI *KIWI* heißt, ist technisch als Custom-Element *virtkeyb-app* realisiert. 
* Die Anwendung ist bereits strukturell für eine weitere Ausbaustufe vorbereitet, die eine zweite View für eine History-Funktion vorsieht, für den in die Anwendung *Routing* eingebaut ist. Dieses Feature bzw. die dafür getroffenen Vorbereitungen wurden in der aktuellen Version mit Hilfe eines Feature-Toogles (*feature/history*) deaktiviert. 
* Die Anwendung bzw. das Custom-Tag für Kiwi untergliedert sich in verschiedene Customtags:
    * *virtkeyb-app*: Die eigentliche App, die dann auch in Web-Seiten eingebettet werden kann.
        * *vkb-model*: Custom-Tag, dass die Business-Logik kapselt. Derzeit ist das das XML-Modell, das den Zeichenvorrat und damit die Fachlichkeit kapselt.
        * *vkb-main*: Custom-Tag, das die View des Hauptbildschirms (Eingabe und Tastatur, Filter) umfasst.
            * *vkb-clipboard*: Customtag, das den Zugriff auf die Zwischenablage kapselt.
        * *vkb-history*: Customtag, das die View für die Historie realisiert.
        * *vkb-notavailable*: Customtag, das eine View realisiert, die dann angezeigt wird, wenn nicht vorhandene URLs angesteuert werden.
* Server-seitig gibt es keine Anwendungslogik oder Datenbank. Die Anwendung benutzt den Web-Server, von dem sie geladen wird, wie eine Dateiablage.

### Poly-Fill für Copy & Paste ###
* Der Zugriff aus die Zwischenablage des ausführenden Systems aus einer Web-Anwendung heraus, die in einem Browser läuft, unterliegt diversen Problemen:
* Unterschiedliche APIs in verschiendenen Browsern bzw. Browser-Versionen, z.T. auch abhängig von der Zielplattform.
* Manche Zielplattformen (z.B. iOS) lassen Zugriff nur aus Code heraus zu, der von sogenannten "trusted event" getriggert wurde. Auf Desktop-Betriebssystemen gibt es i.d.R. - die richtige API vorausgesetzt - keine Probleme beim Zugriff auf die Zwischenablage. 
* Es wurde für den Zugriff auf die Zwischenablage ein Polyfill benutzt, dass i.d.R. sehr gut funktioniert: [clipboard-polyfill](https://www.npmjs.com/package/clipboard-polyfill) 

### Datenbank für Zeichenvorrat ###
* Die Anwendung präsentiert einen wohl-definierten Zeichenvorrat, den sie in Form einer [XML-Datei](src/model/stringlatin-v2.xml) lädt.
* Die XML-Datei, die einen wohldefinierten Inhalt hat, der einem XML-Schema genügt, fungiert als Readonly-Model bzw. -Datenbank, auf der die Datei mit Hilfe von XPath die für die Funktion notwendigen Suchen durchführt. 
* Der Zeichenvorrat (plus Basiszeichen und Profile/Regionen), den die Anwendung dem Benutzer gegenüber präsentiert, kann durch das Austauschen der XML-Datei angepasst werden, wozu die Anwendung mit der geänderten/angepassten XML-Datei neu deployed werden muss. Damit keine Zusatzaufwände durch Tests der Anwendung entstehen, weist die Anwendung zwei Versionsnummern aus, damit keine Anwendungstests notwendig sind, wenn sich nur der Datenstand ändert:
    * Die Version der Anwendung, die den Stand der Anwendung selbst identifiziert.
    * Den Datenstand, der den Stand des XML-Dokuments, das den Zeichenvorrat enthält, identifiziert.
* Der Aufbau der XML-Datei ist in Form von Inline-(XML-)Kommentaren in der XML-Datei selbst und im [XMLSchema](src/model/stringlatin-v2.xsd) dokumentiert.

### Fonts ###
Die Darstellung von Zeichen mit Diakritika ist aufgrund der feinen Unterschiede für die Render-Engine des Browsers anspruchsvoll. Nachdem HTML seit der Version 2.0 Unicode fordert, sind die Browser bei der Darstellung von Zeichen mit Diakritika sehr gut. Damit die Render-Engine bei der Darstellung von Zeichen ihre Stärken voll ausspielen kann, sollte man dem Browser keine all zu engen Vorgaben zu machen. Aus diesem Grund benutzt die Anwendung als Fontstack nur den Font *sans-serif* und die im Polymer-Framework vorhandenen Referenzen auf *fonts.googleapis.com* und die *Noto-* und *Roboto-Fonts* werden beim Build-Vorgang [herausgepatcht](patches/rm-roboto.patch): 

### Lizenzen ###
* Bei der Auswahl der Komponenten, die in KIWI verwendet werden, wurde darauf geachtet, dass sie freien Lizenzen unterliegen, die die Verwendung / Nutzung in keiner Weise einschränken.
* Die Anwendung weist Lizenzen der Komponenten, die Verwendung finden in der Benutzeroberfläche [aus](src/help/de/license.html). Der Grundstock für diese statische HTML-Datei kann mit Hilfe eines kleine Python3-Scripts erzeugt werden: [gen_licenses.py](tools/gen_licenses.py).

### Caching ###
* KIWI kann grundsätzlich auf jedem Web-Server deployed werden, der Dateien mit Hilfe von HTTP/s-Zertifikaten ausliefert, die vom Browser anerkannt werden. 
* Es empfiehlt sich jedoch KIWI auf einem Apache-Web-Server zu hosten bei dem die Option *[AllowOverride](https://httpd.apache.org/docs/2.4/mod/core.html#allowoverride)* so gesetzt ist, dass *.htaccess* berücksichtigt wird. Auf diesen Weg, kann mit Hilfe der in Kiwi enthaltenen [.htaccess-Datei](.htaccess) das Caching angepasst werden. Ziel ist, ohne Änderungen am Server die Caching-Dauer der Anwendung auf dem Client anzupassen.
* Die Idee ist, dass das Caching zu Beginn einer neuen Anwendung kürzer ist (z.B. 24 Stunden), damit kurzfristig Änderungen zu den Nutzern gelangen. Wenn später die Anwendung stabilisiert ist oder die Last auf dem Web-Server stark zunimmt, dann kann die Anwendung länger gecacht werden. 

### Online-Hilfe ###
Die kontext-sensitive Hilfe ist dadurch realisiert, dass programmatisch das Element mit dem Fokus ermittelt wird und die IDs mit Hilfe einer [JSON-Datei](src/help-mapping.json) auf die URLs abgebildet werden, die dem Kontext entsprechen.

### Offline-Fähigkeit ###
Grundsätzlich kann KIWI zu einer Offline-fähigen App erweitert werden, aber derzeit ist der dafür notwendige Service-Worker deaktiviert, weil er die Caching-Einstellungen konterkariert.  

### Konfiguration ###
* Die Anwendung benutzt für die persistente Ablage von Konfigurationsdaten den *Local storage* des Web-Browsers. 
* Durch setzen von Werten (z.B. durch die Developer-Tools) kann Einfluss auf das Verhalten von Kiwi genommen werden:
    * *feature.history* (Default-Wert: *false*): kann das Feature-Toogle für die History beeinflussen.
    * *loglevel*: Wenn des Schlüssel vorhanden und dessen Wert auf *DEBUG* gesetzt ist, dann schreibt die Anwendung mehr log auf den Browser-Konsole.

### Accessibility (a11y) ###
Die Anwendung wurde auf Barrierearmut getestet:
* Mit Hilfe von [Lighthouse im Chrome Browser](https://developers.google.com/web/tools/lighthouse/)
* Durch manuelle Durchführung des [BITV-Test](https://www.bitvtest.de/) mit Level *A* und *AA*.

### GUI ###
* Grundsätzlich ist in der derzeitigen Version das (ergonomische) Funktionieren von KIWI mit Touch-Bedienung (Smartphone, etc.) nicht im Fokus, aber es wurde dort wo es leicht möglich ist, schon "mitgedacht".
    * Jeder Hot-Key kann auch über eine andere Touch-Interaktion ausgelöst werden.
    * Innerhalb der potentiell großen Menge von Zeichen kann die Auswahl der zu aktivierenden (zu drückenden) Taste durch die Cursortasten erfolgen, mit denen dann einfacher (schneller) ein Zeichen erreicht werden kann.
* Es wurde eine platzsparende GUI entworfen, die responsive ist. D.h. die Anwendung lässt sich auf dem Bildschirm klein machen ohne dabei mehr Scrollen als notwendig zu erzwingen. Wichtige Teile, konkret der Eingabepuffer bleiben auch beim Scrollen auf dem Bildschirm erhalten.
* Die GUI ist so entworfen, dass sie mit den (wohlbekannten) Browser-Tasten vergrößert (String-"+") und verkleinert (String-"-") werden kann.
* Die reine Tastaturbedienung wurde auch berücksichtigt:
    * Die üblichen Tastatur-Shortcuts wurden analog belegt: Strg-C kopiert automatisch den Puffer in die Zwischenablage
    * Es wurde eine automatische Fokussteuerung realisiert, die das häufige Springen zwischen Tastatur und Puffer beschleunigt. Sie ist für Barrierearmut in den Optionen abschaltbar.

### Error-Handling ###
* Die Anwendung wurde mit einem Error-Handing augestattet:
    * Wenn JavaScript ausgeschaltet ist, so funktioniert Kiwi (überhaupt) nicht. In diesem Fall wird der Benutzer aufgefordert es einzuschalten.
    * Im Fall von Fehlern wird in der JavaScript-Konsole protokolliert und dem Benutzer eine Fehlermeldung angezeigt.


## Suchlogik bei Suche nach Basiszeichen ##

### Hinweise ###
* Die Suche nach Zeichen ist eigentlich eine Suche nach *Graphemen*. Mit *Graphem* wir die Sequenz aus Zeichen bezeichnet, die zusammen den (graphischen) Raum eines Zeichens einnehmen: Beispielsweise ist die Sequenz *a* ein Graphem, das aus einem Zeichen besteht. Allerdings können Grapheme auch aus mehr aus einem Zeichen bestehen: Basiszeichen plus 1 - n kombinerende Zeichen: *M̂* Ist ein Graphem aus zwei Zeichen mit den Codepoints 0x004D und 0x0302.
* Wenn Nicht-Groß-Kleinschreibungssensitiv gesucht wird, dann wird das zu suchende Zeichen als die Suchmenge der Zeichen auf Kleinschreibung normiert. Wenn ein Zeichen bereits in Kleinschreibung vorliegt, dann ist bei diesem Schritt nichts zu tun.

### Algorithmus ###
1. Ermitteln des Basiszeichens anhand des gegebenen Zeichens.
    * (Such-)Kriterien
        * Zeichen hat ein Basiszeichen vom Typ *real*. 
    * Reduktion
        * Wenn genau ein Zeichen gefunden wird, dann wird dieses verwendet.
        * Wenn mehrere Zeichen gefunden werden, dann wird das Erste gemäß der Unicode-Sortierung verwendet.
        * Wenn kein Zeichen gefunden wird, dann wird das Zeichen in Normalform D zerlegt und das erste Zeichen als Basiszeichen benutzt.
2. Suchen der Zeichen, die vom Basiszeichen abgeleitet sind:
    * (Such-)Kriterien, die mit logischem *Und* kombiniert werden, sind: 
        * Profil, wobei beim Profil *Alle* alle Zeichen ohne ansehen des Profils selektiert werden.
        * Zeichen ist normativ, d.h. normativ = true.
        * Zeichen hat gegebenes Basiszeichen, wobei der Typ des Basiszeichens (*pseudo* oder *real*) für diesen Schritt irrelevant ist. 
    * Die Zeichen, die als Treffermenge herausgefiltert wurden, werden mit einer Ausnahme gemäß Unicode-Sortierung sortiert: Das erste (linkeste) Zeichen ist gemäß Fachkonzept *immer*  das Basiszeichen.
