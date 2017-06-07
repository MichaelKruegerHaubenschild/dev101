# Python
Python Einführung: http://www.thomas-guettler.de/vortraege/python/einfuehrung.html

## Datentypen

| Datentyp | Code | Erklärung|
|--|--|--|
| Boolean	| True, False	| Boolean |
| Integer	| `i = 1`	| Ganzzahl |
| Float	| `f = 0.1`	| Gleitkommazahl |
| String	| `s = 'hallo'`	| Zeichenkette |
| Liste	| `l = [1, 2, 3]`	| Veränderbare Liste |
| Tuple	| `t = (1, 2, 3)`	| Unveränderbare Liste |
| Menge	| `z = set([1, 1, 2, 2, 3]) --> set([1, 2, 3])`	| Menge (ohne Dopplungen)|
| Dictionary |	`d = {1: 'eins', 2: 'zwei', 3: 'drei'}`	| Auch Hash oder assoziatives Array  genannt. |

### Strings
Beispiele:
```
s1 = 'Beispiel'

s2 = 'Er sagte "Hallo" zu mir'

s3 = "er ist der 20'te"

s4 = """Mehrere Zeilen
Zeile 2
Zeile 3
"""

s5 = '''Ebenfalls mehrere
Zeilen
```

### Typ-Umwandlungen
* int(), float(), string()

### User input
* `raw_input()`: liefert ein String
* `input()`: liefert ein int oder double
* Im Zweifelsfall `type(<variable>)`verwenden um zu erfahren, welcher Typ es ist.

### Operatoren
http://www.python-kurs.eu/python3_operatoren.php

| Operator | Name |
|--|--|
| +, - |	Addition, Subtraktion	|
| *, %	| Multiplikation, Rest |
| <, <=, >, >=, !=, == | Vergleichsoperatoren |
| or, and, not	| Boolsches Oder, Boolsches Und, Boolsches Nicht |

## Funktionen
Funktionen werden durch das Schlüsselwort 'def' definiert:
```
def plus(a, b):
    return a+b
```

## Kontrol-Strukturen
### If Then Else
Beispiel:
```
if x < 0:
  x = 0
  print 'Negative changed to zero'
elif x == 0:
  print 'Zero'
elif x == 1:
  print 'Single'
else:
  print 'More'
```

Siehe: https://docs.python.org/2/tutorial/controlflow.html

## Lists
