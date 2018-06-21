#!/usr/bin/python
import datetime
import shutil
import time
from service import Service
from settings import EXTENSIONS

folders = []

#add or remove a folder path
#folders.append("/mnt/user/path/to/your/recordings")
#folders.append("/mnt/user/path/to/your/recordings")
#folders.append("/mnt/user/path/to/your/recordings")


			  
service = Service()
service.get_files(EXTENSIONS,folders)
service.preview()

#uncomment line below to move converted files 
service.move_converted_files()

time.sleep(5)

#uncomment line below to delete original recordings
service.remove_recorded_files()


