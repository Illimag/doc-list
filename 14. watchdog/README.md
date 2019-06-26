# Watchdog

Watchdog is a python dependency that runs in the background watching for changes in a dir.

For example there is a dir:

If a text file is added to the dir, then it will print "test"

Install watchdog

pip install watchdog 

add the event handler and observer

	from watchdog.events import FileSystemEventHandler
	from watchdog.observers import Observer

Will add an example in this dir.

IMPORTANT:

You can't name file watchdog.py

It can be watchdog_test.py

I dont know why but you can't name it watchdog.py

Or else you will have a path issue.
