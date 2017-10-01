import time
import sys
import os
from watchdog.observers import Observer
from termios import tcflush, TCIOFLUSH
import incor
from subprocess import call
try:
    from incor.EventHandler import EventHandler
except ImportError:
    from incor import EventHandler


def main():
    """
    The entry function for the command 'incor' in terminal
    """

    template = 'template'
    input_file = None
    compilers = ['g++', 'gcc', 'python', 'julia']
    flag_list = ['-t', '-i', '-cpp', '-c', '-py', '-jl']

    def get_arg(arg, default=None):
        try:
            global ind
            ind = sys.argv.index(arg)
            value = sys.argv[ind + 1]
            if value not in flag_list:
                sys.argv = sys.argv[:ind] + sys.argv[ind + 2:]
                return True, value
            else:
                sys.argv = sys.argv[:ind] + sys.argv[ind + 1:]
                return True, default
        except ValueError:
            return False, default
        except IndexError:
            sys.argv = sys.argv[:ind]
            return True, default

    present, template = get_arg('-t', template)
    present, input_name = get_arg('-i')
    if input_name is None and present:
        input_name = 'input.txt'
    present, compilers[0] = get_arg('-cpp', compilers[0])
    present, compilers[1] = get_arg('-c', compilers[1])
    present, compilers[2] = get_arg('-py', compilers[2])
    present, compilers[3] = get_arg('-jl', compilers[3])

    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    if path == '--version':
        print('incor v' + incor.__version__)
        return
    elif path == '-h' or path == '--help':
        print("""incor can be configured for a run using these options -

    -i   : To specify the input file name for the to be compiled program
    (with extension).
    -t   : To specify the name of template file(without extension).
    -c   : To specify the C compiler to be used.
    -cpp : To specify the C++ compiler to be used.
    -py  : To specify the python interpreter to be used.
    -jl  : To specify the julia interpreter to be used.

        """)
        return
    else:
        sys.argv = sys.argv[1:]
        path = " ".join(sys.argv) if len(sys.argv) > 0 else '.'
        os.chdir(path)
        path = '.'

    if input_name is not None:
        for root, dirs, files in os.walk(path):
            if input_name in files:
                input_file = os.path.join(root, input_name)
                break
        if input_file is None:
            print(input_name + ' not found')
    eventhandler = EventHandler(path, compilers)
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

                start_time = time.time()
                # creates a child process that executes the final command
                if input_file is not None:
                    input_fd = open(input_file, 'r')
                    call(eventhandler.cmd, shell=True, stdin=input_fd)
                    input_fd.close()
                else:
                    call(eventhandler.cmd, shell=True)
                print('\n---------------------------------------------------')
                print('Program execution terminated in %s seconds.' %
                      (time.time() - start_time))
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
