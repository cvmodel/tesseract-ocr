from PIL import Image
import pytesseract
from cvpm.solver import Solver
from tesseract_ocr.bundle import OcrExampleBundle as Bundle

class OCRExampleSolver(Solver):
    def __init__(self, toml_file=None):
        super().__init__(toml_file)
        self.set_bundle(Bundle)
        self.set_ready()
    
    def infer(self, image_file, config):
        result = pytesseract.image_to_string(Image.open(image_file))
        return {
            'result': result
        }