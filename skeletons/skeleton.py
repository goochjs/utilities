'''
Created on 1 Dec 2016

@author: Jeremy Gooch

    Skeleton script.

    Execute script with -h parameter for usage
'''

# --- LIBRARIES --------------------------------------------------------------

import argparse
import datetime
import sys


# --- FUNCTIONS --------------------------------------------------------------

def process_options():
    '''
    Processes command line options
    '''
    
    opts = argparse.ArgumentParser(description="A skeleton script")

    opts.add_argument("--something", "-s",
                      required=True,
                      help="some parameter")
    opts.add_argument("--log", "-l",
                      required=False,
                      default=False,
                      action="store_true",
                      help="Send log messages to sysout")
    options = opts.parse_args()

    return(options.something, options.log)


# --- CLASSES ----------------------------------------------------------------

class script_logger(object):
    def __init__(self, log_flag):
        '''
        Script control class for logging messages (if required) and stopping execution
        '''
        
        self.log_flag = log_flag


    def log(self, log_message):
        '''
        Prints a timestamped log message
        '''
    
        if self.log_flag:
            time_stamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            print (time_stamp + " " + log_message)


    def stop(self, log_message, exit_code, override_flag):
        '''
        Stops the script, logging an output message and setting a return code
        
        The override flag parameter will force a log message, even if the script has been called in non-logging mode
        '''
    
        if override_flag:
            self.log_flag = True

        self.log(log_message)
        self.log("Exiting with return code " + str(exit_code))
        sys.exit(exit_code)


    
# --- START OF MAIN ----------------------------------------------------------

def main():
    (some_parameter, log_flag) = process_options()
    
    logger = script_logger(log_flag)
    logger.log("Started")
    
    logger.stop("Finished", 0, False)



# --- END OF MAIN ------------------------------------------------------------


if __name__ == "__main__":
    main()