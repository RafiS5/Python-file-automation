# Overview

This file automater is a python script that monitors the downloads folder for file movements. Depending on the file endings (at the moment endings such as .stats, .docx.stats, .doc.stats, .stats.docx, or .stats.doc, .DSA, .query), files will be moved to the allocated folder. This is particularly useful for organizing files in real-time, such as keeping track of documents for a specific course or project. The file ending relate to my second year modules, allowing me to stay organized.

# Features

- The watchdog library observes the Downloads folder for specific extensions
- The "on_moved" function automatically moves matching files to a predefined folder
- All file system event handling is dealt with the _watchdog_ library

# Usage

1) Open the script file_automater.py in a text editor
2) Modify the following variables if needed
    - 'destination_folder': The folder where files will be moved
    - 'path': the folder being monitored 
3) Run the script:
    - python file_automater.py
4) The script will continue running, monitoring the folder in real-time for any file movements. If a file with a matching extension is moved into the folder, the script will automatically move it to the specified destination folder

# Requirements 
- Python 3.x
- Watchdog library(_pip install watchdog_)
