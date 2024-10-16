import random

class Colors:
    # A dictionary to store some common colors with their RGB values
    colors = {
        'red': (255, 0, 0),
        'green': (0, 255, 0),
        'blue': (0, 0, 255),
        'black': (0, 0, 0),
        'white': (255, 255, 255),
        'yellow': (255, 255, 0),
        'purple': (128, 0, 128),
        'orange': (255, 165, 0),
        'pink': (255, 192, 203),
        'gray': (128, 128, 128)
    }

    def __init__(self):
        pass

    def get_rgb(self, color_name):
        """Returns the RGB value of the given color name."""
        color_name = color_name.lower()
        if color_name in self.colors:
            return self.colors[color_name]
        else:
            raise ValueError(f"Color '{color_name}' not found. Please use a valid color name.")


    def random_rgb(self):
        return random.choice(list(self.colors.values()))

