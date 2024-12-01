import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Generierung von zufälligen Datenpunkten für drei Cluster mit weiter auseinanderliegenden Verteilungen (Plot 1 und 2)
np.random.seed(42)
cluster_1 = np.random.normal(loc=[2, 2], scale=0.5, size=(20, 2))  # Kleinere Standardabweichung für weiter entfernte Cluster
cluster_2 = np.random.normal(loc=[6, 6], scale=0.5, size=(20, 2))
cluster_3 = np.random.normal(loc=[2, 8], scale=0.5, size=(20, 2))
data_1 = np.vstack((cluster_1, cluster_2, cluster_3))

# --- Plot 1: Rohdaten in Schwarz ohne Clustering (einfache Unterscheidung) ---
plt.figure(figsize=(8, 6))
plt.scatter(data_1[:, 0], data_1[:, 1], s=5, color='black')
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)
plt.savefig("images/kmeans_3_cluster_einfach_datenpunkte.svg")
plt.show()

# KMeans Clustering für die ersten Datenpunkte (einfache Unterscheidung)
kmeans_1 = KMeans(n_clusters=3, random_state=42)
kmeans_1.fit(data_1)
labels_1 = kmeans_1.labels_
centroids_1 = kmeans_1.cluster_centers_

# Farben für die Cluster definieren
colors = ['blue', 'green', 'red']

# --- Plot 2: Ergebnis des K-Means-Clustering (einfache Unterscheidung) ---
plt.figure(figsize=(8, 6))

# Plotten der Datenpunkte entsprechend ihrer Clusterzugehörigkeit mit der jeweiligen Clusterfarbe
scatterpoints = []
for i, color in enumerate(colors):
    cluster_data = data_1[labels_1 == i]
    scatter = plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=5, color=color, label=f'Cluster {i + 1}')
    scatterpoints.append(scatter)

# Plotten der Zentroiden ohne diese in der Legende zu zeigen
for i, centroid in enumerate(centroids_1):
    plt.scatter(centroid[0], centroid[1], s=200, color=colors[i], marker='x', linewidth=2)

# Labels hinzufügen
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)

# Legende mit größeren Punkten
plt.legend(handles=scatterpoints, scatterpoints=True, markerscale=3)
plt.savefig("images/kmeans_3_cluster_einfach_ergebnis.svg")
plt.show()

# Generierung von zufälligen Datenpunkten für drei Cluster, die enger beieinander liegen (Plot 3 und 4)
cluster_1 = np.random.normal(loc=[3, 3], scale=1.5, size=(20, 2))  # Höhere Standardabweichung für mehr Überlappung
cluster_2 = np.random.normal(loc=[4, 4], scale=1.5, size=(20, 2))
cluster_3 = np.random.normal(loc=[3.5, 5], scale=1.5, size=(20, 2))

data_2 = np.vstack((cluster_1, cluster_2, cluster_3))

# --- Plot 3: Rohdaten in Schwarz ohne Clustering (schwierigere Unterscheidung) ---
plt.figure(figsize=(8, 6))
plt.scatter(data_2[:, 0], data_2[:, 1], s=5, color='black')
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)
plt.savefig("images/kmeans_3_cluster_komplex_datenpunkte.svg")
plt.show()

# KMeans Clustering für die zweiten Datenpunkte (schwierigere Unterscheidung)
kmeans_2 = KMeans(n_clusters=3, random_state=42)
kmeans_2.fit(data_2)
labels_2 = kmeans_2.labels_
centroids_2 = kmeans_2.cluster_centers_

# --- Plot 4: Ergebnis des K-Means-Clustering (schwierigere Unterscheidung) ---
plt.figure(figsize=(8, 6))

# Plotten der Datenpunkte entsprechend ihrer Clusterzugehörigkeit mit der jeweiligen Clusterfarbe
scatterpoints = []
for i, color in enumerate(colors):
    cluster_data = data_2[labels_2 == i]
    scatter = plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=5, color=color, label=f'Cluster {i + 1}')
    scatterpoints.append(scatter)

# Plotten der Zentroiden ohne diese in der Legende zu zeigen
for i, centroid in enumerate(centroids_2):
    plt.scatter(centroid[0], centroid[1], s=200, color=colors[i], marker='x', linewidth=2)

# Labels hinzufügen
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)

# Legende mit größeren Punkten
plt.legend(handles=scatterpoints, scatterpoints=True, markerscale=3)
plt.savefig("images/kmeans_3_cluster_komplex_ergebnis.svg")
plt.show()
