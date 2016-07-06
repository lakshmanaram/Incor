import sys
import time
from watchdog.observers import Observer

import incor
from incor import EventHandler


def main():

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if path == '--version':
        print('incor v' + incor.__version__)
        return
    observer = Observer()
    observer.schedule(EventHandler(path), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
