import matplotlib.pyplot as plt
import os

colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'brown', 'cyan', 'magenta']

def plot_initial_data(data, output_dir):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:, 0], data[:, 1], s=5, color='black')
    plt.title("Ausgangsdaten")
    plt.xlabel('Merkmal 1')
    plt.ylabel('Merkmal 2')
    plt.grid(True)
    output_path = os.path.join(output_dir, "kmeans_step_0.png")
    plt.savefig(output_path)
    plt.close()
    return output_path

def plot_kmeans_step(data, centroids, labels, iteration, output_dir):
    import matplotlib.pyplot as plt
    import os

    colors = ['red', 'blue', 'green', 'purple']  # Farben für die Cluster
    plt.figure(figsize=(8, 6))

    # Clusterpunkte und Labels plotten
    for i, color in enumerate(colors[:len(centroids)]):
        cluster_data = data[labels == i]
        centroid_coords = f"({centroids[i][0]:.2f}, {centroids[i][1]:.2f})"
        plt.scatter(cluster_data[:, 0], cluster_data[:, 1], s=5, color=color, label=f'Cluster {i + 1} {centroid_coords}')

    # Zentroiden plotten (aber nicht in der Legende)
    for i, centroid in enumerate(centroids):
        plt.scatter(centroid[0], centroid[1], s=200, color=colors[i], marker='x', linewidth=2)

    # Titel, Achsenbeschriftung und Legende
    plt.title(f"K-Means Zwischenschritt: Iteration {iteration}")
    plt.xlabel('Merkmal 1')
    plt.ylabel('Merkmal 2')
    plt.grid(True)
    plt.legend(loc='best', markerscale=2)  # Legende korrekt anzeigen

    # Bild speichern
    output_path = os.path.join(output_dir, f"kmeans_step_{iteration}.png")
    plt.savefig(output_path)
    plt.close()
    return output_path

