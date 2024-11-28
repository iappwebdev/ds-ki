import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from imojify import imojify

# Funktion für Emojis hinzufügen (wie oben)
def add_image(emoji_path, x, y, zoom=0.05):
    img = plt.imread(emoji_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, (x, y), frameon=False, zorder=2)
    plt.gca().add_artist(ab)

# Daten vorbereiten
data = np.array([
    [85, 10],  # Apfel
    [83, 10],  # Birne
    [75, 12],  # Banane
    [87, 8],   # Orange
    [81, 16],  # Weintrauben
    [91, 5],   # Erdbeere
    [92, 6],   # Wassermelone
    [83, 14],  # Mango
    [78, 9],   # Kiwi
    [88, 7],   # Pfirsich
    [82, 15],  # Ananas
])

emoji_map = [
    "🍎", "🍐", "🍌", "🍊", "🍇", "🍓", "🍉", "🥭", "🥝", "🍑", "🍍"
]

# Diagramm nur mit Obstsorten
plt.figure(figsize=(8, 6))
plt.title("Obstsorten vor Clustering")
plt.xlabel("Wassergehalt (%)")
plt.ylabel("Fruchtzuckergehalt (g/100g)")
plt.grid(True)

# Originalpunkte unter Emojis ausblenden
plt.scatter(data[:, 0], data[:, 1], color="black", edgecolor="none", s=50, zorder=3)

# Emojis plotten
for i, point in enumerate(data):
    emoji_path = imojify.get_img_path(emoji_map[i])
    add_image(emoji_path, point[0], point[1])

plt.legend()
plt.show()

k = 3  # Anzahl der Cluster
max_iter = 10

# Initialisiere zufällige Zentroiden
# np.random.seed(99) # 5 Iterationen
np.random.seed(60) # 3 Interation
centroids = data[np.random.choice(data.shape[0], k, replace=False)]

# Iterationen
for iteration in range(max_iter):
    # Clusterzuordnung
    distances = np.linalg.norm(data[:, None, :] - centroids[None, :, :], axis=2)
    clusters = np.argmin(distances, axis=1)

    # Visualisierung
    plt.figure(figsize=(8, 6))
    plt.title(f"Iteration {iteration + 1}")
    plt.xlabel("Wassergehalt (%)")
    plt.ylabel("Fruchtzuckergehalt (g/100g)")
    plt.grid(True)

        # Plot Datenpunkte und Emojis
    colors = ['r', 'g', 'b']  # Farben für die Cluster
    for cluster_idx in range(k):
        cluster_points = data[clusters == cluster_idx]
        # Datenpunkte in der Clusterfarbe
        plt.scatter(cluster_points[:, 0], cluster_points[:, 1],
                    color=colors[cluster_idx], s=50, zorder=3, label=f"Cluster {cluster_idx + 1}")

    # Emojis hinzufügen
    for i, point in enumerate(data):
        emoji_path = imojify.get_img_path(emoji_map[i])
        add_image(emoji_path, point[0], point[1])

    # Zentroiden zeichnen
    for cluster_index, centroid in enumerate(centroids):
        plt.scatter(centroid[0], centroid[1], c=[colors[cluster_index]],
                    marker='X', s=300, linewidths=1, zorder=6)

    for i, (x, y) in enumerate(centroids):
      plt.figtext(0.15, 0.25 - i * 0.05, f"Centroid {i + 1}: {x:.2f}, {y:.2f}", ha="left", 
                  fontsize=10, color=colors[i], bbox={"facecolor": "lightgrey", "alpha": 0.7, "pad": 5})
      
    plt.legend()
    plt.show()

    # Zentroiden aktualisieren
    new_centroids = np.array([
        data[clusters == cluster_idx].mean(axis=0) if np.any(clusters == cluster_idx) else centroids[cluster_idx]
        for cluster_idx in range(k)
    ])

    # Abbruchbedingung
    if np.allclose(new_centroids, centroids):
        print(f"Konvergenz nach {iteration + 1} Iterationen erreicht.")
        break

    centroids = new_centroids
