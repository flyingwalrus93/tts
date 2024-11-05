# A small text-to-speech experiment

Hi :)

Aaaalso, ich hab da mal ein bisschen herumgespielt. Es war nicht so erfolgreich wie gehofft, aber erfolgreicher als befürchtet...
Die nächsten Schritte klingen schlimmer als sie sind. Mir ist völlig klar, dass du nicht groß programmieren kannst, aber ich denke das Meiste beschreibe ich hoffentlich ziemlich klar.

### Schritt 1

Wir brauchen Python, die Mutter aller Script-Programmiersprachen. Das sollte hoffentlich am einfachsten sein:

> https://www.python.org/ftp/python/3.10.8/python-3.10.8-amd64.exe

Einfach herunterladen, den Installer ausführen und dann "Install Now" sagen. Wahrscheinlich ist es noch hilfreich _"Add Python.exe to PATH"_ abzuhaken, dass macht es eventuell etwas einfacher hinterher unter Windows alles zu finden. _(Ich habe hier bewusst eine etwas ältere Python-Version verlinkt, um hoffentlich Kompatibilitätsprobleme zu vermeiden.)_

### Schritt 2

Ich nehme an du hast nicht viel Erfahrung mit der Konsole (Command Line Interface [CLI]), aber die brauchen wir für die nächsten Schritte. Ich nehme für das Alles hier einfach an, dass du auf einem relativ aktuellen Windows unterwegs bist. Dort solltest du die _"Windows PowerShell"_ zur Verfügung haben. Kannst du in der Programmsuche finden und ausführen. Sollte dann ungefähr so aussehen:

> Windows PowerShell
> Copyright (C) Microsoft Corporation. Alle Rechte vorbehalten.
>
> PS C:\Users\Kim> 

Hier kannst du jetzt Befehle eingeben und mit Enter bestätigen. Als erstes kannst du zum Beispiel testen ob

> pip list

funktioniert. Das ist der Paketmanager für Python und wenn da kein Fehler kommt, ist schon viel gewonnen ;)

### Schritt 2.5

Eigentlich funktioniert Nichts hiervon, wenn du nicht eine NVIDIA Grafikkarte mit CUDA hast. Du kannst die Konsole auch nutzen um das sehr einfach zu verifizieren:

> nvidia-smi

### Schritt 3

Wir brauchen jetzt zwei zentrale Pakete, die wir mit dem Paketmanager installieren:

> pip install torch
> pip install openai-whisper

### Schritt 4

Jetzt haben wir fast Alles, aber leider auch nicht wirklich Alles. FFMPEG ist die wichtigeste Open-Source-Library für Alles was Video- und Audio-Verarbeitung angeht. Während die Installation unter Linux ein einziger Befehl ist, wird es einem unter Windows leider unnötig schwer gemacht. Da ich das selbst nicht besser beschreiben kann, folgst du am besten diesem Guide: https://www.geeksforgeeks.org/how-to-install-ffmpeg-on-windows/
Für den Befehl in "Step 4" kannst du wieder deine vorher verwendete PowerShell nutzen.

### Schritt 5

Jetzt brauchst du eigentlich nur noch das _whisper_input.py_ File, was du hier oben in diesem Repository findest. Du kannst es zum Beispiel mit diesem Befehl laufen lassen:

> python whisper_input.py C:\Users\Kim\test.mp3

Dabei ist der letzte Teil der Pfad zu der jeweiligen Audiodatei, die du verarbeiten möchtest. Das Beispiel funktioniert so nur, wenn du das _.py_-File auch in dem Pfad liegen hast, in dem du dich gerade befindest. Die Konsole gibt dir mit _"PS C:\irgendeinpfad>"_ immer an, wo du dich gerade befindest. Beim Start ist das immer dein User-Ordner. Solltest du die Datei nicht dorthin legen wollen, kannst du mit dem "cd" Befehl den aktuellen Pfad ändern, z.B.:

> cd C:\mein_kram\irgendwas

