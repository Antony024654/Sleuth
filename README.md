| ![Status](https://img.shields.io/badge/status-stable-brightgreen?style=flat-square)| ![Version](https://img.shields.io/badge/version-1.0.0-blue?style=flat-square)| ![License](https://img.shields.io/badge/license-private-important?style=flat-square) | ![HTML](https://img.shields.io/badge/html-5-E34F26?style=flat-square&logo=html5&logoColor=white) |![CSS](https://img.shields.io/badge/css-3-1572B6?style=flat-square&logo=css3&logoColor=white) |![JavaScript](https://img.shields.io/badge/javascript-ES6+-F7DF1E?style=flat-square&logo=javascript&logoColor=black)|![Node.js](https://img.shields.io/badge/node.js-18.x-339933?style=flat-square&logo=nodedotjs&logoColor=white) |
|---|---|---|---|---|---|---|

| ![Python](https://img.shields.io/badge/python-3.12-3776AB?style=flat-square&logo=python&logoColor=white) | ![Portable Python](https://img.shields.io/badge/portable%20python-enabled-informational?style=flat-square) | ![npm](https://img.shields.io/badge/npm-enabled-CB3837?style=flat-square&logo=npm) |![Interface](https://img.shields.io/badge/interface-html%2Fjs-lightgrey?style=flat-square)|![Theme](https://img.shields.io/badge/theme-dark%2Flight%20%2B%20neon-9c27b0?style=flat-square)|![Export](https://img.shields.io/badge/export-JSON%2FCSV%2FPDF-yellow?style=flat-square)|
|---|---|---|---|---|---|

|![PDF Export](https://img.shields.io/badge/pdf-jsPDF-green?style=flat-square)|![Proxy](https://img.shields.io/badge/proxy-required-orange?style=flat-square)|![JS Libraries](https://img.shields.io/badge/libs-exifr%2Fjspdf%2Fchart.js-blueviolet?style=flat-square)|![EXIF Reader](https://img.shields.io/badge/EXIF-powered%20by%20exifr-informational?style=flat-square)|
|---|---|---|---|

<br>

|🕵️Sleuth – Metadatenanalyse🔍 & Forensik Toolkit🧰|
|---|

- ✅ Sleuth ist ein vollständig Web-Toolkit zur Analyse von Metadaten aus Bildern, Webseiten und Dokumenten.
- ✅ Online/Offline
- ✅ Inklusive EXIF-Analyse, URL-Scan, Exportfunktionen und visueller Darstellung.

<br>

|![Sleuth_github](https://github.com/user-attachments/assets/f254d3ac-d95b-44ca-9af2-f33296be40b7)|
|---|

<br>

---

<br>

## 📦 Projektstruktur

```yarn
Sleuth/
├── index.html                   # Haupt-UI
├── style.css                   # Neon-Design & Theme (Dark/Light)
├── script.js                   # Hauptlogik (Routing & Analyse)
├── README.md                   # Diese Anleitung
├── sleuth_test_exif.jpg        # Beispielbild mit EXIF
├── start_all.bat               # Startet Proxy + Webserver + öffnet Browser
├── generate_exif.bat           # Erzeugt Testbild mit EXIF-Daten
├── exif_gen.py                 # Python-Skript für Bild mit EXIF
├── py312/                      # (optional) portable Python 3.12 Umgebung
└── modules/
    ├── imageMeta.js            # EXIF-Analyse
    ├── urlMeta.js              # Webseitenanalyse
    ├── exportModule.js         # JSON-Export
    ├── exportCSV.js            # CSV-Export
    ├── reportGenerator.js      # PDF-Export mit jsPDF
    ├── darklightToggle.js      # Theme-Umschaltung
```

<br>

---

<br>

|🚀 Installation & Setup (Windows – Offlinefähig)|
|---|

> ✅ Python portable (3.12) installieren
  - Lade herunter:
    - [👉DOWNLOAD - Python 3.12.3]( https://www.python.org/ftp/python/3.12.3/python-3.12.3-embed-amd64.zip)

<br>
   
- Entpacke das Archiv nach:

```yarn
Sleuth/py312/
```

<br>

- Öffne py312/python312._pth und trage folgendes ein:

```yarn
python312.zip
.
import site
```

> Damit pip und Pakete funktionieren

<br>

---

<br>

>✅ pip, Pillow und piexif installieren
- Im Terminal:

```yarn
cd Sleuth
py312\python.exe get-pip.py
py312\python.exe -m pip install pillow piexif
```

> Falls get-pip.py fehlt, lade hier herunter:
  - [👉DOWNLOAD - get-pip](https://bootstrap.pypa.io/get-pip.py)

<br>

---

<br>

>🖼️ Beispielbild mit EXIF erzeugen
 - Verwende:

```yarn
ImageCreator.exe → Doppelklick
```

> oder direkt:

```yarn
py312\python.exe exif_gen.py
```

> Das Bild sleuth_test_exif.jpg wird erstellt und kann anschließend über Sleuth analysiert werden.

<br>

---

<br>

> 🧪 Projekt starten
  - ✅ Variante 1: Alles automatisch

```yarn
Doppelklick auf ServerStarter.exe
```

- startet Proxy (Port 8000)
  - startet Python Webserver (Port 8000)
    - öffnet Browser mit Sleuth
   
<br>

✅ Variante 2: manuell

```yarn
node proxy.js
py312\python.exe -m http.server 8000
```

> Dann im Browser:
  [👉LOCALHOST](http://localhost:8000)

<br>

---

<br>

>🌐 Proxy notwendig für URL-Analyse
  - Sleuth verwendet **fetch()** über Proxy:

```yarn
http://localhost:3000/proxy?url=https://example.com
```

> Daher:
  - **node proxy.js** muss laufen
    - Port ***8000** darf nicht blockiert sein

<br>

---

<br>

> 🧠 Kompatibilitäten & Hinweise

| Komponente |             Version / Voraussetzung           |                 Inkompatibel                    |
|    :---:   |                   :---:                        |                   :---:                        |
|            |                                                |                                                |
| **Python** | ✅ Nur **3.12.x** empfohlen (nicht 3.13+/3.14) |                                              |
| **Pillow** | ✅ ab **9.x – 11.x** kompatibel                |                                              |
| **piexif** | ✅ funktioniert mit **Python 3.12**,           |            ❌ nicht mit 3.14                 |
| **jsPDF**  | 📦 eingebunden via CDN                         |
| **exifr**  | 🚀 verwendet für moderne EXIF-Analyse          |

<br>

---

<br>

> 🧪 Unterstützte Dateitypen

| Typ   | Funktion                                                           |
|    :---:   |                   :---:                                      |
|            |                                                              |
| **JPG**  | ✅ EXIF-Analyse                                                |
| **PNG**  | ⚠️ Teilweise unterstützt – keine klassischen EXIF-Daten        |
| **PDF**  | 📝 Basis-Metadaten (z. B. Titel, Ersteller, Erstellungsdatum)  |
| **URL**  | 🌐 Analyse von `<title>`, Meta-Description, OpenGraph via Proxy |

<br>

---

<br>

> 📁 Hinweise zu Verzeichnissen

| Ordner     |                  Inhalt                     |
|    :---:   |                   :---:                      |
|            |                                              |
| `/modules/` | 🔧 Alle JavaScript-Funktionen modular       |
| `/py312/`   | 🐍 Portable Python 3.12 inkl. Pip & Pillow  |
| Root (`/`)  | 📄 `index.html`, `style.css`, `script.js`   |

<br>

---

<br>

> 🧩 Optional: Erweiterungen
- 📍 GeoMap (Leaflet)
- 📈 Timeline (Chart.js)
- ⚡ Drag&Drop-Unterstützung
- 🧪 Vergleichsansicht
- 🔌 Plugin-System

> Diese erscheinen in der nächsten Version

<br>

---

<br>

> 👨‍💻 Entwickler
  - Erstellt & strukturiert von Thorsten Bylicki

---
