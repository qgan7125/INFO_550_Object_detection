# This file is the main file to run yolo class
# Author: Quan Gan

import basic 
import os
import sys

# -------------------------------------------------------------------------------
# Run object detection
# -------------------------------------------------------------------------------
def simple_model(img='https://ultralytics.com/images/zidane.jpg'):
    model = basic.Simple_model()
    model.detect_video(0)


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
                    - starts simple object detection
                (2) python main.py -t or python main.py --srt
                    - starts a real time simple object detection
    """
    parser = OptionParser(usage_str)

    parser.add_option('-t', '--srt', action='store_true', dest='simple_case', default=False,
                    help=default("Start a simple model object detection"))

    parser.add_option('-f', '--file', dest='file', default=False,
                    help=default("File location or link"))

    options, other_junk = parser.parse_args(argv)
    
    if len(other_junk) != 0:
        raise Exception("Command line input not understood: " + str(other_junk))

    return options

def run_command(options):
    if options.simple_case:
        pass
    else:
        simple_model()

if __name__ == '__main__':
    """
    The main funciton called when wumpus_test.py is run from the command line:
    > python wumpus_test.py <options>
    """
    _options = read_command(sys.argv[1:])
    run_command(_options)