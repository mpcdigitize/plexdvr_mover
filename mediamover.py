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

class MediaMover:

	def __init__(self):
		files = []

	def move_files(self,MIN_FILE_SIZE,MAX_FILE_SIZE,FILE_IS_OLDER_THEN):

		for item in matched:
			if item.size > MIN_FILE_SIZE and item.size < MAX_FILE_SIZE:
				if item.datetime < FILE_IS_OLDER_THEN:
				files.append(item.target_remove_file)
				print item.path
				print item.target_folder + os.sep + item.target_name
				print item.timestamp
			
			
			

	def remove_files(self):

		for file in remove_files:
		print file
	#os.remove(file)
			
