"""
    This file is going to be an adapted version of what is on the Jetsons.
    We will record a video on our webcam and display the relevant FPS
"""
import cv2
import numpy as np
import multiprocessing as mp
import time

from opencv_utils import get_cam, display_frame, create_directory, get_writer

WIDTH = 1280
HEIGHT = 720
FRAME_SIZE = (WIDTH, HEIGHT)


def record_video(directory_name: str, video_name: str) -> None:
    """
        This function records a video from the webcam and saves it in the directory_name
    """
    # Create directory
    create_directory(directory_name)

    # Get camera
    cam = get_cam()

    # Get writer
    writer = get_writer(file_name=f'{directory_name}/{video_name}.avi', frame_size=FRAME_SIZE)


    # Check if camera opened successfully
    if cam.isOpened():
        print('Camera opened successfully')

        while True:

            # start timer for FPS calculation
            start_time = time.time()

            ret_val, frame = cam.read()

            print("Camera read FPS: ", 1.0 / (time.time() - start_time))

            if not ret_val:
                print('Error reading frame')
                break

            writer.write(frame)
            print("Video writer FPS: ", 1.0 / (time.time() - start_time))
    else:
        print('Error opening camera')
        exit()

    # Close the camera
    cam.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    record_video('videos', 'test_video')


