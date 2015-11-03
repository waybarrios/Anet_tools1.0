# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:56:55 2015

@author: waybarrios
"""
#Python libs 
import numpy as np
import yt_info as yt


#Load array with IDs videos
list_indx=np.load('data/array_posic_id.npy')
youtube_ids=np.load('data/array_list_id.npy')


#load arrays with unavailable IDs
error_ids=np.load('data/array_ERROR_IDS.npy')
usa_ids=np.load('data/array_USA_IDS.npy')
other_errorids=np.load('data/other_array_ERROR_IDS.npy')

#ADD IDs into unique array
ids_nodisp=[]
ids_nodisp.extend(usa_ids)
ids_nodisp.extend(error_ids)
ids_nodisp.extend(other_errorids)

#Initialize array with metadata per youtube video
metadata_videos=[]

print youtube_ids[987]
print len(youtube_ids)
print len(list_indx)
print len(ids_nodisp)

print"///---------------------------------------------------"
print"///---------------------------------------------------"

print"To calculate the 28134 videos came from several sections ranging from 2000 videos."
print"For example, a value of 0 for the first 2000. For a value of 5 video ranging from 10000 to 1199 is calculated."
print "Note: The last range is from 28000-28134 to calculate the last 134 videos. The value ranges from 0 to 14 to indicate the 15 iterations"

"""
///---------------------------------------------------------------------------------

Note len(list_indx)=203 it means 203 classes on activity-net.org
For example list_indx[1] corresponds to  Drinking coffee class. 
So list_indx[1] has all indexs from  list_name,list_id, list_ uframes, list_url from Drinking
coffee videos.

///---------------------------------------------------------------------------------
"""
its=[]
ant=0
for j in range (14):
    desp=ant+2000
    its.append([ant,desp])
    ant=desp

#Last Iteration
its.append([28000,28134])
print its [0]

#Input number of iteration 
#Recall from 0 a 14, its means 15 iterations

foo=input('Please enter a value:')


#Get metadata from Youtube IDs
for i in range (its [foo][0],its [foo][1]):
    print "//------------------------------"
    print "Para i: ",i
    if  i in ids_nodisp:
        print "el video con el id: ",youtube_ids[i]
        print "[0,0,0,0]"
        metadata_videos.append([0,'0',0,0])
        print ""
   # elif i==123:
        # metadata_videos.append([188,'1920x1080',4386,30])
        
    else:
        print "el video con el id: ",youtube_ids[i]
        #Calculate metadata per video
        duration,resolution,bitrate,fps=yt.retrieve_video_info(youtube_ids[i])
        #Add metadata into metadata_videos list
        metadata_videos.append([duration,resolution,bitrate,fps])
        print [duration,resolution,bitrate,fps]
        print ""
  
np.save('data/metadata_'+str(foo),metadata_videos)

print "Tamaño total es: ", len (metadata_videos)

