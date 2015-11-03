# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:33:21 2015

@author: wbarrios
"""

import commands
import numpy as np

#Load array with IDs videos
list_indx=np.load('data/array_posic_id.npy')
youtube_ids=np.load('data/array_list_id.npy')

USA="ERROR: YouTube said: This video is available in United States only"

USA_URLS=[]
USA_IDS=[]
ERROR_URLS=[]
ERROR_IDS=[]

video_id="ERlJ0mvYroA"

word="ERROR:"

for i in range (len(youtube_ids)):
    print"///---------------------------------------------"""
    print "Iteracion: ",i
    print "Analizando el video: ",youtube_ids[i]
    cmd = "youtube-dl -j https://www.youtube.com/watch?v=%s"%youtube_ids[i]
    url="https://www.youtube.com/watch?v=%s"%youtube_ids[i]
    output = commands.getoutput(cmd)
    out=str(output)

    
    if out == USA :
        USA_URLS.append(url)
        USA_IDS.append(i)
        print "Es un link de Estados Unidos"
        print ""
        print "La ID es: ",i
       
    elif out.find(word)>= 0: 
           
        ERROR_URLS.append(url)
        ERROR_IDS.append(i)
        print "Hay un error en el link"
        print ""
        print "La ID es: ",i

        
    else:
        print "TODO OK con la posicion: ",i
        print ""

np.save('data/array_USA_URLS',USA_URLS)
np.save('data/array_USA_IDS',USA_IDS)
np.save('data/array_ERROR_URLS',ERROR_URLS)
np.save('data/array_ERROR_IDS',ERROR_IDS)




#https://www.youtube.com/watch?v=XFhdwNmgNyg