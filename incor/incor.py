import time
import sys
import os
from watchdog.observers import Observer
from termios import tcflush, TCIOFLUSH
import incor
from EventHandler import EventHandler
from subprocess import call


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if path == '--version':
        print('incor v' + incor.__version__)
        return
    observer = Observer()
    eventhandler = EventHandler(path)
    eventhandler.parentPid = os.getpid()  # parent process pid
    observer.schedule(eventhandler, path, recursive=True)
    observer.start()
    try:
        while True:
            if eventhandler.newCmd:
                eventhandler.newCmd = False
                sys.stdout.flush()
                sys.stdout.flush()
                tcflush(sys.stdin, TCIOFLUSH)
                # flushes the keystrokes of the previously terminated program
                call(eventhandler.cmd, shell=True)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
