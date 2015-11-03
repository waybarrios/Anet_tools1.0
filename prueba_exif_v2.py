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
from argparse import ArgumentParser

def calculate_metadata (path_video):
    with exiftool.ExifTool() as et:
        #Execute py exiftool script from lib
        #with exiftool.ExifTool() as et:
        #Get metadata video
        
        metadata = et.get_metadata(path_video)
        resolution=str(metadata['Composite:ImageSize'])
        
                
        for key, value in metadata.items():
           
            if key.find('VideoFrameRate')>=0:
                fps=int (round(metadata[key]))
                
            if key.find('AverageBitrate')>=0:
                bitrate=metadata[key]/1000 #unit=Kbps
            
        
              
#        print metadata
#        fps=int (round(metadata['QuickTime:VideoFrameRate']))
       
#        bitrate=metadata['QuickTime:AverageBitrate']/1000 #unit=Kbps
#        fps,bitrate=None,None
    return resolution,fps, bitrate
        
def calc_totalframes (time,fps):
    #Calculate number of frames per video
    frames=time*fps
    return frames 
  


if __name__ == "__main__":
    parser = ArgumentParser(description="Gets video info.")
    parser.add_argument("path_video", help="Youtube video identifier.")
    args = vars(parser.parse_args())
    res, fps,tbr  = calculate_metadata(**args)
    
    print "Resolution:\t\t\t\t%s" % res
    print "Bitrate:\t\t\t\t%d kbps" % tbr
    print "FrameRate:\t\t\t\t%d fps" % fps

