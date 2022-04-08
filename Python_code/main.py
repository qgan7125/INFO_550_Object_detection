# This file is the main file to run yolo class
# Author: Quan Gan

import basic 
import os
import sys
import torch

# -------------------------------------------------------------------------------
# Run object detection
# -------------------------------------------------------------------------------
def simple_model(type=True, file=""):
    """Using basic yolo to detect

    Args:
        type: a boolean to indicate what type file to detect
            True as video detection, False as image detection
        file: a string to represent file source, 
             default 0 as camera
    """
    yolo_model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    model = basic.Obj_detect(yolo_model)

    if type:
        if not file:
            model.detect_video(0)
        else:
            model.detect_video(file)
    else:
        model.detect_img(file)


# -------------------------------------------------------------------------------
# Command-line interface
# -------------------------------------------------------------------------------
def default(str):
  return str + ' [Default: %default]'

def read_command(argv):
    """
    Processes the command used to run yolo.py from the command line.
    """
    from optparse import OptionParser
    usage_str = """
    USAGE:      Python main.py <options>
    Examples:   (1) python main.py
                    - starts simple object detection with camera
                (2) python main.py -f filename
                    - starts simple object detection on video source
                    - ex python main.py -f car_traffic.mp4
                (3) python main.py -i -f filename or python main.py --img -file filename
                    - to indicate if the file source is image
                    - must with -f command to specify the file source
                    - python main.py -i -f https://ultralytics.com/images/zidane.jpg
    """
    parser = OptionParser(usage_str)

    parser.add_option('-i', '--img', action='store_true', dest='image', default=False,
                help=default("Indicate the source file type as image"))

    parser.add_option('-f', '--file', dest='file',
                    help=default("File location or link"))

    options, other_junk = parser.parse_args(argv)
    
    if len(other_junk) != 0:
        raise Exception("Command line input not understood: " + str(other_junk))

    return options

def run_command(options):
    if not options.file:
        simple_model()
    else:
        if options.image:
            simple_model(False, options.file)
        else:
            simple_model(True, options.file)


if __name__ == '__main__':
    """
    The main funciton called when wumpus_test.py is run from the command line:
    > python wumpus_test.py <options>
    """
    _options = read_command(sys.argv[1:])
    run_command(_options)