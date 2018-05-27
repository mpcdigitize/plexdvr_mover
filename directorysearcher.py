#!/usr/bin/python
import os



class DirectorySearcher:

  def get_files(self,pattern,folder_path):

    results = []
    for (path, dirnames, filenames) in os.walk(folder_path):
        for name in filenames:
            if name.endswith(pattern):
                results.append(os.path.join(path, name))
        #print os.path.join(path, name)

    return results
