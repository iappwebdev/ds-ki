import random
import logging

# Konfiguration für das Logging
logging.basicConfig(format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)
# logging.INFO:  Informationen über den Verlauf des Programms
# logging.DEBUG: Detaillierte Informationen für die Fehlersuche
logger.setLevel(logging.INFO)

class Datenpunkt:
    """Klasse zur Darstellung eines Datenpunktes im 2D-Raum."""
    def __init__(self, x: float, y: float) -> None:
        """Initialisiert einen Datenpunkt mit den gegebenen Koordinaten."""
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __eq__(self, anderer_datenpunkt: object) -> bool:
        """Vergleicht zwei Datenpunkte basierend auf ihren Koordinaten."""
        if isinstance(anderer_datenpunkt, Datenpunkt):
            return self.x == anderer_datenpunkt.x and self.y == anderer_datenpunkt.y
        return False
    
    def __hash__(self) -> int:
        """Berechnet den Hashwert eines Datenpunktes."""
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        """Gibt eine lesbare Repräsentation eines Datenpunktes zurück."""
        return f"Datenpunkt({self.x}, {self.y})"
    
    def berechne_distanz(self, anderer_datenpunkt: 'Datenpunkt') -> float:
        """Berechne die euklidische Distanz zu einem anderen Datenpunkt.  
           Return: Euklidische Distanz zwischen zwei Datenpunkten.  
           Z.B: 2.5"""
        diff_x = (self.x - anderer_datenpunkt.x) ** 2
        diff_y = (self.y - anderer_datenpunkt.y) ** 2
        distanz = (diff_x + diff_y) ** 0.5
        return round(distanz, 2)

# Setze den Zufallsgenerator auf einen fixen Wert für reproduzierbare Ergebnisse
random.seed(42)

def generiere_datenpunkte(anzahl_datenpunkte: int, zahlenraum: int = 10) -> list[Datenpunkt]:
    """Generiert eine Liste von zufälligen Datenpunkten im angegebenen Zahlenraum.  
       Return: Liste der generierten Datenpunkte.  
       Z.B: [Datenpunkt(1.4, 2.3), Datenpunkt(3.1, 4.5), Datenpunkt(5.7, 6.2)]"""
    datenpunkte = set()
    while len(datenpunkte) < anzahl_datenpunkte:
        x = random.uniform(0, zahlenraum)
        y = random.uniform(0, zahlenraum)
        datenpunkt = Datenpunkt(x, y)
        datenpunkte.add(datenpunkt)
    logger.info(f"Generierte Datenpunkte im {zahlenraum}x{zahlenraum} Zahlenraum: {datenpunkte}")
    return list(datenpunkte)

def initialisiere_zentroiden(anzahl_zentroiden: int, datenpunkte: list[Datenpunkt]) -> list[Datenpunkt]:
    """Wählt zufällig die angegebene Anzahl von Zentroiden aus den Datenpunkten aus.  
       Return: Liste der initialisierten Zentroiden.  
       Z.B: [Datenpunkt(1.4, 4.5), Datenpunkt(5.2, 8.3), Datenpunkt(3.1, 9.2)]"""
    zentroiden = random.sample(datenpunkte, anzahl_zentroiden)
    logger.info(f"Initialisierte Zentroiden: {zentroiden}")
    return zentroiden

def erzeuge_cluster(datenpunkte: list[Datenpunkt], zentroiden: list[Datenpunkt]) -> dict[int, list[Datenpunkt]]:
    """Weist jeden Datenpunkt den entsprechenden Cluster zu.  
       Return: Dictionary mit den Clustern und den zugehörigen Datenpunkten.
       Z.B: {0: [Datenpunkt(1.4, 4.5), Datenpunkt(1.6, 4.7)], 1: [Datenpunkt(5.2, 8.3), Datenpunkt(5.1, 8.2)], 2: [Datenpunkt(3.1, 9.2)]}"""
    clusters: dict[int, list[Datenpunkt]] = {}
    for zentroid in range(len(zentroiden)):
        clusters[zentroid] = []

    for datenpunkt in datenpunkte:
        index_naechster_zentroid = finde_naechsten_zentroiden(zentroiden, datenpunkt)
        clusters[index_naechster_zentroid].append(datenpunkt)
        logger.debug(f"{datenpunkt} wurde Zentroid {index_naechster_zentroid} zugewiesen")
    logger.info(f"Zuweisungen der Datenpunkte zu Zentroiden: {clusters}")
    return clusters

def finde_naechsten_zentroiden(zentroiden: list[Datenpunkt], datenpunkt: Datenpunkt) -> int:
    """Finde den nächsten Zentroiden für einen gegebenen Datenpunkt.  
       Return: Index (!) des nächsten Zentroiden.  
       Z.B: 2 bedeutet, dass der dritte (!) Zentroid der nächstgelegene für den Datenpunkt ist."""
    geringste_distanz = float('inf')
    naechster_zentroid: int
    for i in range(len(zentroiden)):
        distanz = datenpunkt.berechne_distanz(zentroiden[i])
        logger.debug(f"Distanz von {datenpunkt} zu Zentroid {i} ({zentroiden[i]}): {distanz}")
        if distanz < geringste_distanz:
            geringste_distanz = distanz
            naechster_zentroid = i
    logger.debug(f"Nächster Zentroid für {datenpunkt} ist Zentroid {naechster_zentroid}")
    return naechster_zentroid

def berechne_zentroid_koordinaten(datenpunkte: list[Datenpunkt]) -> Datenpunkt:
    """Berechnet die Position des Zentroiden basierend auf den zugehörigen Datenpunkten.  
       Return: Position des Zentroiden als Datenpunkt.  
       Z.B: Datenpunkt(2.5, 3.7)"""
    logger.debug(f"Berechne Zentroid für Datenpunkte: {datenpunkte}")
    summe_x = sum(datenpunkt.x for datenpunkt in datenpunkte)
    summe_y = sum(datenpunkt.y for datenpunkt in datenpunkte)
    position_x = summe_x / len(datenpunkte)
    position_y = summe_y / len(datenpunkte)
    return Datenpunkt(position_x, position_y)

def aktualisiere_zentroiden(clusters: dict[int, list[Datenpunkt]]) -> list[Datenpunkt]:
    """Aktualisiert die Zentroiden basierend auf den zugewiesenen Datenpunkten.  
       Return: Liste der aktualisierten Zentroiden.  
       Z.B: [Datenpunkt(1.4, 4.5), Datenpunkt(5.2, 8.3), Datenpunkt(3.1, 9.2)]"""
    neue_zentroiden: list[Datenpunkt] = []
    logger.debug(f"Berechne Zentroiden basierend auf den Clustern: {clusters}")
    for datenpunkte_in_cluster in clusters.values():
        neuer_zentroid: Datenpunkt = berechne_zentroid_koordinaten(datenpunkte_in_cluster)
        neue_zentroiden.append(neuer_zentroid)
    logger.info(f"Aktualisierte Zentroiden: {neue_zentroiden}")
    return neue_zentroiden

def k_means(datenpunkte: list[Datenpunkt], anzahl_cluster: int, max_iterationen: int) -> None:
    """Hauptfunktion für den k-means Algorithmus. Führt den k-means Clustering Algorithmus aus."""
    # 2. Initialisierung der Zentroiden
    zentroiden = initialisiere_zentroiden(anzahl_cluster, datenpunkte)

    for iteration in range(max_iterationen):
        logger.info(f"Iteration {iteration + 1}")
        # 3. Zuweisung der Datenpunkte und Bildung der Cluster
        clusters = erzeuge_cluster(datenpunkte, zentroiden)
        
        # 4. Aktualisierung der Zentroiden
        neue_zentroiden = aktualisiere_zentroiden(clusters)
        
        # 5. Überprüfung, ob sich die Zentroiden verändert haben
        if neue_zentroiden == zentroiden:
            logger.info("Zentroiden haben sich nicht mehr verändert. Algorithmus stoppt.")
            break
        zentroiden = neue_zentroiden
    logger.info(f"Endgültige Zentroiden: {zentroiden}")

# Starte den k-means Algorithmus mit 100 Datenpunkten, 3 Zentroiden und maximal 10 Iterationen
datenpunkte = generiere_datenpunkte(100, zahlenraum=10)
k_means(datenpunkte=datenpunkte, anzahl_cluster=3, max_iterationen=100)

# datenpunkte_100 = generiere_datenpunkte(100, zahlenraum=100)
# k_means(datenpunkte=datenpunkte_100, anzahl_cluster=3, max_iterationen=10)
