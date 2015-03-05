adduser.sh
==========

Shell script to interactively add a user to a Linux system, including importing a public key for ssh access..

Script will ask for:-

* the new user ID
* the user's name
* a comma-separated list of groups (NB no spaces!)
* the user's public key

It will then:-

* add the user to the system
* create the home directory
* create the .ssh directory
* add the certificate to the "authorized_keys" file

Script must be run as root or via sudo.