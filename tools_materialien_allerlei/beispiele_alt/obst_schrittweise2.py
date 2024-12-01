import random
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from imojify import imojify

# Funktion für Emojis hinzufügen
def add_image(emoji_path, x, y, zoom=0.05):
    img = plt.imread(emoji_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, (x, y), frameon=False, zorder=2)
    plt.gca().add_artist(ab)

# Manhattan-Distanz berechnen
def manhattan_distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

# Zentroiden aktualisieren
def calculate_new_centroids(data, clusters, k):
    centroids = []
    for cluster_idx in range(k):
        cluster_points = [data[i] for i in range(len(data)) if clusters[i] == cluster_idx]
        if cluster_points:
            avg_x = sum([p[0] for p in cluster_points]) / len(cluster_points)
            avg_y = sum([p[1] for p in cluster_points]) / len(cluster_points)
            centroids.append([avg_x, avg_y])
        else:
            centroids.append(None)  # Zentroid bleibt unverändert
    return centroids

# Daten vorbereiten
data = [
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
    [86, 11],  # Pflaume
]

emoji_map = [
    "🍎", "🍐", "🍌", "🍊", "🍇", "🍓", "🍉", "🥭", "🥝", "🍑", "🍍", "🍈"
]

# Diagramm nur mit Obstsorten
plt.figure(figsize=(8, 6))
plt.title("Obstsorten vor Clustering")
plt.xlabel("Wassergehalt (%)")
plt.ylabel("Fruchtzuckergehalt (g/100g)")
plt.grid(True)

# Datenpunkte plotten
for i, point in enumerate(data):
    plt.scatter(point[0], point[1], color="black", s=50, zorder=1)
    emoji_path = imojify.get_img_path(emoji_map[i])
    add_image(emoji_path, point[0], point[1])

plt.show()

# K-Means Clustering
k = 3  # Anzahl der Cluster
max_iter = 10

# Initialisiere zufällige Zentroiden
# random.seed(0) # 3 Interation
# random.seed(60) # 2 Iterationen
random.seed(42) # 4 Interation
# random.seed(99) # 4 Interation
centroids = random.sample(data, k)

# K-Means Iterationen
for iteration in range(max_iter):
    # Clusterzuordnung basierend auf der Manhattan-Distanz
    clusters = []
    for point in data:
        distances = [manhattan_distance(point, centroid) for centroid in centroids]
        cluster_idx = distances.index(min(distances))
        clusters.append(cluster_idx)

    # Visualisierung
    plt.figure(figsize=(8, 6))
    plt.title(f"Iteration {iteration + 1}")
    plt.xlabel("Wassergehalt (%)")
    plt.ylabel("Fruchtzuckergehalt (g/100g)")
    plt.grid(True)

    colors = ['#381fb4', '#2ca02c', '#a14242']  # Farben für die Cluster
    for cluster_idx in range(k):
        cluster_points = [data[i] for i in range(len(data)) if clusters[i] == cluster_idx]
        if cluster_points:
            x_vals = [p[0] for p in cluster_points]
            y_vals = [p[1] for p in cluster_points]
            plt.scatter(x_vals, y_vals, color=colors[cluster_idx], s=50, zorder=3, label=f"Cluster {cluster_idx + 1}")

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
    new_centroids = calculate_new_centroids(data, clusters, k)

    # Abbruchbedingung prüfen
    if all(new_centroids[i] == centroids[i] for i in range(k)):
        print(f"Konvergenz nach {iteration + 1} Iterationen erreicht.")
        break

    centroids = new_centroids
