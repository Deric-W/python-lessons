# gibt alle Zeilen einer Datei aus
with open("test1.txt", mode='r') as f:
    for line in f:
        print(line)

# schreibe einen String und lese ihn wieder
with open("test2.txt", mode='w+') as f:
    # oder print("Test", file=f)
    f.write("Test\n")
    # seek ändert die Position innerhalb der Datei
    # und gibt ihren neuen Wert zurück
    f.seek(0) == 0
    # tell gibt diese zurück ohne sie zu ändern
    f.tell() == 0
    print(f.read())

# öffnet eine Datei falls sie nicht existiert
try:
    f = open("test.txt", "x")
except FileExistsError:
    print("Datei existiert bereits")
else:
    with f:
        f.write("Erster!")

# Nutzung ohne Context Manager
f = open("test.txt")
try:
    # nutze die Datei
    pass
finally:
    f.close()
