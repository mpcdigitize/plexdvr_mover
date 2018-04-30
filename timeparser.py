#!/usr/bin/python
import glob
import os
import datetime
from time import strptime

class TimeParser:

	def parse_timestamp(self,timestamp):
	
		t = timestamp
		struct = strptime(timestamp,"%a %b %d %H:%M:%S %Y")
		dt = datetime.datetime(struct.tm_year,struct.tm_mon,struct.tm_mday,struct.tm_hour,struct.tm_min,struct.tm_sec)
		
		return dt