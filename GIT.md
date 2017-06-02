# Wichtige Git Kommandos

* `git clone <repo>`: Kommando um Repo auf Deinen Rechner zu bekommen.
* `git status`: Wie ist der Status meines lokalen Repos?
* `git add <filename>`: Geänderte Datei(en) in Staging Area sammeln.
* `git commit -m "<message>"`: Alle Dateien in Staging Area ins lokale Repo einchecken.
* `git checkout -- <filename>`: Lokale änderungen rückgängig machen.
* `git push`: Commits im lokalen Repo zu Remote schieben.
* `git pull`: Commits aus dem remote Repo auf deinen Rechner bekommen.

Git Essentials: https://github.com/hughfdjackson/git-essentials

# Git einrichten
Bitte folgende Kommandos ausführen um Fehlermeldungen zu unterdrücken und handhabung ein wenig vereinfachen:
```
git config --global user.name "<vorname>"
git config --global user.email <email>
git config --global pull.rebase true
```

# Hilfe!
Falls Du im Vim Modus gelandet bist, folgendes ausführen: `:wq`
