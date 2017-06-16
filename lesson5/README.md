## Aufgabe 1
Schreibe eine Funktion, namens `greet()` die als Eingabe einen Namen als String und ein Booleschen Wert nimmt.
Falls der Wert True ist, gibt die Funktion ein Kompliment zurück, falsch False, gibt die Funktion eine (sehr milde) Beleidigung zurück.

Bsp Anwendung:
```
reply = greet("Donald", True)
print reply
```
Die Ausgabe:
`"Donald, you are the best"`

## Aufgabe 2
Schreibe eine Funktion, namens `list_info()` die als Eingabe eine beliebige Liste bekommt. Die Ausgabe (mittels `print()`) ist zB:
```
Die Liste is 20 Elemente lang
Das erste Element ist 7
Das letzte Element ist 88
```

## Aufgabe 3
Schreibe eine Funktion namens `less_than_10()`, die als Eingabe eine Liste mit Ints bekommt. Die Funktion soll eine neue Liste zürück geben, in der alle Ints größer 10 entfernt wurden.
Im Code sieht es dann so aus:
```
a = [12, 9, 3, 92, 3, 2, 0, -1]
b = less_than_10(a)
print b
```
Die Ausgabe wäre dann: `[9, 3, 3, 2, 0, -1]`

Für diese Aufgabe braucht ihr
 * `append()` oder `remove()` je nachdem, wie ihr es löst
 * eine **for** schleife!

Ihr müsst euch einlesen ;-)
