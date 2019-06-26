# File Lock Threading

## Linux Specific : fcntl

When multiple programs write to one file, there can be issues with the order of file being written on.

For Linux system, using the fcntl lock functionality will solve this problem.

Currently I am using WSL(Ubuntu 16.04) on a Windows 10 machine.

The test has 6 run files each adding to a json object : master.json

When there is a lock on the file, the file can't be written and the other files need to wait for it to be unlocked.

The next file in the line will be able to write to the json object.

	import fcntl
	fcntl.flock(outfile, fcntl.LOCK_EX)
	fcntl.flock(outfile, fcntl.LOCK_UN)

## Cross-Platform (Windows and UNIX) Solution : portalocker

For Windows we will need to use portalocker.

This solution will also work for Linux.

Currently I am using Powershell on a Windows 10 machine.

With Python3 and Python2 installations.

The specific version is Python 2.7.9 which has pip installed by default.

So running it as a Python2 command use the following to first update pip:

	py -2 -m pip install -U pip

Now that pip is updated, install portalocker with this command:

	py -2 -m pip install portalocker

Important to note that each Python installation will have a different pip installed.

To run portalocker:

	import portalocker
	portalocker.lock(outfile, portalocker.LOCK_EX)
	portalocker.unlock(outfile)