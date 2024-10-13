from PIL import Image
import os
import time
from sense_hat import SenseHat

def display_image(sense, image, delay=1):
    sense.load_image(image)
    time.sleep(delay)

def display_image_in_sections(sense, image_path, section_size=8):
    # Open the image
    img = Image.open(image_path)
    img_width, img_height = img.size

    # Create an output directory for sections
    output_dir = "image_sections"
    os.makedirs(output_dir, exist_ok=True)

    # Calculate the number of horizontal and vertical sections
    num_horizontal_sections = img_width // section_size
    num_vertical_sections = img_height // section_size

    # Loop through the image and extract sections
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
            display_image(sense, section_filename)

    print(f"Image split into {num_vertical_sections * num_horizontal_sections} sections.")

sense = SenseHat()

display_image_in_sections(sense, "image-files/8x8characters.png")
