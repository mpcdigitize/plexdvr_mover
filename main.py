#!/usr/bin/python
import datetime
import shutil
import time
from service import Service

#add or remove source file extension
extensions = [".ts",".wtv",".mkv",".mp4"]

folders = []

#add or remove a path to your recorded shows and movies
folders.append("/mnt/user/path/to/your/recordings")



			  
service = Service()
service.get_files(extensions,folders)
service.preview()

#uncomment line below to move converted files 
#service.move_converted_files()

time.sleep(5)

#uncomment line below to delete original recordings
#service.remove_recorded_files()


