from __future__ import annotations


class Knoten[Typ]:  # ab Python 3.12 ist diese Schreibweise für generische Typen möglich

    def __init__(self, inhalt: Typ) -> None:
        self.__inhalt: Typ = inhalt
        self.__linkerKnoten: Knoten[Typ] | None = None
        self.__rechterKnoten: Knoten[Typ] | None = None

    def istBlatt(self) -> bool:
        return self.__linkerKnoten == None and self.__rechterKnoten == None

    def gibInhalt(self) -> Typ:
        return self.__inhalt

    def setzeInhalt(self, pInhalt: Typ) -> None:
        self.__inhalt = pInhalt

    def gibLinkenKnoten(self) -> Knoten[Typ] | None:
        return self.__linkerKnoten

    def setzeLinkenKnoten(self, pLinkerKnoten: Knoten[Typ]) -> None:
        self.__linkerKnoten = pLinkerKnoten

    def gibRechtenKnoten(self) -> Knoten[Typ] | None:
        return self.__rechterKnoten

    def setzeRechtenKnoten(self, pRechterKnoten: Knoten[Typ]) -> None:
        self.__rechterKnoten = pRechterKnoten


class Binaerbaum[Typ]:
    def __init__(self) -> None:
        self.__wurzel: Knoten[Typ] | None = None

    def gibWurzel(self) -> Knoten[Typ] | None:
        return self.__wurzel

    def setzeWurzel(self, pWurzel: Knoten[Typ]) -> None:
        self.__wurzel = pWurzel

    def istLeer(self) -> bool:
        return self.__wurzel == None

    def anzahlKnoten(self) -> int:
        # Dies ist die öffentliche Methode zur Ermittlung der Anzahl der Knoten im Baum.
        # Die eigentliche Arbeit wird von der privaten Methode __anzahlKnotenRekursiv erledigt.
        return self.__anzahlKnotenRekursiv(self.__wurzel)

    def __anzahlKnotenRekursiv(self, knoten: Knoten[Typ] | None) -> int:
        # private Hilfsmethode, die die Anzahl der Knoten im Baum rekursiv ermittelt.
        # Sie entspricht fast 1:1 der Funktion anzahl_knoten_binaerbaum aus von weiter oben.
        if knoten == None:
            return 0
        else:
            anzahlLinks = self.__anzahlKnotenRekursiv(knoten.gibLinkenKnoten())
            anzahlRechts = self.__anzahlKnotenRekursiv(knoten.gibRechtenKnoten())
            return 1 + anzahlLinks + anzahlRechts

    def anzahlBlaetter(self) -> int:
        # Diese Methode gibt die Anzahl der Blattknoten im Baum zurück.
        # Auch hier wird die eigentliche Arbeit von einer privaten Methode erledigt.
        return self.__anzahlBlaetterRekursiv(self.__wurzel)

    def __anzahlBlaetterRekursiv(self, knoten: Knoten[Typ] | None) -> int:
        # private Hilfsmethode, die die Anzahl der Blattknoten im Baum rekursiv ermittelt
        if knoten == None:
            return 0
        if knoten.istBlatt():
            return 1
        else:
            anzahlLinks = self.__anzahlBlaetterRekursiv(knoten.gibLinkenKnoten())
            anzahlRechts = self.__anzahlBlaetterRekursiv(knoten.gibRechtenKnoten())
            return anzahlLinks + anzahlRechts

    def tiefe(self) -> int:
        # Selbes Spiel wie oben: Die eigentliche Arbeit wird von einer privaten Methode erledigt.
        return self.__tiefeRekursiv(self.__wurzel)

    def __tiefeRekursiv(self, knoten: Knoten[Typ] | None) -> int:
        if knoten == None:
            return -1  # Die Tiefe eines leeren Baums ist -1; die der Wurzel ist 0‚
        else:
            tiefeLinks = self.__tiefeRekursiv(knoten.gibLinkenKnoten())
            tiefeRechts = self.__tiefeRekursiv(knoten.gibRechtenKnoten())
            return 1 + max(tiefeLinks, tiefeRechts)

    def enthaeltElement(self, gesuchterWert: Typ) -> bool:
        # Auch hier wird die eigentliche Arbeit von einer privaten Methode erledigt.
        return self.__enthaeltElementRekursiv(self.__wurzel, gesuchterWert)

    def __enthaeltElementRekursiv(
        self, knoten: Knoten[Typ] | None, gesuchterWert: Typ
    ) -> bool:
        # private Hilfsmethode, die prüft, ob ein bestimmtes Element im Baum enthalten ist
        if knoten == None:
            return False
        if knoten.gibInhalt() == gesuchterWert:
            return True
        linksGefunden = self.__enthaeltElementRekursiv(
            knoten.gibLinkenKnoten(), gesuchterWert
        )
        rechtsGefunden = self.__enthaeltElementRekursiv(
            knoten.gibRechtenKnoten(), gesuchterWert
        )
        if linksGefunden == True or rechtsGefunden == True:
            return True
        return False


##############################################################################


def main() -> None:
    print("Binärbaum zum Speichern von Integer-Werten anlegen:")
    baum = Binaerbaum[int]()  # Erzeugen eines leeren Baums, der Integer-Werte speichert
    print("Ist der Baum leer?", baum.istLeer())  # Erwartet: True
    print("Anzahl der Knoten im leeren Baum:", baum.anzahlKnoten())  # Erwartet: 0

    k1: Knoten[int] = Knoten(1)
    k2: Knoten[int] = Knoten(2)
    k3: Knoten[int] = Knoten(3)
    k4: Knoten[int] = Knoten(4)
    k5: Knoten[int] = Knoten(5)
    k6: Knoten[int] = Knoten(6)
    k7: Knoten[int] = Knoten(7)

    print("Wir fügen die Knoten 1 bis 7 ein.")
    baum.setzeWurzel(k1)
    k1.setzeLinkenKnoten(k2)
    k1.setzeRechtenKnoten(k3)
    k2.setzeLinkenKnoten(k4)
    k2.setzeRechtenKnoten(k5)
    k3.setzeLinkenKnoten(k6)
    k3.setzeRechtenKnoten(k7)

    anzahlKnoten = baum.anzahlKnoten()
    print(f"Anzahl der Knoten ist jetzt: {anzahlKnoten}")  # Erwartet: 7

    anzahlBlätter = baum.anzahlBlaetter()
    print(f"Anzahl der Blattknoten ist: {anzahlBlätter}")  # Erwartet: 4

    tiefe = baum.tiefe()  # Erwartet: 3
    print(f"Die Tiefe des Baums ist: {tiefe}")

    print("Enthält der Baum die Zahl 3?", baum.enthaeltElement(3))  # Erwartet: True
    print("Enthält der Baum die Zahl 8?", baum.enthaeltElement(8))  # Erwartet: False

    def anzahl_knoten(knoten: Knoten[int] | None) -> int:
        if knoten is None:
            return 0
        else:
            anzahl_links = anzahl_knoten(knoten.gibLinkenKnoten())
            anzahl_rechts = anzahl_knoten(knoten.gibRechtenKnoten())
            return 1 + anzahl_links + anzahl_rechts

    zahl: int = anzahl_knoten(baum.gibWurzel())
    print(f"Anzahl der Knoten im Baum: {zahl}")


if __name__ == "__main__":
    main()
