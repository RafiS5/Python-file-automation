
import time
import os
import shutil
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler 


class MyEventHandler(LoggingEventHandler):
    def on_moved(self, event):
        if event.dest_path.endswith('.stats') or event.dest_path.endswith('.docx.stats') or event.dest_path.endswith('.doc.stats') or event.dest_path.endswith('.stats.docx') or event.dest_path.endswith('.stats.doc'):
            destination_folder = r"C:\YEAR 2\Probability and Stats"
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
    

