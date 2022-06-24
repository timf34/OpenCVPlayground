"""
    This file is to test the OpenCV code locally on a laptop.
"""
import cv2
import numpy as np
import multiprocessing as mp
import time

WIDTH = 1280
HEIGHT = 720
FRAME_SIZE = (WIDTH, HEIGHT)


def get_cam() -> cv2.VideoCapture:
    """
        This function returns the cv2.VideoCapture object
    """
    return cv2.VideoCapture(0)


def display_frame(frame: np.ndarray) -> None:
    """
        This function displays the frame
    """
    cv2.imshow('frame', frame)
    cv2.waitKey(0)


def get_frame(cam: cv2.VideoCapture) -> np.ndarray:
    """
        This function gets a frame from the camera and returns it
    """
    ret_val, frame = cam.read()
    return frame


if __name__ == '__main__':
    # Get camera
    cam = get_cam()

    # Check if camera opened successfully
    if cam.isOpened():
        print('Camera opened successfully')
    else:
        print('Error opening camera')
        exit()

    # Get the frame
    frame = get_frame(cam)

    # Display the frame
    display_frame(frame)

    # Close the camera
    cam.release()
    cv2.destroyAllWindows()
    print('Camera closed successfully')


