from PIL import Image
import numpy as np
import os
import time
from sense_hat import SenseHat

def find_non_black_bbox(image, threshold=12):
    """
    Finds the bounding box (left, top, right, bottom) of non-black content within an image section.
    """
    pixels = np.array(image)
    non_black_coords = np.where(np.any(pixels > threshold, axis=-1))

    if non_black_coords[0].size == 0 or non_black_coords[1].size == 0:
        return None  # All black section

    top, bottom = np.min(non_black_coords[0]), np.max(non_black_coords[0])
    left, right = np.min(non_black_coords[1]), np.max(non_black_coords[1])

    return (left, top, right + 1, bottom + 1)

def display_image(image, delay=1):
    print(f"Displaying {image}")
    sense = SenseHat()
    sense.load_image(image)
    time.sleep(delay)

def extract_tiles(image_path, tile_size, border_size=10, threshold=5):
    """
    Extracts individual tiles from a tiled image where each tile is surrounded by black pixels.

    Parameters:
    - image_path: Path to the input image.
    - tile_size: Size of each tile (without borders).
    - border_size: Minimum black border size around each tile.
    - threshold: Pixel intensity threshold to detect non-black content.
    """
    # Open the image in RGB mode
    img = Image.open(image_path).convert("RGB")
    img_width, img_height = img.size

    # Output directory for extracted tiles
    output_dir = "_extracted_tiles"
    os.makedirs(output_dir, exist_ok=True)

    tile_counter = 0

    # Calculate the step size including the tile and black borders
    step_size = tile_size + 2 * border_size

    # Loop through the image based on the step size
    for y in range(0, img_height, step_size):
        for x in range(0, img_width, step_size):
            # Crop the section including the tile and its surrounding black border
            section = img.crop((x, y, x + step_size, y + step_size))

            # Find the bounding box of the non-black content in the section
            bbox = find_non_black_bbox(section, threshold)

            if bbox:
                # Crop the tile to remove the black borders
                cropped_tile = section.crop(bbox)
                scaled = cropped_tile.resize((8, 8), Image.LANCZOS)
                # Save the cropped tile
                output_filename = f"{output_dir}/tile_{tile_counter}.png"
                scaled.save(output_filename)
                display_image(output_filename)
                tile_counter += 1

extract_tiles("image-files/8x8characters.png", tile_size=64, border_size=8)
