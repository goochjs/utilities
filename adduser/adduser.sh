#!/bin/bash
# Script to add a user to Linux system
if [ $(id -u) -eq 0 ]; then
	read -p "Enter username : " username
	egrep "^$username" /etc/passwd >/dev/null
	if [ $? -eq 0 ]; then
		echo "$username already exists"
		exit 1
	fi

	read -p "Enter fullname : " fullname
	read -p "Enter comma-separated list of groups : " usergrps
	read -p "Enter public cert : " cert

	# -m = create home dir
	useradd -m -G $usergrps -c "\"$fullname\"" -s /bin/bash $username

	if [ $? -eq 0 ]; then
		echo "User has been added to system"
	else
		echo "Failed to add user"
		exit 1
	fi

	mkdir /home/$username/.ssh
	echo $cert > /home/$username/.ssh/authorized_keys
	chmod 600 /home/$username/.ssh/authorized_keys
	sudo chown -R $username:$username /home/$username
else
	echo "Only root may add a user to the system"
	exit 2
fi
