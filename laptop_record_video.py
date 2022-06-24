"""
    This file is going to be an adapted version of what is on the Jetsons.
    We will record a video on our webcam and display the relevant FPS
"""
import cv2
import numpy as np
import multiprocessing as mp
import time

from opencv_utils import get_cam, display_frame, create_directory, get_writer

FRAME_SIZE = (640, 480) # Stick with this figure! (1280, 720) doesn't seem to work!

directory_name: str = 'videos'
video_name: str = 'test'

def record_video(directory_name: str, video_name: str) -> None:
    """
        This function records a video from the webcam and saves it in the directory_name
    """
    # Create directory
    create_directory(directory_name)

    # Get camera
    cam = cv2.VideoCapture(0)

    # Get writer
    writer = cv2.VideoWriter('test.avi', cv2.VideoWriter_fourcc(*'XVID'), 20.0, (640, 480))

    count = 0

    if cam.isOpened():
        print('Camera opened successfully')
        while(True):

            # start timer for FPS calculation
            # start_time = time.time()

            ret_val, frame = cam.read()

            # print("Camera read FPS: ", 1.0 / (time.time() - start_time))

            if not ret_val:
                print('Error reading frame')
                break

            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            # cv2.imshow("frame", frame)

            writer.write(frame)
            # print("Video writer FPS: ", 1.0 / (time.time() - start_time))

            if cv2.waitKey(1) & 0xFF == ord('a'):
                break
    else:
        print('Error opening camera')
        exit()

    # Close the camera
    cam.release()
    writer.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    record_video(directory_name, video_name)

