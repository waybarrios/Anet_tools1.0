# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 09:56:13 2015

@author: wbarrios
"""
Requirements:

*Youtube-dl

console: sudo apt-get youtube-dl (last version)
"""

"""
from subprocess import call
from argparse import ArgumentParser


def get_video (id_youtube):
    url="https://www.youtube.com/watch?v="+id_youtube
    cmd="youtube-dl "+url+" -o ANET_VIDEOS/"+id_youtube+".mp4"
    call(cmd.split(), shell=False)
    return
    


if __name__ == "__main__":
    parser = ArgumentParser(description="Gets video info.")
    parser.add_argument("id_youtube", help="Youtube video identifier.")
    args = vars(parser.parse_args())
    get_video(**args)
   
#    res, tbr, fps = calculate_metadata(**args)
#    
#    print "Resolution:\t\t\t\t%s" % res
#    print "Bitrate:\t\t\t\t%d kbps" % tbr
#    print "FrameRate:\t\t\t\t%d fps" % fps


    
    
    
