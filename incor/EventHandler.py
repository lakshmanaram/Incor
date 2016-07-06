import os

from watchdog.events import FileSystemEventHandler


class EventHandler(FileSystemEventHandler):

    # TODO Add docstrings

    def on_modified(self, event):
        cur_path = ""
        if event.is_directory is False:
            cur_path = event.src_path
        print(cur_path.split('.'))
        file_extension = cur_path.split('.')[-1]
        if file_extension == "py":
            print("issuing system call - python " + cur_path)
            os.system("python " + cur_path)

