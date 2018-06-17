#!/usr/bin/python
import os
import shutil
from mediaparser import MediaParser
from repository import Repository
from directorysearcher import DirectorySearcher
from size import Size
from sequence import Sequencer 
from settings import MAX_DATETIME
from settings import MIN_FILE_SIZE
from settings import MAX_FILE_SIZE
from settings import CONVERTED_EXTENSION


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

    def _match_media_items(self,_recordings_,_converted_):  
        for recording in _recordings_:
            for converted in _converted_:
                if converted.sequence == recording.sequence:
                    converted.target_name = recording.file_name + converted.extension
                    converted.target_remove_file = recording.path
                    self.selected.append(converted)
                    self.remove_files.append(recording.path)

    def _get_recordings(self,extensions,folders):
        repository = Repository()
        repo_recordings = repository.get_recordings(extensions,folders)
        return repo_recordings

    def _get_converted(self,extensions,folders):
        repository = Repository()
        repo_converted = repository.get_converted(CONVERTED_EXTENSION,folders)
        return repo_converted
    
    def _parse_metadata(self,files):
        parsed_metadata = self._parse_info_from_path(files)
        return parsed_metadata
        
    
    def _select_files(self,_files):
        selected_result = []
        for item in _files:
            if item.file_size > MIN_FILE_SIZE and item.file_size < MAX_FILE_SIZE:
                if item.datetime < MAX_DATETIME:
                    selected_result.append(item)
        return selected_result
        
    def _get_sequence(self,files_):
        sequencer = Sequencer()
        _files_with_sequence = sequencer.get_sequence(files_)
        return _files_with_sequence
		

    def get_files(self,extensions,folders):
        files_recorded = self._get_recordings(extensions,folders)
        files_converted = self._get_converted(CONVERTED_EXTENSION,folders)
        metadata_recorded = self._parse_metadata(files_recorded)
        metadata_converted = self._parse_metadata(files_converted)
        selected_recorded = self._select_files(metadata_recorded)
        selected_converted = self._select_files(metadata_converted)
        sequence_recorded = self._get_sequence(selected_recorded)
        sequence_converted = self._get_sequence(selected_converted) 
        self._match_media_items(sequence_recorded,sequence_converted)
        

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
            print "Size: ", size.convert_size(item.file_size)
        print "Total files: " , len(self.selected) , " to move"
        print "------------------------"
        print "REMOVING:"
        print "------------------------"

        for item in self.remove_files:
            print "Recording: ",item

        print "Total files: " , len(self.remove_files) , " to delete"
        print "------------------------"
        print "------------------------"

    def move_converted_files(self):
        x = 0
        for file in self.selected:
            x = x + 1
            if os.path.exists(file.path):
              print "Moving " ,x , " of " , len(self.selected) , " - " , file.path
              shutil.move(file.path,file.target_folder + os.sep + file.target_name)
            else:
              print "Error! "  ,x , " of " , len(self.selected) , " - " , file.path
        print "------------------------"
        print "------------------------"
        
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
        print "------------------------"
        print "------------------------"


