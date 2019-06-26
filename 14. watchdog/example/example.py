#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
import sys
import time

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.ERROR)

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer, filename):
        self.observer = observer
        self.filename = filename

    def on_created(self, event):
        print "e=", event
        if not event.is_directory and event.src_path.endswith(self.filename):
            print "file created"
            self.observer.stop()

        cwd = os.getcwd()  # Get the current working directory (cwd)
        files = os.listdir(cwd)  # Get all the files in that directory
        print("Files in '%s': %s" % (cwd, files))

        print "test" 

def main(argv=None):
    path = "test"
    filename = "test"
    observer = Observer()
    event_handler = MyEventHandler(observer, filename)
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    observer.join()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
