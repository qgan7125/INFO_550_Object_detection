# This file is the main file to run yolo class
# Author: Quan Gan

from ast import arg
from operator import mod
import basic 
import os
import sys
import torch

# -------------------------------------------------------------------------------
# Helper
# -------------------------------------------------------------------------------
def filenames(path):
    """Read all file names in the folder and return full path

    Args:
        path: a str of the test folder
    
    return a list of file paths
    """
    files = os.listdir(path)
    return None

# -------------------------------------------------------------------------------
# Run object detection
# -------------------------------------------------------------------------------
def yield_result(pretained_model, **arguments):
    """Using basic yolo to detect

    Args:
        arguments: a unknown dictionary
    """

    model = basic.Obj_detect(pretained_model)

    # for multiple detect
    if arguments['path']:
        files = os.listdir(arguments['path'])
        if arguments['image']:
            for file in files:
                model.detect_img(os.path.join(arguments['path'], file))
        else:
            if not arguments['file']:
                model.detect_video(0)
            else:
                for file in files:
                    model.detect_video(os.path.join(arguments['path'], file))
    # for single file
    else:
        if arguments['image']:
            model.detect_img(arguments['file'])
        else:
            if not arguments['file']:
                model.detect_video(0)
            else:
                model.detect_video(arguments['file'])



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
    
    parser.add_option('-c', '--custom', dest='custom_model',
                help=default("The path of custom_model"))

    parser.add_option('-f', '--file', dest='file',
                    help=default("Test file location or link"))
    
    parser.add_option('-p', '--path', dest='path',
                help=default("Test folder location"))

    options, other_junk = parser.parse_args(argv)
    
    if len(other_junk) != 0:
        raise Exception("Command line input not understood: " + str(other_junk))

    return options

def run_command(options):
    if options.file and options.path:
        print("Error: Multiple sources", file=sys.stderr)

    model = None
    print(options)
    if options.custom_model:
        # train the custom model
        model = torch.hub.load('ultralytics/yolov5', 'custom', path=options.custom_model, force_reload=True)
    else:
        # train the basic model
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

    yield_result(model, 
                image = options.image, 
                custom_model = options.custom_model,
                file = options.file,
                path = options.path)


if __name__ == '__main__':
    """
    The main funciton called when wumpus_test.py is run from the command line:
    > python wumpus_test.py <options>
    """
    _options = read_command(sys.argv[1:])
    run_command(_options)