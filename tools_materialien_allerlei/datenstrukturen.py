from __future__ import annotations
from typing import Any


class Knoten:
    def __init__(self, inhalt: Any, naechster: Knoten = None):
        self.inhalt = inhalt
        self.naechster = naechster


class VerketteteListe:

    def __init__(self):
        self.erster: Knoten | None = None  # Der erste Knoten in der Liste (Listenkopf)

    def __str__(self) -> str:
        """Gibt die Liste als Zeichenkette, getrennt durch Pfeile, zurück."""
        inhalte = []
        knoten = self.erster
        while knoten is not None:
            inhalte.append(knoten.inhalt)
            knoten = knoten.naechster
        return " -> ".join(inhalte)

    def einfuegen_vorne(self, pInhalt):
        """Fügt einen neuen Knoten mit pInhalt am Anfang der Liste ein."""
        neu = Knoten(pInhalt)  # "Verpacke" den Inhalt in einen Knoten
        neu.naechster = (
            self.erster
        )  # Nachfolger des neuen Knotens ist der bisherige Listenkopf
        self.erster = neu  # Der neue Knoten ist ab jetzt der Listenkopf

    # AUFGABE: Implementiere die folgenden Methoden für die Klasse VerketteteListe:

    def ist_leer(self) -> bool:
        """gibt True zurück, wenn die Liste leer ist, sonst False"""
        if self.erster is None:
            return True
        else:
            return False

    def anzahl_elemente(self) -> int:
        """gibt die Anzahl der Elemente in der Liste zurück"""
        anzahl = 0
        aktuell = self.erster
        while aktuell is not None:
            anzahl += 1
            aktuell = aktuell.naechster
        return anzahl

    def gib_inhalt(self, index: int) -> Any:
        """gibt den Inhalt des Knotens an der Stelle index zurück"""
        if self.erster is None:
            return None
        aktuell = self.erster
        for i in range(index):
            if aktuell.naechster is None:
                return None
            aktuell = aktuell.naechster
        return aktuell.inhalt

    def ersetzen(self, index: int, neuer_inhalt: Any) -> None:
        """ersetzt den Inhalt des Knotens an der Stelle index durch neuer_inhalt"""
        if self.erster is None:
            return
        aktuell: Knoten = self.erster
        for i in range(index):
            if aktuell.naechster is None:
                return
            aktuell = aktuell.naechster
        aktuell.inhalt = neuer_inhalt

    def enthaelt(self, inhalt: Any) -> bool:
        """gibt True zurück, wenn inhalt in der Liste enthalten ist, sonst False"""
        aktuell = self.erster
        while aktuell is not None:
            if aktuell.inhalt == inhalt:
                return True
            aktuell = aktuell.naechster
        return False

    def anhaengen(self, inhalt: Any) -> None:
        """hängt einen neuen Knoten mit dem Inhalt inhalt ans Ende der Liste an"""
        neu = Knoten(inhalt)
        if self.erster is None:
            self.erster = neu
        else:
            aktuell = self.erster
            while aktuell.naechster != None:
                aktuell = aktuell.naechster
            aktuell.naechster = neu

    def entfernen_vorne(self) -> Any:
        """entfernt den ersten Knoten und gibt dessen Inhalt zurück"""
        if self.erster is None:
            return None
        inhalt = self.erster.inhalt
        self.erster = self.erster.naechster
        return inhalt

    def entfernen(self, index: int) -> Any:
        """entfernt den Knoten an der Stelle index und gibt dessen Inhalt zurück"""
        if self.erster is None:
            return None
        if index == 0:  # Spezialfall: Erstes Element entfernen
            inhalt = self.erster.inhalt
            self.erster = self.erster.naechster
            return inhalt
        aktuell = self.erster
        for i in range(index - 1):
            if aktuell.naechster is None:
                return None
            aktuell = aktuell.naechster
        if aktuell.naechster is None:
            return None
        inhalt = aktuell.naechster.inhalt
        aktuell.naechster = aktuell.naechster.naechster
        return inhalt

    def einfuegen(self, index: int, inhalt: Any) -> None:
        """fügt einen neuen Knoten mit inhalt an der Stelle index ein"""
        if index == 0:
            self.einfuegen_vorne(inhalt)
            return
        neu: Knoten = Knoten(inhalt)
        # Knoten vor der Einfügeposition finden
        aktuell = self.erster
        for i in range(index - 1):
            if aktuell is None:
                return
            aktuell = aktuell.naechster
        if aktuell is None:
            return
        # Knoten zwischen den Knoten einfügen
        neu.naechster = aktuell.naechster
        aktuell.naechster = neu

    def entfernen_inhalt(self, inhalt: Any) -> None:
        """entfernt alle Knoten mit dem gegebenen Inhalt"""
        if self.erster is None:
            return
        while self.erster is not None and self.erster.inhalt == inhalt:
            # Spezialfall: Erstes Element (und evtl. weitere) enthält den gesuchten Inhalt
            self.erster = self.erster.naechster
        aktuell = self.erster
        while aktuell is not None and aktuell.naechster is not None:
            if aktuell.naechster.inhalt == inhalt:
                aktuell.naechster = aktuell.naechster.naechster
            else:
                aktuell = aktuell.naechster


##############################################################################


class Stapel:

    class Knoten:
        def __init__(self, inhalt, naechster=None):
            self.inhalt = inhalt
            self.naechster = naechster

    def __init__(self):
        self.anfang: Stapel.Knoten | None = None
        self.hoehe = 0

    def push(self, daten):
        """legt ein neues Element auf den Stapel"""
        neuer_knoten = Stapel.Knoten(daten, self.anfang)
        self.anfang = neuer_knoten
        self.hoehe += 1

    def pop(self):
        """entfernt das oberste Element vom Stapel und gibt es zurück"""
        if self.anfang is None:
            raise IndexError("Pop-Operation auf leerem Stapel nicht möglich")
        inhalt = self.anfang.inhalt
        self.anfang = self.anfang.naechster
        self.hoehe -= 1
        return inhalt

    def top(self):
        """gibt das oberste Element des Stapels zurück, ohne es zu entfernen"""
        if self.anfang is None:
            raise IndexError("Top-Operation auf leerem Stapel nicht möglich")
        return self.anfang.inhalt

    def ist_leer(self):
        """gibt True zurück, wenn der Stapel leer ist, sonst False"""
        return self.anfang is None

    def anzahl_elemente(self):
        """gibt die Anzahl der Elemente auf dem Stapel zurück"""
        return self.hoehe


##############################################################################


class Warteschlange:

    class Knoten:
        def __init__(self, inhalt, naechster=None):
            self.inhalt = inhalt
            self.naechster = naechster

    def __init__(self):
        self.kopf: Warteschlange.Knoten | None = None
        self.ende: Warteschlange.Knoten | None = None
        self.hoehe = 0

    def enqueue(self, daten):
        """fügt ein neues Element in die Warteschlange ein"""
        neuer_knoten = Warteschlange.Knoten(daten, None)
        if self.kopf is None:
            self.kopf = neuer_knoten
        else:
            self.ende.naechster = neuer_knoten
        self.ende = neuer_knoten
        self.hoehe += 1

    def dequeue(self):
        """entfernt das vorderste Element aus der Warteschlange und gibt es zurück"""
        if self.kopf is None:
            raise IndexError("Dequeue-Operation auf leerer Warteschlange nicht möglich")
        inhalt = self.kopf.inhalt
        self.kopf = self.kopf.naechster
        if self.kopf is None:
            self.ende = None
        self.hoehe -= 1
        return inhalt

    def ist_leer(self):
        """gibt True zurück, wenn die Warterschlange leer ist, sonst False"""
        return self.kopf is None

    def anzahl_elemente(self):
        """gibt die Anzahl der Elemente in der Warteschlange zurück"""
        return self.hoehe


##############################################################################


if __name__ == "__main__":
    # Test
    print("Tests für Warteschlange")
    q = Warteschlange()
    print("Leere Warteschlange ist leer:", q.ist_leer())
    print("Anna, Berta und Cora stellen sich nacheinander an")
    q.enqueue("Anna")
    q.enqueue("Berta")
    q.enqueue("Cora")
    print("Länge der Warteschlange:", q.anzahl_elemente())
    erste = q.dequeue()
    print("Die erste Kundin wird bedient:", erste)
    print("Länge der Warteschlange:", q.anzahl_elemente())
    print("Die zweite Kundin wird bedient:", q.dequeue())
    print("Dora stellt sich an")
    q.enqueue("Dora")
    print("Länge der Warteschlange:", q.anzahl_elemente())
    weitere = ["Ella", "Frieda", "Greta"]
    print("Weitere Kundinnen stellen sich an:", weitere)
    for kundin in weitere:
        q.enqueue(kundin)
    print("Länge der Warteschlange:", q.anzahl_elemente())
    print("Alle verbleibenden Kundinnen werden bedient:")
    while not q.ist_leer():
        print(q.dequeue())
    print("Länge der Warteschlange:", q.anzahl_elemente())
