import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class event_handler(FileSystemEventHandler):
	def on_modified(self, event):
		cur_path = ""
		if event.is_directory is False:
			cur_path = event.src_path
		#print cur_path +" "+ cur_path[-3:]
		file_extension = cur_path[-3:]
		if file_extension==".py":
			print "issuing system call - pyhton "+cur_path
			os.system("python "+cur_path)
#			os.system("x")

if __name__ == "__main__":
	path = sys.argv[1] if len(sys.argv) > 1 else '.'
	observer = Observer()
	observer.schedule(event_handler(), path, recursive=True)
	observer.start()
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		observer.stop()
	observer.join()
