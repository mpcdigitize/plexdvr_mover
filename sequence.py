#!/usr/bin/python
import pandas as pd
from mediaitem import MediaItem

class Sequencer(object):
    
  
  def _get_data_frame(self,files):
  
    df = pd.DataFrame(columns=["index","file_name","full_name","path","extension","file_size","timestamp","datetime",
				   "parent_directory","main_folder_name","target_folder","target_name",
				   "target_remove_file","sequence_pattern"])
    
    files.sort(key=lambda r: r.file_name)
    files.sort(key=lambda r: r.datetime)
    x = 0
    for f in files:
        x = x + 1
        df.loc[x] = [x,f.file_name,f.full_name,f.path,f.extension,f.file_size,f.timestamp,
                          f.datetime,f.parent_directory,f.main_folder_name,
                          f.target_folder,f.target_name,f.target_remove_file,f.sequence_pattern]
    
  
    df["sequence"] = df.groupby("sequence_pattern").cumcount()
	
    return df

  def get_sequence(self,files):
    df = self._get_data_frame(files)
    result = []
    for index,row in df.iterrows():
        media_item = MediaItem()
        media_item.path = row.path
        media_item.file_name = row.file_name
        media_item.file_size = row.file_size
        media_item.full_name = row.full_name
        media_item.extension = row.extension
        media_item.timestamp = row.timestamp
        media_item.target_folder = row.target_folder
        media_item.datetime = row.datetime
        media_item.sequence_pattern = row.sequence_pattern
        media_item.sequence = row.target_folder + "_" + row.sequence_pattern.rstrip().lstrip() + "_" + str(row.sequence).rstrip().lstrip()
        
        result.append(media_item)

    return result

  def get_sequence_id_from_string(self,file_name):
    
    id = ""
    if " - " in file_name:
        split_text = file_name.split(" - ")[1]
    
        if "-" in split_text:
          id = split_text.split(" ")[0]
        else:
          id = split_text
    else:
      id = file_name
    
    #print id
    return id

