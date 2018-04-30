#!/usr/bin/python
import glob
import os


class DirectorySearcher:
  
  def __init__(self):
 
    self.scanned = ["/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Conan (2010) - S08E56 - Dax Shepard; Grant Gustin; Nick Griffin.ts","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Conan (2010) - S08E57 - Hilary Swank; Zach Woods; The Lone Bellow.ts","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Conan (2010) - S08E58 - Conan Without Borders Italy.ts","/mnt/user/Media/Video/TV/The Tonight Show Starring Jimmy Fallon (2014)/Season 05/The Tonight Show Starring Jimmy Fallon (2014) - S05E83 - Katie Holmes; Brian Tyree Henry; Meghan Trainor; Bun B.ts ","/mnt/user/Media/Video/TV/The Tonight Show Starring Jimmy Fallon (2014)/Season 05/The Tonight Show Starring Jimmy Fallon (2014) - S05E87 - Drew Barrymore; Josh Radnor; Kelsey Cook.ts","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Plex Versions/Custom_ Universal TV 3864/Conan/S08E56.mp4","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Plex Versions/Custom_ Universal TV 3864/Conan/S08E57.mp4","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Plex Versions/Custom_ Universal TV 3864/Conan/S08E58.mp4","/mnt/user/Media/Video/TV/Conan (2010)/Season 08/Plex Versions/Custom_ Universal TV 3864/Conan/S08E59.mp4 ","/mnt/user/Media/Video/TV/The Tonight Show Starring Jimmy Fallon (2014)/Season 05/Plex Versions/Custom_ Universal TV 3578/The Tonight Show Starring Jimmy Fallon/S05E87.mp4","/mnt/user/Media/Video/TV/The Tonight Show Starring Jimmy Fallon (2014)/Season 05/Plex Versions/Custom_ Universal TV 3578/The Tonight Show Starring Jimmy Fallon/S05E93.mp4","/mnt/user/Media/Video/Clara/Hallmark/Back to You Me (2005)/Back to You and Me (2005).wtv","/mnt/user/Media/Video/Clara/Hallmark/Back to You Me (2005)/Plex Versions/Optimized for Mobile/Back to You and Me (2005).mp3","/mnt/user/Media/Video/Clara/Hallmark/Backyard Wedding (2011)/Backyard Wedding (2011).wtv","/mnt/user/Media/Video/Clara/Hallmark/Backyard Wedding (2011)/Plex Versions/Optimized for Mobile/Backyard Wedding (2010).mp3"]
   
  
  def get_files(self,pattern,folder_path):
    
    results = []
    for (path, dirnames, filenames) in os.walk(folder_path):
	for name in filenames:
	    if name.endswith(pattern):
	        results.append(os.path.join(path, name)) 
   
    return results