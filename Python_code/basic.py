# This file contains the basic example to use yolov5
# And class to do real time object detection
# Author: Quan Gan


from matplotlib import pyplot as plt
import numpy as np
import cv2
import os

class Obj_detect:
    '''This is a simple yolov5 class

    This class will run basic yolov5s model to detect image 
    or video

    Args:
        model: a pretrained yolo model

    '''
    def __init__(self, model):
        self._yolo_model = model
    
    def detect_img(self, img: str) -> None:
        """This function detects a image

        Args:
            img: a str of image link or path
        
        Print the detection result
        """
        results = self._yolo_model(img)
        results.print()
        plt.imshow(np.squeeze(results.render()))
        filename = ".".join(os.path.basename(img).split('.')[:-1])
        plt.savefig(f'result/{filename}_result.png')
    
    def detect_video(self, video) -> None:
        """This function detects a video

        Args:
            img: a str of video link or path or
                 a integer of camera default as 0
        
        Press q to stop
        """
        cap = cv2.VideoCapture(video)
        print("Press q to stop the real time detection")

        while cap.isOpened():
            ret, frame = cap.read()
            
            # Make detections 
            results = self._yolo_model(frame)
            
            cv2.imshow('YOLO', np.squeeze(results.render()))
            
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
    
