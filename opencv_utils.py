import cv2
import numpy as np

def get_cam() -> cv2.VideoCapture:
    """
        This function returns the cv2.VideoCapture object
    """
    return cv2.VideoCapture(0)


def get_frame(cam: cv2.VideoCapture) -> np.ndarray:
    """
        This function gets a frame from the camera and returns it
    """
    ret_val, frame = cam.read()
    return frame


def display_frame(frame: np.ndarray, delay: int = 0) -> None:
    """
        This function displays the frame
    """
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)
