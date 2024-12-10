import os
import numpy as np
from kmeans_module.kmeans_runner import run_kmeans

# Anzahl der Cluster
n_clusters = 3

# Maximale Iterationen
max_iter = 10

# Seed für Zufallszahlen
random_seed = 42

# Funktion zum Generieren der Daten
random_seed = 42

# Funktion zum Generieren der Daten
def generate_data(): 
    cluster_1 = np.random.normal(loc=[3, 3], scale=0.5, size=(20, 2))  # Kleinere Standardabweichung für weiter entfernte Cluster
    cluster_2 = np.random.normal(loc=[5, 5], scale=0.5, size=(20, 2))
    cluster_3 = np.random.normal(loc=[3, 7], scale=0.5, size=(20, 2))
    return np.vstack((cluster_1, cluster_2, cluster_3))

# --- AB HIER NICHTS MEHR ÄNDERN ---
# Daten generieren
np.random.seed(random_seed)
data = generate_data()

# K-Means ausführen
current_file_name = os.path.splitext(os.path.basename(__file__))[0]
gif_path = run_kmeans(data, n_clusters, max_iter, current_file_name, random_seed)

print(f"K-Means abgeschlossen. GIF erstellt: {gif_path}")
