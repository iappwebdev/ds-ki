import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# Datenpunkte
points = np.array([
    [2, 10],
    [2, 5],
    [8, 4],
    [5, 8],
    [7, 5],
    [6, 4],
    [1, 2],
    [4, 9],
    [6, 2],
    [3, 3],
    [5, 6],
    [9, 7]
])

# Anzahl der Cluster
k = 3

# Initiale Centroids
centroids = np.array([
    [2, 10],  # Centroid A
    [5, 8],   # Centroid B
    [1, 2]    # Centroid C
])

# Farben für die Cluster
colors = ['r', 'b', 'g', 'c', 'm', 'y', 'k']

# Initialer Plot der Datenpunkte
plt.figure(figsize=(8, 6))
plt.scatter(points[:, 0], points[:, 1], c='gray', label='Datenpunkte')
plt.title('Initiale Datenpunkte')
plt.xlabel('X-Wert')
plt.ylabel('Y-Wert')
plt.legend()
plt.grid(True)
plt.show()

# Funktion zur Berechnung der Manhattan-Distanz
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

# Speichert die Historie der Centroids und Clusterzuweisungen
centroid_history = [centroids.copy()]
cluster_history = []

# K-Means-Algorithmus mit Manhattan-Distanz
for iteration in range(10):  # Maximal 10 Iterationen
    clusters = {}
    for idx in range(k):
        clusters[idx] = []
    
    # Zuweisung der Punkte zu den nächstgelegenen Centroids
    for point in points:
        distances = [manhattan_distance(point, centroid) for centroid in centroids]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)
    
    cluster_history.append(deepcopy(clusters))
    
    # Speichern der aktuellen Centroids zum Vergleich
    prev_centroids = centroids.copy()
    
    # Aktualisierung der Centroids
    for idx in range(k):
        if clusters[idx]:  # Vermeidung von Division durch Null
            centroids[idx] = np.mean(clusters[idx], axis=0)
    
    centroid_history.append(centroids.copy())
    
    # Überprüfen auf Konvergenz
    if np.allclose(prev_centroids, centroids):
        print(f"Algorithmus konvergierte nach {iteration+1} Iterationen.")
        break

# Plotten der Ergebnisse
for i in range(len(cluster_history)):
    plt.figure(figsize=(8, 6))
    for idx in range(k):
        cluster_points = np.array(cluster_history[i][idx])
        if cluster_points.size > 0:
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[idx], label=f'Cluster {idx+1}')
            # Plot der Centroids in der gleichen Farbe wie das Cluster
            centroid = centroid_history[i][idx]
            plt.scatter(centroid[0], centroid[1], c=colors[idx], marker='X', s=100)
    plt.title(f'Iteration {i+1}')
    plt.xlabel('X-Wert')
    plt.ylabel('Y-Wert')
    plt.legend()
    plt.grid(True)
    plt.show()
