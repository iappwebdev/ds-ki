class Suchproblem:
    """Abstrakte Klasse für allgemeine Suchprobleme.
    Konkrete Problemklassen werden von dieser Klasse abgeleitet und überschreiben
    die Methoden moegliche_aktionen() und fuehre_aktion_aus(), evtl. auch
    ist_zielzustand(). """

    def __init__(self, startzustand, zielzustand=None):
        """erzeugt ein neues Suchproblem mit festem Startzustand.
        Falls kein Zielzustand vorgegeben wird, muss die Methode
        ist_zielzustand() überschrieben werden."""
        self.startzustand = startzustand
        self.zielzustand = zielzustand

    def moegliche_aktionen(self, zustand):
        """liefert alle in zustand möglichen Aktionen zurück."""
        pass

    def fuehre_aktion_aus(self, zustand, aktion):
        """wendet aktion in zustand an und gibt den daraus resultierenden
        neuen Zustand zurück. """
        pass

    def ist_zielzustand(self, zustand):
        """prüft, ob der übergebene Zustand die Zielbedingung erfüllt.
        Standardverhalten: Es gibt genau einen Zielzustand self.ziel_zustand,
        mit dem zustand verglichen wird.
        Unterklassen von Suchproblem können diese Methode überschreiben und so
        andere Zieltests implementieren. """

        return zustand == self.zielzustand


class Knoten:
    """Ein Knoten in einem Suchbaum. Der Knoten speichert Referenzen auf
    den gespeicherten Zustand sowie den Vorgängerknoten und die Aktion, aus denen
    dieser Zustand entstanden ist."""

    naechste_nummer = 0  # Klassenvariable, dient dazu eindeutige Nummern an Knoten zu vergeben 

    def __init__(self, zustand, vorgaenger=None, aktion=None):
        """erzeugt einen neuen Suchknoten und setzt dabei Referenzen auf
        Vorgängerknoten und die gerade ausgeführte Aktion.
        Um später nachvollziehen zu können, in welcher Reihenfolge die Knoten erzeugt wurden,
        werden sie aufsteigend durchnummeriert."""
        self.zustand = zustand
        self.vorgaenger = vorgaenger
        self.aktion = aktion
        self.nummer = Knoten.naechste_nummer
        Knoten.naechste_nummer += 1

    def pfad_hierher(self):
        """verfolgt den Pfad von hier rückwärts bis zum Wurzelknoten und liefert die Liste
        der Aktionen zurück, die in den jetzigen Zustand geführt haben."""
        pfad = []
        knoten = self  # Gehe von diesem Knoten aus...
        while knoten.vorgaenger:  # ...solange noch nicht beim Wurzelknoten...
            pfad.append(knoten.aktion)
            knoten = knoten.vorgaenger  # ...rückwärts...
        pfad.reverse()  # Fertigen Pfad umdrehen, dadurch vom Start ausführbar
        return pfad

    def folgeknoten(self, problem, aktion):
        """wendet eine Aktion im aktuellen Zustand an und verpackt den resultierenden
        Zustand in einen neuen Knoten mit korrekt gesetztem Vorgänger usw."""
        zustand_neu = problem.fuehre_aktion_aus(self.zustand, aktion)
        knoten_neu = Knoten(zustand_neu, vorgaenger=self, aktion=aktion)
        return knoten_neu

    def expandiere(self, problem):
        """liefert alle von diesem Knoten direkt erreichbaren Folgeknoten"""
        return [self.folgeknoten(problem, aktion)
                for aktion in problem.moegliche_aktionen(self.zustand)]



def breitensuche(problem):
    """durchsucht den Baum, so dass Knoten mit niedriger Suchtiefe zuerst untersucht werden"""
    grenze = [Knoten(problem.startzustand)]  # Warteschlange mit dem Startknoten initialisieren

    while grenze:  # Solange noch Knoten in der Warteschlange sind...
        aktuell = grenze.pop(0)  # Hole den vordersten Knoten aus der OL
        if problem.ist_zielzustand(aktuell.zustand):    # Bin ich am Ziel?
            return aktuell.pfad_hierher()
        folge_knoten = aktuell.expandiere(problem)
        grenze.extend(folge_knoten)   # Folgezustände ans Ende der Schlange einfügen
    return None  # keine Lösung gefunden


def breitensuche_graph(problem):
    """durchsucht den Baum, so dass Knoten mit niedriger Suchtiefe zuerst untersucht werden"""
    untersucht = set()  # Zustände, die wir schon einmal besucht haben. Zu Anfang: leere Menge.
    grenze = [Knoten(problem.startzustand)]

    while grenze:
        knoten = grenze.pop(0)
        untersucht.add(knoten.zustand)   # Knoten wird nicht noch einmal untersucht werden
        if problem.ist_zielzustand(knoten.zustand):
            return knoten.pfad_hierher()
        folge_knoten = knoten.expandiere(problem)
        neue_knoten = [k for k in folge_knoten        # NEU: betrachte nur unbekannte Knoten
                       if k.zustand not in untersucht and k.zustand not in grenze]
        grenze.extend(neue_knoten)
    return None



##############################################

import schiebepuzzle


class Schiebepuzzle(Suchproblem):

    def moegliche_aktionen(self, zustand):
        return schiebepuzzle.moegliche_zuege(zustand)

    def fuehre_aktion_aus(self, zustand, aktion):
        return schiebepuzzle.verschiebe_pos(zustand, aktion)


if __name__ == "__main__":
    start = 'D CGABEHF'
    ziel = 'ABCDEFGH '

    problem = Schiebepuzzle(start, ziel)
    loesung = breitensuche_graph(problem)
    print(loesung, len(loesung))
    print("Startzustand war:", start)
    #schiebepuzzle.zugsequenz_ausfuehren(problem.startzustand, loesung, anzeigen=True)
