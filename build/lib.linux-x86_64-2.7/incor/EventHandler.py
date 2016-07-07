import os
import signal
from watchdog.events import FileSystemEventHandler
from subprocess32 import call
import psutil


class EventHandler(FileSystemEventHandler):

    # TODO Add docstrings

    parentPid = None
    cmd = None
    newCmd = False
    lastCall = ''

    def __init__(self, path):
        self.path = path

    def on_modified(self, event):
        if not event.is_directory:
            # Checks whether the created event is not a directory event
            cur_path = event.src_path
            file_extension = cur_path.split('.')[-1]
            if file_extension == 'py':
                parent = ''
                try:
                    parent = psutil.Process(self.parentPid)
                except psutil.NoSuchProcess:
                    print 'No such process'
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGKILL)
                call('clear', shell=True)
                if children:
                    print 'Previously executing processes terminated'
                print('issuing system call - python ' + cur_path)
                self.cmd = 'python ' + cur_path
                self.newCmd = True

    def on_created(self, event):
        if not event.is_directory:
            cur_path = event.src_path
            file_extension = cur_path.split('.')[-1]
            if file_extension in ['py', 'cpp', 'c']:
                name = 'template.' + file_extension
                f_created = open(cur_path, 'rw')
                if f_created.read() == '':
                    for root, dirs, files in os.walk(self.path):
                        if name in files:
                            f = open(os.path.join(root, name))
                            f_created.write(f.read())
                            f.close()
                            break
                f_created.close()
