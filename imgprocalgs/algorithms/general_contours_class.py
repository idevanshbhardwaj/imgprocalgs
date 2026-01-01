# Class-based wrapper for contour detection

import cv2
from imgprocalgs.base import ImageAlgorithm


class GeneralContours(ImageAlgorithm):

    def process(self):
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        _, saturation, _ = cv2.split(hsv)

        _, thresholded = cv2.threshold(
            saturation, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        filtered = cv2.medianBlur(thresholded, 5)

        contours, _ = cv2.findContours(
            filtered, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )

        return contours
