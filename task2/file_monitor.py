#!/usr/bin/env python3
import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileEventHandler(FileSystemEventHandler):
    def __init__(self, log_file):
        self.log_file = log_file
        logging.basicConfig(filename=log_file, 
                           level=logging.INFO,
                           format='%(asctime)s - %(message)s',
                           datefmt='%Y-%m-%d %H:%M:%S')
        
    def on_created(self, event):
        if not event.is_directory:
            logging.info(f"File created: {event.src_path}")
    
    def on_deleted(self, event):
        if not event.is_directory:
            logging.info(f"File deleted: {event.src_path}")
            
    def on_modified(self, event):
        if not event.is_directory:
            logging.info(f"File modified: {event.src_path}")
            
    def on_moved(self, event):
        if not event.is_directory:
            logging.info(f"File moved from {event.src_path} to {event.dest_path}")

def monitor_directory(path):
    log_file = "log.txt"
    event_handler = FileEventHandler(log_file)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        print(f"Monitoring directory: {path}")
        print(f"Events are being logged to: {log_file}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python file_monitor.py <directory_path>")
        sys.exit(1)
        
    directory_path = sys.argv[1]
    monitor_directory(directory_path)
