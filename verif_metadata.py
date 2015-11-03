# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 14:33:47 2015

@author: wbarrios
"""
#Python libs
import numpy as np
import yt_info as yt
import get_videos as gtvideo
import prueba_exif_v2 as exift

"""
///----------------------------------------------------------------------

Use useful  functions

///----------------------------------------------------------------------
"""

def find (array,array2):
    new_ids=[]
    for i in range (len(array)):
        if array[i] in list(array2):
            continue
        else:
            new_ids.append(array[i])
    
    return new_ids

def verif(value,array):
    ids=[]
    for k in range (len (array)):
        if value in list(array[k]):
            ids.append(k)
            
    return ids

def none_alls (array):
    ids=[]
    x=None
    comp=list([x,x,x,x])
    for k in range (len(array)):
        if comp==list(array[k]):
            ids.append(k)
            
    return ids

def data_again(meta,ids):
     for i in range (len(ids)):
         print " "
         print "Volviendo a calcular los valores de: ",ids[i]     
         duration,resolution,bitrate,fps=yt.retrieve_video_info(youtube_ids[ids[i]])
         print [duration,resolution,bitrate,fps]
         meta[ids[i]]=[duration,resolution,bitrate,fps]
     
     return meta
     
    
"""
*********************************************************************
"""
#Initialize array with all metadata videos
metadata_videos=[]

#Initialize array used in loading array operation
load=[]

#Load array with IDs videos
youtube_ids=np.load('data/array_list_id.npy')



    
"""
///--------------------------------------------------------

***Total videos from activity-org.net= 28134 videos
***Damaged videos from activty-org.net=222 from 28134 videos

Recall to calculate metadata was used  several sections ranging from 2000 videos
For example, a value of 0 for the first 2000. For a value of 5 video ranging from 10000 to 1199 is calculated.
Note: The last range is from 28000-28134 to calculate the last 134 videos. The value ranges from 0 to 14 to indicate the 15 iterations


///-------------------------------------------------------
"""

#We have 15 iterations, so it means we have to load 15 arrays list using numpy.load()
#load array with metadata from videos

for i in range (15):
    load.append(np.load('data/metadata_'+str(i)+'.npy'))

#--------------------------------------------------------------------------------------



"""
///---------------------------------------------------------------------------

In this segment of code, the union of the arrays was done. 
Considering  list_name,list_id, list_ uframes, list_url located on json_loadv3.py script 
corresponding to 28134 videos from JSON on activity-net.org

///-------------------------------------------------------------------------
"""

for i in range (15):
     for j in range (len (load[i])):
         metadata_videos.append(load[i][j])


print len(metadata_videos)

np.save('data/old_metadata_videos',metadata_videos)
print metadata_videos[5958]


"""
///---------------------------------------------------------------------------

Proceed to verify that there are no data with value= "None" since 
this happens because these values weren't calculated by response time of Youtube's server.

///---------------------------------------------------------------------------
"""
#Initialize none array where any data="None" (Resolution, Duration, Bitrate or FPS) Note: At least one parameter="None"

none_ids=verif(None,metadata_videos)    

print none_ids


"""
///---------------------------------------------------------------------------


///---------------------------------------------------------------------------
"""


metadata_videos=data_again(metadata_videos,none_ids)

#for i in range (len(none_ids)):
#     print ""
#     print "Volviendo a calcular los valores de: ",none_ids[i]
#     
#     
#     duration,resolution,bitrate,fps=yt.retrieve_video_info(youtube_ids[none_ids[i]])
#     print [duration,resolution,bitrate,fps]
#     metadata_videos[none_ids[i]]=[duration,resolution,bitrate,fps]
# 


    
allnones_ids=none_alls(metadata_videos)
np.save('data/other_array_ERROR_IDS',allnones_ids)
#update none_ids array
none_ids=verif(None,metadata_videos)  


print "********************************************************************************"
print "Segunda toma de datos"


print "todos son nones: ", len(allnones_ids)
print allnones_ids

print " Al menos un none en:", len(none_ids)
print none_ids

#Get array without all None values
without_allnone=find(none_ids,allnones_ids)

print " Sin los 4 nones"

print without_allnone 

print "Tamaño de: ",len(without_allnone )

#Put [0,'0',0,0] in damaged videos

for i in range (len(allnones_ids)):
    metadata_videos[allnones_ids[i]]=[0,'0',0,0]


"""    
///---------------------------------------------------------------------------------------------

At least one value that is different from None.
It corresponds to the following IDs:
[6535, 8024, 9408, 12807, 18309, 18794, 19714, 20414, 20509, 24310, 26255, 27996]


We proceed to another method of downloading the video 
using the get_videos.py script and then calculate the metadata using prueba_exifv2.py



////    
"""
#Download videos from Youtube server
for i in range (len(without_allnone)):
    gtvideo.get_video(youtube_ids[without_allnone[i]])


#Calculate metadata videos using exiftool


for i in range (len(without_allnone)):
    path= "ANET_VIDEOS/"+youtube_ids[without_allnone[i]]+".mp4"
    print "Analizando el video: ",path
    """
    It is not possible to calculate the bitrate information to video: https://www.youtube.com/watch?v=RDBtFlDX9D0.
    By fact, information was calculated by a third application and entered manually.
    
    url: http://www.dr-lex.be/info-stuff/videocalc.html
    """
    if youtube_ids[without_allnone[i]]=="RDBtFlDX9D0":
        r='320x240'
        f=15
        b=230
    else:
        r,f,b=exift.calculate_metadata(path)
    
    metadata_videos[without_allnone[i]][1]=r
    metadata_videos[without_allnone[i]][2]=b
    metadata_videos[without_allnone[i]][3]=f
        

np.save('data/array_metadata_videosv3',metadata_videos)

      