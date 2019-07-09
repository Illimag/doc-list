# Create update-grub

To run update-grub command after making edits to the 

	/etc/default/grub

First try to reinstall to see if this fixes the problem.

	sudo apt-get update; sudo apt-get install --reinstall grub

Just make a new file

	sudo vim /usr/sbin/update-grub

Add this to the file

	#!/bin/sh
	set -e
	exec grub-mkconfig -o /boot/grub/grub.cfg "$@"

Then save and run the following commands to update permissions

	sudo chown root:root /usr/sbin/update-grub
	sudo chmod 755 /usr/sbin/update-grub

Now try to run

	update-grub
