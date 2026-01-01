from imgprocalgs.base import ImageAlgorithm


class GenAIImageEnhancer(ImageAlgorithm):
    """
    This class is used to enhance an image using a GenAI service.
    """

    def __init__(self, image, prompt=None):
        super().__init__(image)
        self.prompt = prompt
        if self.prompt is None:
            self.prompt = "Enhance image quality"

    def process(self):
       
        enhanced_image = self.image.copy()
        return enhanced_image
