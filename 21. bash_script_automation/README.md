# Bash Script Automation

Bash files are a great way to automate processes.

For example, for the WSL(Windows Subsystem for Linux) on the Windows 10 platform, when opening the shell application, the default location is:

	home/user

Because the location of the Desktop is:

	mnt/c/Users/user/Desktop

Instead of using cd commands to manually move through the system, a simple bash script takes the shell to the dir.

	#!/bin/bash
	cd /
	cd mnt/c/Users/user/Desktop

To run a bash file from the terminal:

	. ./file.sh 
