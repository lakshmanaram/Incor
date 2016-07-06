import os

from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):

    # TODO Add docstrings

    def __init__(self, path):

        self.path = path

    def on_modified(self, event):

        cur_path = ""
        if event.is_directory is False:
            cur_path = event.src_path
        print(cur_path.split('.'))
        file_extension = cur_path.split('.')[-1]
        if file_extension == "py":
            print("issuing system call - python " + cur_path)
            os.system("python " + cur_path)

    def on_created(self, event):

        cur_path = ''
        if not event.is_directory:
            cur_path = event.src_path
        file_extension = cur_path.split('.')[-1]
        name = 'template.' + file_extension
        f_created = open(cur_path, 'r+')
        if f_created.read() == '':
            for root, dirs, files in os.walk(self.path):
                if name in files:
                    f = open(os.path.join(root, name))
                    f_created.write(f.read())
                    f.close()
                    break
        f_created.close()
