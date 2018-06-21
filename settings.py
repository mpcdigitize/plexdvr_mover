#!/usr/bin/python
import datetime
from timeparser import TimeParser

#add or remove source extension
EXTENSIONS = [".ts",".wtv"]
#do not change this extension
CONVERTED_EXTENSION = ".mp4"
#current time less how many hours?
HOURS_TO_SUBTRACT = 1
#set minimum converted file size in kilobytes
MIN_FILE_SIZE = 500000000 #500 MB
#set maximum converted file size in kilobytes
MAX_FILE_SIZE = 100000000000 #10 GB






#do not change this section
MAX_DATETIME = datetime.datetime.now() - datetime.timedelta(hours=HOURS_TO_SUBTRACT)
