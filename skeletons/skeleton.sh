#!/bin/bash

# skeleton script
#



# configuration stuff ----------------

_DEBUG="on"



# commands used ----------------------




# functions --------------------------


usage ()
{
  echo "$0 [-h] -- skeleton script

where
    -h  show this help message
    -s  do stuff"

  exit 1
}


do_stuff ()
{
  log "Started"

  # >> INSERT STUFF HERE <<

  log "Finished"
}


log ()
{
  TIMESTAMP=`date "+%Y-%m-%d %H:%M.%S"`
  echo $0 $TIMESTAMP $1
}


function DEBUG()
{
 [ "$_DEBUG" == "on" ] &&  $@
}




# start of main ----------------------

DEBUG set -x

# stop if no params have been passed
if [ $# -eq 0 ] ; then
  usage
  exit 1
fi

# check command line params,
while getopts "sh" opt; do
  case $opt in
    h)
      usage
      exit 0
      ;;
    s)
      do_stuff
      ;;
    ?)
      usage
      exit 1
      ;;
  esac
done

DEBUG set +x

