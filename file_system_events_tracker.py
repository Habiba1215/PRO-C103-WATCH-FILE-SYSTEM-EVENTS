import sys
import time 
import shutil
import os
import random
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/salma/OneDrive/Desktop/WhiteHatJr/PRO-C102 AUTOMATE FILE SEGREGATION/Document_Files"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"hey {event.src_path} has been created !")

    def on_deleted(self,event):
        print(f"Oops! Someone deleted {event.src_path} !")
    
    def on_modified(self, event):
        print(f"Someone has modified {event.src_path}!")

    def on_moved(self,event):
        print(f"File location of {event.src_path} has been changed or the file has been renamed")

event_handler = FileEventHandler()
observer = Observer()
observer.schedule(event_handler, from_dir, recursive=True)
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop()