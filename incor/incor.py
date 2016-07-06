import sys
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
            x = raw_input()
            p = eventHandler.p
            if p is not None:
                stdout,stderr = p.communicate(x)
                print stdout
                if stderr is not None:
                    print stderr
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
