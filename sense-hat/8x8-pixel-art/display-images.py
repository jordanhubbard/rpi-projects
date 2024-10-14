from PIL import Image
import os
import time
from sense_hat import SenseHat

def display_image(image, delay=1):
    print(f"Displaying {image}")
    sense = SenseHat()
    sense.load_image(image)
    time.sleep(delay)

def display_image_in_sections(image_path, section_size=64):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Create an output directory for sections
    output_dir = "_image_sections"
    os.makedirs(output_dir, exist_ok=True)

    # Calculate the number of horizontal and vertical sections
    num_horizontal_sections = img_width // section_size
    num_vertical_sections = img_height // section_size

    # Loop through the image and extract sections
    print(f"Split image into {num_vertical_sections * num_horizontal_sections} sections.")
    for row in range(num_vertical_sections):
        for col in range(num_horizontal_sections):
            # Define the box (left, upper, right, lower) for the section
            left = col * section_size
            upper = row * section_size
            right = left + section_size
            lower = upper + section_size

            # Crop the section
            section = img.crop((left, upper, right, lower))

            # Save the section
            section_filename = f"{output_dir}/section_{row}_{col}.png"
            section.save(section_filename)
            display_image(section_filename)

display_image_in_sections("image-files/8x8characters.png")
