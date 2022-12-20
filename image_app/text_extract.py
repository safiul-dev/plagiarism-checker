import pytesseract
from PIL import Image
class ImageConverter:

    def convert(self, image): 

        text = pytesseract.image_to_string(Image.open(image), lang="ben")
        return text.replace('\n', ' ')