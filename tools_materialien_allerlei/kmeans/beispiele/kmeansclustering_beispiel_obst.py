import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import pandas as pd
from sklearn.cluster import KMeans
from matplotlib import rcParams
from imojify import imojify

# Daten vorbereiten
data = {
    "Obst": ["Apfel", "Birne", "Banane", "Orange", "Weintrauben", "Erdbeere", "Wassermelone", "Mango"], #"Kiwi", "Pfirsich", "Ananas"],
    "Wassergehalt": [85, 83, 75, 87, 81, 91, 92, 83], #78, 88, 82],
    "Fruchtzuckergehalt": [10, 10, 12, 8, 16, 5, 6, 14], #9, 7, 15],
}

df = pd.DataFrame(data)

# K-Means Clustering
# Um unterschiedliche Resultate zu erhalten, kann random_state auf andere Werte als 42 gesetzt werden
random_state, colors = 5, ['r', 'g', 'b']
#random_state, colors = 42, ['r', 'g', 'b']
# Um das Bild ohne Datenpunkte zu erhalten, muss temporär zorder=3 für add_image() gesetzt werden
zorder_emojis = 1

kmeans = KMeans(n_clusters=3, max_iter=500, random_state=random_state)
df['Cluster'] = kmeans.fit_predict(df[["Wassergehalt", "Fruchtzuckergehalt"]])

# Zuordnung der Früchte zu den entsprechenden Emojis
emoji_map = {
    "Apfel": "🍎",
    "Birne": "🍐",
    "Banane": "🍌",
    "Orange": "🍊",
    "Weintrauben": "🍇",
    "Erdbeere": "🍓",
    "Wassermelone": "🍉",
    "Mango": "🥭",
    # "Kiwi": "🥝",
    # "Pfirsich": "🍑",
    # "Ananas": "🍍",
}

# Diagramm einrichten
plt.figure(figsize=(10, 8))
plt.xlabel("Wassergehalt (%)")
plt.ylabel("Fruchtzuckergehalt (g/100g)")
plt.grid(True)

# Zuerst Emojis neben den Streudiagrammpunkten hinzufügen
def add_image(emoji_path, x, y, zoom=0.05, x_offset=1.5, y_offset=1.0):
    """
    Fügt ein Bild (Emoji) neben dem Diagramm an den angegebenen Koordinaten mit einem Versatz hinzu.

    Parameter:
    - emoji_path: Pfad zum Emoji-Bild.
    - x, y: Koordinaten, wo das Bild hinzugefügt werden soll.
    - zoom: Zoom-Level des Bildes.
    - x_offset, y_offset: Versatzwerte, um das Emoji neben den Datenpunkt zu positionieren.
    """
    img = plt.imread(emoji_path)
    imagebox = OffsetImage(img, zoom=zoom)
    ab = AnnotationBbox(imagebox, (x + x_offset, y + y_offset), frameon=False, zorder=zorder_emojis)
    plt.gca().add_artist(ab)

for i, row in df.iterrows():
    emoji = emoji_map.get(row['Obst'])
    if emoji:
        emoji_path = imojify.get_img_path(emoji)
        # Emoji mit einem Versatz hinzufügen, um Überlappungen mit dem Datenpunkt zu vermeiden
        add_image(emoji_path, row['Wassergehalt'], row['Fruchtzuckergehalt'], zoom=0.075, x_offset=0.0, y_offset=0.0)

# Jedes Cluster separat plotten, um unterschiedliche Legendeinträge zu erzeugen
for cluster in sorted(df['Cluster'].unique()):  # Cluster sortieren, damit die Legende in der gewünschten Reihenfolge ist
    cluster_data = df[df['Cluster'] == cluster]
    plt.scatter(cluster_data['Wassergehalt'], cluster_data['Fruchtzuckergehalt'],
                label=f'Cluster {cluster + 1}', color=colors[cluster], s=100, zorder=2)

# Nur aktivieren, wenn neu erzeugt werden soll, zorder_emojis=3 setzen (s.o.)
# plt.draw()
# plt.savefig("images/kmeans_obst.svg")

# Zentroiden der Cluster plotten, mit den gleichen Farben wie die Cluster
centroids = kmeans.cluster_centers_
for cluster_index, centroid in enumerate(centroids):
    plt.scatter(centroid[0], centroid[1], c=[colors[cluster_index]], marker='x', s=200, linewidths=3)

centroids = kmeans.cluster_centers_
for i, centroid in enumerate(centroids):
    print(f"Centroid {i}: Wassergehalt = {centroid[0]}, Fruchtzuckergehalt = {centroid[1]}")

# Zentroiden-Koordinaten als Text in der entsprechenden Cluster-Farbe unterhalb des Plots einfügen
for i, (x, y) in enumerate(centroids):
    plt.figtext(0.2, 0.3 - i * 0.05, f"Centroid {i + 1}: {x:.2f}, {y:.2f}", ha="left", 
                fontsize=10, color=colors[i], bbox={"facecolor": "lightgrey", "alpha": 0.5, "pad": 5})

# Hinzufügen von Beschriftungen, Legende und Raster
plt.legend()
plt.savefig(f"images/kmeans_obst_clusters_{random_state}.svg")
