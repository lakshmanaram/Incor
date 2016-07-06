import sys
import os
from watchdog.observers import Observer
import incor
from EventHandler import EventHandler


def main():

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if path == '--version':
        print('incor v' + incor.__version__)
        return
    observer = Observer()
    eventHandler = EventHandler(path)
    observer.schedule(eventHandler, path, recursive=True)
    observer.start()
    try:
        while True:
            if eventHandler.newcmd:
                eventHandler.newcmd=False
                os.system(eventHandler.cmd)
                print "done"
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
