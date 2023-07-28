from PIL import Image
from .converter import ImageConverter

class PNGtoJPGConverter(ImageConverter):
    def _convert_image(self, img):
        if img.mode == "RGBA":
            img = img.convert("RGB")
        return img
