#!/usr/bin/python
import glob
import os
from searcher import DirectorySearcher
from mediaparser import MediaParser
import datetime
from timeparser import TimeParser


class Service:
  
  def __init__(self):
    self.mmatched = []
    
  def _parse_info_from_path(self,files):
    parser = MediaParser()
    result =[]
    for item in files:
      media_item = parser.parse_media_item(item)
      result.append(media_item)
    return result

  def match_media_items(self,recording_extension,converted_extension,folder_path):
    
	matched = []
	
	directory = DirectorySearcher()
	timeparser = TimeParser()
	recordings = directory.get_files(recording_extension,folder_path)
	converted = directory.get_files(converted_extension,folder_path)
	media_item_recordings = self._parse_info_from_path(recordings)
	media_item_converted = self._parse_info_from_path(converted)
    
	for recording in media_item_recordings:
		for converted in media_item_converted:
			if converted.name in recording.name and converted.target_folder == recording.target_folder:
				converted.target_name = recording.name + converted.extension
				converted.target_remove_file = recording.path
				converted.datetime = timeparser.parse_timestamp(converted.timestamp)
				matched.append(converted)
	return matched
  
  