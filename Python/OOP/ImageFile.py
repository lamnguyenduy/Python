from PIL import Image
import os

class ImageFile:
    def __init__(self, path):
        self.path = path
        self.image = Image.open(path)

    def resize(self, width, height):
        self.image = self.image.resize((width, height))

    def rotate(self, degrees):
        self.image = self.image.rotate(degrees)

    def save(self, output_path):
        self.image.save(output_path)

