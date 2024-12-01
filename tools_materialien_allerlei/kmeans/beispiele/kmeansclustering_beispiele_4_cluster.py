import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans

# Generierung von zufälligen Datenpunkten für vier Cluster mit klarer Trennung (Plot 1 und 2)
np.random.seed(42)
cluster_1 = np.random.normal(loc=[2, 2], scale=0.8, size=(25, 2))
cluster_2 = np.random.normal(loc=[7, 7], scale=0.8, size=(25, 2))
cluster_3 = np.random.normal(loc=[2, 8], scale=0.8, size=(25, 2))
cluster_4 = np.random.normal(loc=[8, 2], scale=0.8, size=(25, 2))

data_easy = np.vstack((cluster_1, cluster_2, cluster_3, cluster_4))

# --- Plot 1: Rohdaten in Schwarz ohne Clustering (leichte Unterscheidung) ---
plt.figure(figsize=(8, 6))
plt.scatter(data_easy[:, 0], data_easy[:, 1], s=5, color='black')
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)
plt.savefig("images/kmeans_4_cluster_einfach_datenpunkte.svg")
plt.show()

# KMeans Clustering für vier klar getrennte Cluster
kmeans_easy = KMeans(n_clusters=4, random_state=42)
kmeans_easy.fit(data_easy)
labels_easy = kmeans_easy.labels_
centroids_easy = kmeans_easy.cluster_centers_

# Farben für die Cluster definieren
colors = ['blue', 'green', 'red', 'orange']

# --- Plot 2: Ergebnis des K-Means-Clustering (leichte Unterscheidung) ---
plt.figure(figsize=(8, 6))

# Plotten der Datenpunkte entsprechend ihrer Clusterzugehörigkeit mit der jeweiligen Clusterfarbe
scatterpoints = []
for i, color in enumerate(colors):
    cluster_data = data_easy[labels_easy == i]
    scatter = plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=5, color=color, label=f'Cluster {i + 1}')
    scatterpoints.append(scatter)

# Plotten der Zentroiden ohne diese in der Legende zu zeigen
for i, centroid in enumerate(centroids_easy):
    plt.scatter(centroid[0], centroid[1], s=200, color=colors[i], marker='x', linewidth=2)

# Labels hinzufügen
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)

# Legende mit größeren Punkten
plt.legend(handles=scatterpoints, scatterpoints=True, markerscale=3)
plt.savefig("images/kmeans_4_cluster_einfach_ergebnis.svg")
plt.show()

# Generierung von zufälligen Datenpunkten für vier Cluster, die enger beieinander liegen (Plot 3 und 4)
cluster_1 = np.random.normal(loc=[4, 4], scale=1.5, size=(25, 2))
cluster_2 = np.random.normal(loc=[5, 5], scale=1.5, size=(25, 2))
cluster_3 = np.random.normal(loc=[4, 7], scale=1.5, size=(25, 2))
cluster_4 = np.random.normal(loc=[6, 3], scale=1.5, size=(25, 2))

data_hard = np.vstack((cluster_1, cluster_2, cluster_3, cluster_4))

# --- Plot 3: Rohdaten in Schwarz ohne Clustering (schwierige Unterscheidung) ---
plt.figure(figsize=(8, 6))
plt.scatter(data_hard[:, 0], data_hard[:, 1], s=5, color='black')
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)
plt.savefig("images/kmeans_4_cluster_komplex_datenpunkte.svg")
plt.show()

# KMeans Clustering für die enger zusammenliegenden Cluster
kmeans_hard = KMeans(n_clusters=4, random_state=42)
kmeans_hard.fit(data_hard)
labels_hard = kmeans_hard.labels_
centroids_hard = kmeans_hard.cluster_centers_

# --- Plot 4: Ergebnis des K-Means-Clustering (schwierige Unterscheidung) ---
plt.figure(figsize=(8, 6))

# Plotten der Datenpunkte entsprechend ihrer Clusterzugehörigkeit mit der jeweiligen Clusterfarbe
scatterpoints = []
for i, color in enumerate(colors):
    cluster_data = data_hard[labels_hard == i]
    scatter = plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=5, color=color, label=f'Cluster {i + 1}')
    scatterpoints.append(scatter)

# Plotten der Zentroiden ohne diese in der Legende zu zeigen
for i, centroid in enumerate(centroids_hard):
    plt.scatter(centroid[0], centroid[1], s=200, color=colors[i], marker='x', linewidth=2)

# Labels hinzufügen
plt.xlabel('Merkmal 1')
plt.ylabel('Merkmal 2')
plt.grid(True)

# Legende mit größeren Punkten
plt.legend(handles=scatterpoints, scatterpoints=True, markerscale=3)
plt.savefig("images/kmeans_4_cluster_komplex_ergebnis.svg")

plt.show()
