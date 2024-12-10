from PIL import Image
import os

def create_gif(image_paths, output_dir):
    frames = [Image.open(img) for img in image_paths]
    gif_path = os.path.join(output_dir, "kmeans_iterations.gif")
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=1000,
        loop=0
    )
    return gif_path
