# Linux File Lock Threading

When multiple programs write to one file, there can be issues with the order of operations.

For Linux system, using the fcntl lock functionality will solve this problem.

The test has 6 run files each adding to a json object : master.json

When there is a lock on the file, the file can't be written and the other files need to wait for it to be unlocked.

The next file in the line will be able to write to the json object.

	import fcntl
	fcntl.flock(outfile, fcntl.LOCK_EX)
	fcntl.flock(outfile, fcntl.LOCK_UN)
