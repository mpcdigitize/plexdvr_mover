#!/usr/bin/python

import glob
import os
from searcher import DirectorySearcher
from mediaparser import MediaParser
from service import Service
import datetime
from timeparser import TimeParser
from time import strptime
import shutil
import time
from mediamover import MediaMover

HOURS_TO_SUBTRACT = 24
#500MB
MIN_FILE_SIZE = 500000000
#2.5GB
MAX_FILE_SIZE = 2500000000
FILE_IS_OLDER_THEN = datetime.datetime.now() - datetime.timedelta(hours=HOURS_TO_SUBTRACT)

mover = MediaMover()
service = Service()
 
#print FILE_IS_OLDER_THEN

folders = []
folders.append("/mnt/user/Media/Video/TV/ESPN FC (2013)")
folders.append("/mnt/user/Media/Video/TV/Conan (2010)")
folders.append("/mnt/user/Media/Video/TV/The Tonight Show Starring Jimmy Fallon (2014)")

for folder_path in folders:
	#print folder_path
	matched = service.match_media_items(".ts",".mp4",folder_path)

print "MOVE FILES"
print "------------"
for item in matched:
    if item.size > MIN_FILE_SIZE and item.size < MAX_FILE_SIZE:
		if item.datetime < FILE_IS_OLDER_THEN:
			remove_files.append(item.target_remove_file)
			print item.path
			print item.target_folder + os.sep + item.target_name
			print item.timestamp
			print item.datetime - datetime.timedelta(hours=HOURS_TO_SUBTRACT)
			print item.size
			#shutil.move(item.path,item.target_folder + os.sep + item.target_name)
			#os.remove(item.target_remove_file)
			
time.sleep(5)

print "REMOVE FILES"
print "---------------"
			
for file in remove_files:
	print file
	#os.remove(file)
			
