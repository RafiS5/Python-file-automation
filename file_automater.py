
import time
import os
import shutil
import logging
import json
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler 


with open('file_extensions.json' , 'r') as config_file:
    config = json.load(config_file) # File extension folder succcessfully loaded in ay python dictionary


class MyEventHandler(LoggingEventHandler):
    def on_moved(self, event):

        target_dest_path = None 

        for file_ending in config:
            if event.dest_path.lower().endswith(file_ending.lower()):
                print(f"Checking if {event.dest_path} ends with {file_ending}")
                target_file_ending = file_ending
                target_dest_path = config[file_ending] # Target file path and ending have been found
                break

        if target_dest_path is None:
            print(f"No matching file extension found for {event.dest_path}")
            return

        destination_folder = target_dest_path
        destination = os.path.join(destination_folder,  os.path.basename(event.dest_path))
            
        # Delay to ensure OS completes the move action before we try moving it again
        time.sleep(1)

        # Move the file if it still exists
        if os.path.exists(event.dest_path):
            shutil.move(event.dest_path, destination)
            print(f"File has been moved to {destination}")
        else:
            print(f"File {event.dest_path} no longer exists.")


if __name__ == "__main__":

    path = r"C:\Users\rafis\Downloads"
    # path which needs to be monitored

    event_handler = MyEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    # observer now running in a seperate thread
    try:
        while True:
            time.sleep(1)
            # loop ensures that observer is kept alive for as long as the loop is alive
    finally:
        observer.stop()
        observer.join()
        # allows for a graceful exit, incase of an interruption
    

