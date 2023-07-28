from PIL import Image

class ImageConverter:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def convert(self):
        try:
            img = Image.open(self.input_file)
            converted_img = self._convert_image(img)
            converted_img.save(self.output_file)
            print(f"Conversion successful. Image saved as {self.output_file}")
        except Exception as e:
            print(f"Error converting image: {e}")

    def _convert_image(self, img):
        pass
