#!/usr/bin/python
import os
import time
from mediaitem import MediaItem
from timeparser import TimeParser
from sequence import Sequencer

  
        
class MediaParser:


  def _get_media_type_from_path(self, path):
    if os.sep +"Season " in path:
      media_type = "TV"
    else:
      media_type = "Movie"
    return media_type

  def _get_converted_from_path(self,path):
    if "Plex Versions" in path:
      media_converted = "True"
    else:
      media_converted = "False"
    return media_converted

 

  def _get_target_folder_name_from_path(self,path):

    media_type = self._get_media_type_from_path(path)
    media_converted = self._get_converted_from_path(path)
    result = ""

    if media_type == "TV" and media_converted == "False":
      parent_dir = os.path.abspath(os.path.join(path, os.pardir))
      result = parent_dir

    elif media_type == "TV" and media_converted == "True":
      parent_dir = os.path.abspath(os.path.join(path, os.pardir))
      parent_parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
      parent_parent_parent_dir = os.path.abspath(os.path.join(parent_parent_dir, os.pardir))
      parent_parent_parent_parent_dir = os.path.abspath(os.path.join(parent_parent_parent_dir, os.pardir))
      result = parent_parent_parent_parent_dir

    elif media_type == "Movie" and media_converted == "False":
      parent_dir = os.path.abspath(os.path.join(path, os.pardir))
      result = parent_dir

    elif media_type == "Movie" and media_converted == "True":
      parent_dir = os.path.abspath(os.path.join(path, os.pardir))
      parent_parent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
      parent_parent_parent_dir = os.path.abspath(os.path.join(parent_parent_dir, os.pardir))
      result = parent_parent_parent_dir

    else:
      result =""

    return result

  def parse_media_item(self,path):

    media_item = MediaItem()
    timeparser = TimeParser()
    sequencer = Sequencer()

    media_item.path = path
    media_item.file_name = os.path.basename(os.path.splitext(path)[0])
    media_item.file_size = os.path.getsize(path)
    media_item.full_name = os.path.basename(path)
    media_item.extension = os.path.splitext(path)[1]
    media_item.timestamp = time.ctime(os.path.getmtime(path))
    media_item.date_modified = time.ctime(os.path.getmtime(path))
    media_item.target_folder = self._get_target_folder_name_from_path(path)
    media_item.datetime = timeparser.parse_timestamp(time.ctime(os.path.getmtime(path)))
    media_item.sequence_pattern = self._get_target_folder_name_from_path(path) + "_" + sequencer.get_sequence_id_from_string(os.path.basename(os.path.splitext(path)[0]))



    return media_item
