from tempfile import TemporaryDirectory
from pdf2image import convert_from_bytes
from .image_converter import ImageConverter
class PdfConverter:
    
    def converter (pdf) -> None:
        
        image_converter = ImageConverter()
        if pdf:
            image_file_list = []
            all_text = ''
            with TemporaryDirectory() as tempdir:
                pdf_pages = convert_from_bytes(pdf.read())
                for page_enumeration, page in enumerate(pdf_pages, start=1):
                    filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
                    page.save(filename, "JPEG")
                    image_file_list.append(filename)
                else:
                    all_text = image_converter.convert(image_file_list) # convert this all images using ocr
                    terminator = ["।", "?", "!"]
                    tokens = []
                    for i in all_text:
                        if i in terminator:
                            my_string = all_text[:all_text.index(i)+1]
                            all_text = all_text[all_text.index(i)+1:]
                            tokens.append(my_string.strip())
                    return tokens
        else:
            return 'this is not a pdf'
