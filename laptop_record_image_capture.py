import os
import cv2
import numpy as np
import multiprocessing as mp
import time

from opencv_utils import get_cam, get_frame, display_frame


def create_directory(directory_name: str) -> None:
    """
        This function creates a directory
    """
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)
        print('Directory created successfully')
    else:
        print('Directory already exists')


def basic_image_capture(directory_name: str, video_name: str) -> None:
    """
        This function records a video from the webcam and saves it in the directory_name
    """
    # Create directory
    create_directory(directory_name)

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
    print("Press 'q' or 'return' to quit")
    display_frame(frame)

    # Close the camera
    cam.release()
    cv2.destroyAllWindows()
    print('Camera closed successfully')

    # Save the frame
    cv2.imwrite(directory_name + '/' + video_name + '.jpg', frame)
    print('Frame saved successfully')


if __name__ == '__main__':
    basic_image_capture('images', 'test')
