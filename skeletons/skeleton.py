'''
Created on 1 Dec 2016

@author: Jeremy Gooch

    Skeleton script.

    Execute script with -h parameter for usage
'''

# --- LIBRARIES --------------------------------------------------------------

import argparse
import logging
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
    opts.add_argument("--something_else", "-e",
                      required=True,
                      help="another parameter")
    opts.add_argument("--verbose", "-v",
                      required=False,
                      default=False,
                      action="store_true",
                      help="Send log messages to sysout")
    options = opts.parse_args()

    if options.verbose:
        logging.basicConfig(
            level=logging.DEBUG,
            format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )
    else:
        logging.basicConfig(
            level=logging.INFO,
            format='[%(levelname)s] (%(threadName)-10s) %(message)s',
        )

    return(
        options.something,
        options.something_else
    )


# --- CLASSES ----------------------------------------------------------------



# --- START OF MAIN ----------------------------------------------------------

def main():
    start_time = datetime.datetime.now()
    (some_parameter, another_parameter) = process_options()

    logging.debug(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p") + " Started")

    # Do stuff here
    logging.info("Parameter 1: " + some_parameter)
    logging.info("Parameter 2: " + another_parameter)

    exec_time = datetime.datetime.now() - start_time
    logging.debug("Execution time " + str(exec_time))
    logging.debug(datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p") + " Finished")



# --- END OF MAIN ------------------------------------------------------------


if __name__ == "__main__":
    main()
