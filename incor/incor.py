import time
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
            p = eventHandler.p
            if p is not None:
                p.poll()
                if p.returncode is not None:
                    while True:
                        try:
                            out1 = p.stdout.read()
                        except IOError:
                            continue
                        else:
                            break
                    print p.stdout.read()
                    x = raw_input()
                    p.stdin.write(x)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
