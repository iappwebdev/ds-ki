import numpy as np
import matplotlib.pyplot as plt
from copy import deepcopy

# Datenpunkte und Namen
points = np.array([
    [2, 10], [2, 5], [8, 4], [5, 8], [7, 5],
    [6, 4], [1, 2], [4, 9], [6, 2], [3, 3],
    [5, 6], [9, 7]
])
point_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']

# Anzahl der Cluster
k = 3

# Initiale Centroids
centroids = np.array([
    [2, 10],  # Centroid A
    [5, 8],   # Centroid B
    [1, 2]    # Centroid C
])

# Farben für die Cluster
colors = ['r', 'b', 'g']

# Funktion zur Berechnung der Manhattan-Distanz
def manhattan_distance(a, b):
    return np.sum(np.abs(a - b))

# Visualisierung der Punkte und Cluster
def plot_clusters(iteration, clusters, centroids, show_initial=False):
    plt.figure(figsize=(8, 6))
    
    # Plot der Ausgangsdatenpunkte
    if show_initial:
        for idx, point in enumerate(points):
            plt.scatter(point[0], point[1], c='gray', label='Ausgangsdaten' if idx == 0 else "")
            plt.text(point[0] + 0.2, point[1], point_names[idx], fontsize=9, color='gray')
    
    # Plot der Cluster und Zentroiden
    for idx in range(k):
        cluster_points = np.array(clusters[idx])
        if cluster_points.size > 0:
            # Zentroidenkoordinaten in die Legende einfügen
            centroid_coords = f"({int(centroids[idx][0])}, {int(centroids[idx][1])})"
            plt.scatter(cluster_points[:, 0], cluster_points[:, 1], c=colors[idx], label=f'Cluster {idx+1} {centroid_coords}')
            
            # Punktnamen in die Cluster-Plotbeschriftung einfügen
            for cluster_point in cluster_points:
                point_idx = np.where((points == cluster_point).all(axis=1))[0][0]
                plt.text(cluster_point[0] + 0.2, cluster_point[1], point_names[point_idx], fontsize=9, color=colors[idx])
        
        # Plot der Zentroiden
        centroid = centroids[idx]
        plt.scatter(centroid[0], centroid[1], c=colors[idx], marker='X', s=100)
    
    plt.title(f'Iteration {iteration+1}')
    plt.xlabel('X-Wert')
    plt.ylabel('Y-Wert')
    plt.legend()
    plt.grid(True)
    
    # Speichern des Plots als Bild
    filename = f'cluster_plot_iteration_{iteration+1}.png'
    plt.savefig(filename, dpi=300, bbox_inches='tight')
    print(f"Plot für Iteration {iteration+1} gespeichert als {filename}")
    plt.close()  # Schließt die Figur, um Speicher zu sparen

# K-Means-Algorithmus mit Manhattan-Distanz
max_iterations = 10
centroid_history = [centroids.copy()]
cluster_history = []

# Initialer Plot der Ausgangsdatenpunkte
plot_clusters(0, {idx: [] for idx in range(k)}, centroids, show_initial=True)

for iteration in range(max_iterations):
    clusters = {idx: [] for idx in range(k)}
    
    # Zuweisung der Punkte zu den nächstgelegenen Centroids
    for idx, point in enumerate(points):
        distances = [manhattan_distance(point, centroid) for centroid in centroids]
        cluster_idx = np.argmin(distances)
        clusters[cluster_idx].append(point)
        print(f"Punkt {point_names[idx]} zu Cluster {cluster_idx+1} (Distanzen: {distances})")
    
    cluster_history.append(deepcopy(clusters))
    
    # Speichern der aktuellen Centroids zum Vergleich
    prev_centroids = centroids.copy()
    
    # Aktualisierung der Centroids (gerundet auf ganze Zahlen)
    for idx in range(k):
        if clusters[idx]:  # Vermeidung von Division durch Null
            centroids[idx] = np.round(np.mean(clusters[idx], axis=0))
    
    centroid_history.append(centroids.copy())
    
    # Debugging-Ausgabe
    print(f"Iteration {iteration+1}:")
    print(f"  Neue Zentroiden: {centroids}")
    for idx, cluster in clusters.items():
        cluster_points_names = [point_names[np.where((points == p).all(axis=1))[0][0]] for p in cluster]
        print(f"  Cluster {idx+1}: {cluster_points_names}")
    
    # Überprüfen auf Konvergenz
    if np.allclose(prev_centroids, centroids):
        print(f"Algorithmus konvergierte nach {iteration+1} Iterationen.")
        break
    
    # Plot der aktuellen Iteration
    plot_clusters(iteration, clusters, centroids)

# Abschließender Plot
print("Finale Zentroiden:")
print(centroids)
plot_clusters(iteration, clusters, centroids)
