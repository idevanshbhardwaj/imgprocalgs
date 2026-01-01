from abc import ABC, abstractmethod
import numpy as np


class ImageAlgorithm(ABC):

    def __init__(self, image):
        self.image = image

    def run(self):
        if self.image is None:
            raise ValueError("Image is required")

        if not isinstance(self.image, np.ndarray):
            raise TypeError("Image must be a numpy array")

        return self.process()

    @abstractmethod
    def process(self):
        pass
