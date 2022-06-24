import cv2
import numpy as np
import os
from typing import Tuple


def get_cam() -> cv2.VideoCapture:
    """
        This function returns the cv2.VideoCapture object
    """
    return cv2.VideoCapture(0)


def get_writer(frame_size: Tuple[int, int], file_name: str = 'test.avi', fps: int = 10) -> cv2.VideoWriter:
    """
        This function returns the cv2.VideoWriter object
    """
    return cv2.VideoWriter(file_name, cv2.VideoWriter_fourcc(*'XVID'), fps, frame_size)


def display_frame(frame: np.ndarray, delay: int = 0) -> None:
    """
        This function displays the frame
    """
    cv2.imshow('frame', frame)
    cv2.waitKey(delay)


def create_directory(directory_name: str) -> None:
    """
        This function creates a directory
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print('Directory created successfully')
    else:
        print('Directory already exists')

