import os
import sys
import subprocess

PROJECT_DIR = os.path.expanduser("~/Documents")

if(os.path.isdir(PROJECT_DIR)):
    print(f"Directory {PROJECT_DIR} exists.")

    print("Total number of files")
    print(len(os.listdir(PROJECT_DIR)))

    print("Total disk usage")
    files = os.listdir(PROJECT_DIR);
    files.sort(
        key=lambda file : os.path.getmtime(os.path.join(PROJECT_DIR,file)),
        reverse=True
    )
    for file in files:
        print(file)

    print("Analysis Complete")

else:
    print(f"Error:Directory {PROJECT_DIR} does not exist")
    sys.exit(1);
    

