#!/usr/bin/env python
# -*- coding: utf-8 -*-
import watchdog
import os
import logging
import sys
import time
import subprocess


from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

logging.basicConfig(level=logging.ERROR)

class MyEventHandler(FileSystemEventHandler):
    def __init__(self, observer, filename, filename1, filename2):
        self.observer = observer
        self.filename = filename
        self.filename1 = filename1
        self.filename2 = filename2

    def on_created(self, event):
        #print "e=", event
        if not event.is_directory and event.src_path.endswith(self.filename):
            print "test"
        if not event.is_directory and event.src_path.endswith(self.filename1):
            print "test1"   
        if not event.is_directory and event.src_path.endswith(self.filename2):
            print "test2"

        #cwd = os.getcwd()  # Get the current working directory (cwd)
        #files = os.listdir(cwd)  # Get all the files in that directory
        #print("Files in '%s': %s" % (cwd, files))

        #os.system('python ../check_master.py')

        # Because another file is created which is out_lead.json
        # Watchdog runs the clean_leads script again.
        # But because there is no lead.json because spider.py hasen't
        # It throws a missing file error.
        # Currently this is fine for now.
        # But eventually a solution should be for Watchdog to watch 
        # For specific file.

        # Watchdog runs the clean_leads.py with os.system.
        # Because the run_watchdog.py file is located in test_leads
        # When clean_leads.py is run
        # All files paths are relative to the run_watchdog.py file.

def main(argv=None):
    path = "."
    filename = "out_lead.json"
    filename1 = "out1_lead.json"
    filename2 = "out2_lead.json"
    observer = Observer()
    event_handler = MyEventHandler(observer, filename, filename1, filename2)
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    observer.join()
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))