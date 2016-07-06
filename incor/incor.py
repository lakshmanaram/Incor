import time
import sys
import os
from watchdog.observers import Observer
import incor
from EventHandler import EventHandler
# import psutil

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
    # parent = None
    # try:
    #     parent = psutil.Process(eventHandler.parentpid)
    # except psutil.NoSuchProcess:
    #     print 'No such process'
    # eventHandler.existing_Children = parent.children(recursive=True)
    try:
        while True:
            p = eventHandler.p
            if p is not None:
                fr = open('tmpout', 'r')
                p.poll()
                if p.returncode is not None:
                    p.communicate()
                while p.returncode is not None:
                    print fr.read()
                    if p is not None:
                        p.stdin.write(raw_input()+"\n")
                    print fr.read()
                    p.poll()
                fr.close()
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
