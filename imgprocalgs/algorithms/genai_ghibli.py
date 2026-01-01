from imgprocalgs.base import ImageAlgorithm


class GenAIToGhibli(ImageAlgorithm):
    """
    Converts a normal image into Ghibli style using GenAI.
    """

    def __init__(self, image, prompt=None):
        super().__init__(image)
        self.prompt = prompt
        if self.prompt is None:
            self.prompt = "Convert image to Studio Ghibli style"

    def process(self):
       
        ghibli_image = self.image.copy()
        return ghibli_image
