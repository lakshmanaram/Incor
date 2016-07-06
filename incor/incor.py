import time
import sys
import os
from watchdog.observers import Observer
import incor
from EventHandler import EventHandler
import psutil
from subprocess import call

def main():

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if path == '--version':
        print('incor v' + incor.__version__)
        return
    observer = Observer()
    eventHandler = EventHandler(path)
    eventHandler.parentpid = os.getpid()
    observer.schedule(eventHandler, path, recursive=True)
    observer.start()
    parent = None
    try:
        parent = psutil.Process(eventHandler.parentpid)
    except psutil.NoSuchProcess:
        print 'No such process'
    eventHandler.existing_Children = parent.children(recursive=True)
    print eventHandler.existing_Children
    try:
        while True:
            if eventHandler.newcmd:
                eventHandler.newcmd = False
                call(eventHandler.cmd,shell=True)

    except KeyboardInterrupt:
        observer.stop()
    observer.join()
