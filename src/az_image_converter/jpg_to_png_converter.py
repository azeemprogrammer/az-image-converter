from PIL import Image
from .converter import ImageConverter

class JPGtoPNGConverter(ImageConverter):
    def _convert_image(self, img):
        if img.mode != "RGBA":
            img = img.convert("RGBA")
        return img
