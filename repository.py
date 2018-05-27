#!/usr/bin/python
from directorysearcher import DirectorySearcher


class Repository:

    def __init__(self):
        self.recordings = []
        self.converted = []

    def _find_recordings(self,files):
        result = []
        for path in files:
            if not "Plex Versions" in path:
                result.append(path)
        return result

    def _find_converted(self,files):
        result = []
        for path in files:
            if "Plex Versions" in path:
                result.append(path)
        return result

    def get_recordings(self,extensions,paths):
        dir_searcher = DirectorySearcher()
        for ext in extensions:
            for path in paths:
                result = dir_searcher.get_files(ext,path)
                recordings = self._find_recordings(result)
                self.recordings.extend(recordings)
        return self.recordings

    def get_converted(self,extension,paths):
        dir_searcher = DirectorySearcher()
        for path in paths:
            result = dir_searcher.get_files(extension,path)
            converted = self._find_converted(result)
            self.converted.extend(converted)
        return self.converted

    def display(self):
        print "-----------------"
        print "RECORDINGS"
        print "-----------------"
        for item in self.recordings:
            print item
        print "Total files: ", len(self.recordings)
        print "-----------------"
        print "CONVERTED"
        print "-----------------"
        for item in self.converted:
            print item
        print "Total files: ", len(self.converted)
