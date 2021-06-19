from PIL import Image
import os
import sys


class NumberModel:
    STANDARD_SIZE = 100, 100

    def __init__(self):
        pass

    def parse_image(self, path_for_image):
        image_file = Image.open(path_for_image)
        image_file = image_file.convert('1')
        image_file.thumbnail(self.STANDARD_SIZE, Image.ANTIALIAS)
        image_file.show()

        return image_file.load(), image_file.size

    def train_model(self, path_for_image):
        image_pixels, x_size, y_size = self.parse_image(path_for_image)
        print(self.parse_image(path_for_image))

    def try_to_analyze(self, path_to_image):
        pass
