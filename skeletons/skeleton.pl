#!/usr/bin/perl -w

#
# Skeleton script.
# 
# $Id: $
# $Author: $
# $Date: $
# $Revision: $
#

# --- LIBRARIES --------------------------------------------------------------
use strict;
use Date::Calc qw(Today_and_Now);

# --- CONSTANTS --------------------------------------------------------------
use constant {
  USAGE_MSG => "Usage: $0\n"
};


# --- START OF MAIN ----------------------------------------------------------

&log("Started");

# check parameters or...
print USAGE_MSG;

my $var = "Do stuff";
&log($var);

&stop("Finished", 0);

# --- END OF MAIN ------------------------------------------------------------


sub log {
  my $msg = $_[0];
  my $stamp = sprintf("%4d-%02d-%02d %02d:%02d:%02d", Today_and_Now());

  print "$stamp $msg\n";
}

sub stop {
  &log($_[0]);
  &log("Exiting with return code $_[1]");
  exit $_[1];
}

