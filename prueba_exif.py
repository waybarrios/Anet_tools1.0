# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 12:28:59 2015

@author: waybarrios

This script extracts metadata from videos and image files 
using exiftool. Also add lib pyexiftool from github.

git clone git://github.com/smarnach/pyexiftool.git

Note: Exiftool have to be installed on Ubuntu or Linux UNIX

Terminal: sudo apt-get install libimage-exiftool-perl

"""

import exiftool

#Path file
files = "prueba.mp4"

#execute py exiftool script from lib
with exiftool.ExifTool() as et:
    #get metadata from file
    metadata = et.get_metadata(files)

print metadata
print ""
print "Avg Bitrate_QUICKTIME: ",metadata['QuickTime:AverageBitrate'],"bps"
print "Avg Bitrate: ",metadata['Composite:AvgBitrate'],"bps"
print "Resolution: ",metadata['Composite:ImageSize']," pixels"
print "Video frame rate: ",metadata['QuickTime:VideoFrameRate']," fps"
