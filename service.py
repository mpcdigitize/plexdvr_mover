#!/usr/bin/python
import os
import datetime
import shutil
from mediaparser import MediaParser
from repository import Repository
from directorysearcher import DirectorySearcher
from timeparser import TimeParser
from size import Size

#recording should be older than ...hours from now
HOURS_TO_SUBTRACT = 0
#set minimum converted file size in kilobytes
MIN_FILE_SIZE = 500000000 #500 MB
#set maximum converted file size in kilobytes
MAX_FILE_SIZE = 100000000000 #10 GB

#do not change this section
MAX_DATETIME = datetime.datetime.now() - datetime.timedelta(hours=HOURS_TO_SUBTRACT)
CONVERTED_EXTENSION = ".mp4"

class Service:

    def __init__(self):
        self.matched = []
        self.selected = []
        self.remove_files = []

    def _parse_info_from_path(self,files):
        parser = MediaParser()
        result =[]
        for item in files:
            media_item = parser.parse_media_item(item)
            result.append(media_item)
        return result

    def _match_media_items(self,extensions,folders):
        repository = Repository()
        directory = DirectorySearcher()
        timeparser = TimeParser()
        recordings = repository.get_recordings(extensions,folders)
        converted = repository.get_converted(CONVERTED_EXTENSION,folders)
        media_item_recordings = self._parse_info_from_path(recordings)
        media_item_converted = self._parse_info_from_path(converted)
        for recording in media_item_recordings:
            for converted in media_item_converted:
                if converted.name in recording.name and converted.target_folder == recording.target_folder:
                    converted.target_name = recording.name + converted.extension
                    converted.target_remove_file = recording.path
                    converted.datetime = timeparser.parse_timestamp(converted.timestamp)
                    self.matched.append(converted)

    def _select_files(self):
        for item in self.matched:
            if item.size > MIN_FILE_SIZE and item.size < MAX_FILE_SIZE:
                if item.datetime < MAX_DATETIME:
                    self.selected.append(item)
                    self.remove_files.append(item.target_remove_file)

    def get_files(self,extensions,folders):
        self._match_media_items(extensions,folders)
        self._select_files()

    def preview(self):
        size = Size()
        print "------------------------"
        print "DETAILS:"
        print "------------------------"
        for item in self.selected:
            print "Recorded: ", item.target_remove_file
            print "Converted: ",item.path
            print "Target: ",item.target_folder + os.sep + item.target_name
            print "DateTime: ",item.timestamp
            print "Size: ", size.convert_size(item.size)
        print "------------------------"
        print "REMOVING:"
        print "------------------------"

        for item in self.remove_files:
            print "Recording: ",item

        print "Total files: " , len(self.selected) , " to move"

    def move_converted_files(self):
        x = 0
        for file in self.selected:
            x = x + 1
            if os.path.exists(path):
              print "Moving " ,x , " of " , len(self.selected) , " - " , file.path
              shutil.move(file.path,file.target_folder + os.sep + file.target_name)
            else:
              print "Error! "  ,x , " of " , len(self.selected) , " - " , file.path

    def remove_recorded_files(self):
        x = 0
        for path in self.remove_files:
            x = x + 1
            if os.path.exists(path):
              print "Deleting " ,x , " of " , len(self.remove_files)
              os.remove(path)
              print "Success! Deleted: ",path
            else:
              print "Error! " ,x , " of " , len(self.remove_files), " " , path 


