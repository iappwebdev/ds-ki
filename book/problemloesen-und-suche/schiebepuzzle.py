def pretty_str(zustand):
    return "\n".join(" ".join(zustand[i : i + 3]) for i in [0, 3, 6])


def pprint(zustand, ueberschrift="", anzeigen=True):
    if not anzeigen:
        return
    if ueberschrift:
        print(f"{ueberschrift}")
    print(pretty_str(zustand))


def verschiebe_pos(puzzle, pos):
    leer_pos = puzzle.index(" ")
    neu = list(puzzle)
    neu[leer_pos] = puzzle[pos]  # Stein wandert an bisher leere Position
    neu[pos] = " "  # alte Position des Steins ist jetzt leer
    return "".join(neu)


def moegliche_zuege(puzzle):
    leer_pos = puzzle.index(" ")
    y, x = divmod(leer_pos, 3)  # kurz für: y, x = leer_pos // 3, leer_pos % x
    kandidaten = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
    nachbarn = [k for k in kandidaten if k[0] in [0, 1, 2] and k[1] in [0, 1, 2]]
    return [kx + 3 * ky for (kx, ky) in nachbarn]


# Da moegliche_zuege() während der Suche sehr oft aufgerufen wird, kann man versuchen, diese Berechnung
# zu "cachen", dh die Ergebnisse zu speichern und dann nur noch abzurufen.
# Erstaunlicherweise bringt das kaum Laufzeitvorteile. Hier aber der Vollständigkeit halber

ZUGTABELLE = [
    [1, 3],
    [0, 2, 4],
    [1, 5],
    [0, 4, 6],
    [1, 3, 5, 7],
    [2, 4, 8],
    [3, 7],
    [4, 6, 8],
    [5, 7],
]


def moegliche_zuege_mit_tabelle(puzzle):
    leer_pos = puzzle.index(" ")
    return ZUGTABELLE[leer_pos]


def zugsequenz_ausfuehren(beginn, zuege, anzeigen=False):
    pprint(beginn, anzeigen=anzeigen)
    aktuell = beginn
    for i, zug_pos in enumerate(zuege):
        zug = aktuell[zug_pos]
        leer_pos = aktuell.index(" ")
        if anzeigen:
            print(
                f"\nZug {i + 1}: Verschiebe {zug} von Position {zug_pos} nach {leer_pos}:"
            )
        aktuell = verschiebe_pos(aktuell, zug_pos)
        pprint(aktuell, anzeigen=anzeigen)
    return aktuell


def interaktives_spiel(start, ziel, max_zuege=20):
    print(f"Löse das Schiebepuzzle in max. {max_zuege} Zügen!")
    zustand = start
    zug_nr = 1
    while zustand != ziel and zug_nr <= max_zuege:
        pprint(zustand, ueberschrift="\nAktueller Zustand:\n")
        print(f"\nZug {zug_nr}: Welches Feld möchtest du bewegen? ", end="")
        zuege = moegliche_zuege(zustand)
        steine = ", ".join(zustand[z] for z in zuege)
        while True:
            zug = input("Tippe " + steine + " oder Q (Abbruch):  ").upper()
            if zug in steine:
                zug_pos = zustand.index(zug)
                break
            if zug == "Q":
                return
        zustand = verschiebe_pos(zustand, zug_pos)
        zug_nr += 1
    pprint(zustand, ueberschrift="\nEndzustand")
    if zustand != ziel:
        print(f"Du hast das Puzzle leider nicht in {max_zuege} Zügen gelöst!")
    else:
        print(f"Du hast das Ziel in {zug_nr - 1} Zügen erreicht!")


import random


def erzeuge_random_walk(beginn, schritte):
    walk = []
    bekannt = set()
    aktuell = beginn
    for _ in range(schritte):
        bekannt.add(aktuell)
        zuege = moegliche_zuege(aktuell)
        random.shuffle(zuege)
        while zuege:
            zug = zuege.pop()
            neuer_zustand = verschiebe_pos(aktuell, zug)
            if neuer_zustand not in bekannt:
                aktuell = verschiebe_pos(aktuell, zug)
                walk.append(zug)
                break
        else:  # wird nur ausgeführt, wenn die while-Bedingung False wird
            # Sollte fast nie passieren: Wir können von hier aus nur in schon bekannte Zustände kommen --> Neustart
            return erzeuge_random_walk(beginn, schritte)
    return walk


### Heuristiken


def falsch_positionierte_steine(zustand, zielzustand="ABCDEFGH "):
    return (
        sum(1 for a, b in zip(zustand, zielzustand) if a != b) - 1
    )  # Leerzeichen nicht mitzählen


def manhattan_distanz(zustand, zielzustand="ABCDEFGH "):
    gesamt = 0
    for pos, stein in enumerate(zustand):
        if stein == " ":
            continue
        y, x = divmod(pos, 3)
        zpos = zielzustand.index(stein)
        zy, zx = divmod(zpos, 3)
        gesamt += abs(x - zx) + abs(y - zy)
    return gesamt


def alle_moeglichen_zuege():
    table = []
    for leer_pos in range(9):
        y, x = divmod(leer_pos, 3)  # kurz für: y, x = leer_pos // 3, leer_pos % x
        kandidaten = [(x, y - 1), (x - 1, y), (x + 1, y), (x, y + 1)]
        nachbarn = [k for k in kandidaten if k[0] in [0, 1, 2] and k[1] in [0, 1, 2]]
        table.append([kx + 3 * ky for (kx, ky) in nachbarn])
    return table


if __name__ == "__main__":

    # Ein paar Nutzungsbeispiele:

    # start = 'CBD AFGEH'
    # ziel  = 'ABCDEFGH '

    # #start = erzeuge_random_walk(ziel, 15)
    # #interaktives_spiel(start, ziel, max_zuege=20)

    # fast_am_ziel = "ABCDEFG H"
    # scheinbar_gut = " BCDEFGHA"
    # start = scheinbar_gut

    # print(falsch_positionierte_steine(start))
    # print(manhattan_distanz(start))

    # pprint(ziel)

    print(alle_moeglichen_zuege())
