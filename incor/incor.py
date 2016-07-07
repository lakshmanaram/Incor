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
    template = 'template.'
    if path == '-t':
        # changes template file name for the run
        path = sys.argv[3] if len(sys.argv) > 3 else '.'
        template = sys.argv[2] if len(sys.argv) > 2 else 'template.'

    eventhandler = EventHandler(path)
    eventhandler.parentPid = os.getpid()  # parent process pid
    eventhandler.TemplateName = template

    observer = Observer()
    observer.schedule(eventhandler, path, recursive=True)
    observer.start()
    try:
        while True:
            if eventhandler.newCmd:

                # stores the status of the cmd
                eventhandler.newCmd = False

                # flushes the keystrokes of the previously terminated program
                sys.stdout.flush()
                sys.stdout.flush()
                tcflush(sys.stdin, TCIOFLUSH)

                # creates a child process that executes the final command
                call(eventhandler.cmd, shell=True, cwd=path)
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
