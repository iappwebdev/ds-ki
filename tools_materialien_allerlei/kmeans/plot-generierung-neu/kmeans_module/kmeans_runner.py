import os
import shutil
import numpy as np
from .kmeans_plotting import plot_initial_data, plot_kmeans_step
from .kmeans_gif import create_gif

def run_kmeans(data, n_clusters, max_iter, current_file_name, random_seed=42):
    # Seed für Reproduzierbarkeit setzen
    np.random.seed(random_seed)

    # Verzeichnis für Bilder erstellen
    output_dir = f"images/{current_file_name}"
    
    # Ordner löschen, falls er existiert
    if os.path.exists(output_dir):
        shutil.rmtree(output_dir)
        print(f"Ordner {output_dir} existiert bereits und wird gelöscht")
    os.makedirs(output_dir, exist_ok=True)

    # k-means++ Initialisierung
    centroids = []
    centroids.append(data[np.random.randint(data.shape[0])])  # Wähle einen zufälligen Punkt als erstes Zentrum

    for _ in range(1, n_clusters):
        # Berechne den Abstand jedes Punktes zu den nächsten bereits gewählten Zentroiden
        distances = np.array([min(np.linalg.norm(x - c) for c in centroids) for x in data])
        probabilities = distances / distances.sum()  # Wahrscheinlichkeiten proportional zu den Abständen
        cumulative_probabilities = np.cumsum(probabilities)
        r = np.random.rand()

        # Wähle den nächsten Punkt basierend auf den Wahrscheinlichkeiten
        for i, p in enumerate(cumulative_probabilities):
            if r < p:
                centroids.append(data[i])
                break

    centroids = np.array(centroids)

    labels = np.zeros(data.shape[0], dtype=int)
    saved_images = []

    # Ausgangsdaten plotten
    saved_images.append(plot_initial_data(data, output_dir))

    # K-Means-Iteration
    for i in range(1, max_iter + 1):
        labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)
        centroids_old = centroids.copy()

        # Berechne die neuen Zentroiden
        for j in range(n_clusters):
            cluster_points = data[labels == j]
            if len(cluster_points) > 0:
                centroids[j] = cluster_points.mean(axis=0)
        
        # Visualisierung der aktuellen Iteration
        plot_path = plot_kmeans_step(data, centroids, labels, i, output_dir)
        saved_images.append(plot_path)

        # Abbruchbedingung
        if np.allclose(centroids, centroids_old, atol=1e-4):
            print(f"Konvergenz nach {i} Iterationen erreicht")
            break

    # GIF erstellen
    gif_path = create_gif(saved_images, output_dir)
    return gif_path
