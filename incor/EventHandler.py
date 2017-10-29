import os
import signal
from watchdog.events import FileSystemEventHandler
from subprocess import call
import psutil


class EventHandler(FileSystemEventHandler):

    """
    The class inherited from watchdog.events.FileSystemEventHandler, overrides
    the functions on_modified() and on_created() from the base class.
    """

    def __init__(self, path, compilers):
        self.path = path
        self.TemplateName = ''
        self.newCmd = False
        self.parentPid = None
        self.cmd = None
        self.lastCall = ''
        self.compilers = compilers

    def on_modified(self, event):
        """
        Overrides the function on_modified() from the base class

        :param watchdog.events.FileModifiedEvent event:
        Specifies the type of event

        """

        if not event.is_directory:
            # Checks whether the created event is not a directory event
            cur_path = event.src_path
            file_extension = cur_path.split('.')[-1]

            if file_extension == 'py':
                # python files
                parent = ''
                try:
                    parent = psutil.Process(self.parentPid)
                except psutil.NoSuchProcess:
                    print('No such process')
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGKILL)
                call('clear', shell=True)
                if children:
                    print('Previously executing processes terminated')
                self.cmd = self.compilers[2] + ' ' + cur_path
                print('issuing system call - ' + self.cmd)
                self.newCmd = True

            elif file_extension == 'jl':
                # julia files
                parent = ''
                try:
                    parent = psutil.Process(self.parentPid)
                except psutil.NoSuchProcess:
                    print('No such process')
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGKILL)
                call('clear', shell=True)
                if children:
                    print('Previously executing processes terminated')
                self.cmd = self.compilers[3] + ' ' + cur_path
                print('issuing system call - ' + self.cmd)
                self.newCmd = True

            elif file_extension == "cpp":
                # cpp files
                parent = ''
                try:
                    parent = psutil.Process(self.parentPid)
                except psutil.NoSuchProcess:
                    print('No such process')
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGKILL)
                call('clear', shell=True)
                if children:
                    print('Previously executing processes terminated')
                out_path = cur_path[:-3] + 'out'

                if os.path.isfile(out_path):
                    # removes the existing output file
                    self.cmd = 'rm ' + out_path
                    print('issuing system call - ' + self.cmd)
                    call(self.cmd, shell=True)

                # compiles the cpp program
                self.cmd = self.compilers[0] + \
                    ' ' + cur_path + ' -o ' + out_path
                print('issuing system call - ' + self.cmd)
                call(self.cmd, shell=True)

                if os.path.isfile(out_path):
                    # if the output file has been created
                    if out_path[:2] != './':
                        out_path = './' + out_path
                    self.cmd = out_path
                    print('issuing system call - ' + self.cmd)
                    self.newCmd = True

            elif file_extension == "c":
                # c files
                parent = ''
                try:
                    parent = psutil.Process(self.parentPid)
                except psutil.NoSuchProcess:
                    print('No such process')
                children = parent.children(recursive=True)
                for process in children:
                    process.send_signal(signal.SIGKILL)
                call('clear', shell=True)
                if children:
                    print('Previously executing processes terminated')
                out_path = cur_path[:-3] + 'out'

                if os.path.isfile(out_path):
                    # removes the existing output file
                    self.cmd = 'rm ' + out_path
                    print('issuing system call - ' + self.cmd)
                    call(self.cmd, shell=True)

                # compiles the c program
                self.cmd = self.compilers[1] + \
                    ' ' + cur_path + ' -o ' + out_path
                print('issuing system call - ' + self.cmd)
                call(self.cmd, shell=True)

                if os.path.isfile(out_path):
                    # if the output file has been created
                    out_path = './' + out_path
                    self.cmd = out_path
                    print('issuing system call - ' + self.cmd)
                    self.newCmd = True

    def on_created(self, event):
        """
        Overrides the function on_created() from the base class

        :param watchdog.events.FileModifiedEvent event:
        Specifies the type of event

        """

        if not event.is_directory:
            cur_path = event.src_path
            file_extension = cur_path.split('.')[-1]
            if file_extension in ['py', 'cpp', 'c', 'jl']:
                name = self.TemplateName + '.' + file_extension
                f_created = open(cur_path, 'r+')
                if f_created.read() == '':
                    for root, dirs, files in os.walk(self.path):
                        if name in files:
                            f = open(os.path.join(root, name))
                            f_created.write(f.read())
                            f.close()
                            break
                f_created.close()
