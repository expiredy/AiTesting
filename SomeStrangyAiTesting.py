from PIL import Image
from config import *
import json
import os
import sys


class AiCore:
    STANDARD_SIZE = 50, 50
    DIFFERENCES_PERCENT = 10
    object_id_name = None

    def __init__(self):
        pass

    def parse_image(self, path_for_image):
        image_file = Image.open(path_for_image)
        image_file.thumbnail(self.STANDARD_SIZE, Image.ANTIALIAS)
        image_file = image_file.convert('1')
        image_file.show()

        return image_file.load(), image_file.size[0], image_file.size[1]

    def train_model(self, path_for_image):
        image_pixels, x_size, y_size = self.parse_image(path_for_image)

    def try_to_analyze(self, image_pixels, x_size_of_image, y_size_of_image):
        pass


class NumberSpirit:
    object_id_name = None
    data_file_path = None
    DATA = []

    def __init__(self, object_id_name, scanning_resolution=(50,50)):
        self.object_id_name = object_id_name
        self.load_saved_data(object_id_name, scanning_resolution[0], scanning_resolution[1])
        self.data_file_path = SAVING_DATA_PATH + "/" + object_id_name + ".json"

    def load_saved_data(self, object_id_name, raw_points, column_points):
        try:
            with open(self.data_file_path) as model_saved_data:
                model_parsed_data = json.load(model_saved_data)
                for key, value in model_parsed_data.item():
                    pass

        except FileNotFoundError:
            with open(self.data_file_path, "w") as new_model_saved_data:
                null_data = {NAME_OF_MODEL_KEY: object_id_name,
                             MODEL_OF_NUMBER_KEY: [[0 for _ in range(AiCore.STANDARD_SIZE[0])]
                                                   for _ in range(AiCore.STANDARD_SIZE[1])],
                             NUMBER_OF_RAW_POINTS_KEY: raw_points,
                             NUMBER_OF_COLUMN_POINTS_KEY: column_points}
                json.dump(null_data, new_model_saved_data, ensure_ascii=False)


if __name__ == "__main__":
    a = NumberSpirit("1")
    a.load_saved_data("1", 50, 50)
