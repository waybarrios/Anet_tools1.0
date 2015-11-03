# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:39:59 2015

@author: waybarrios
"""

#Librerias de Python usadas
import json 
import numpy as np
import collections


#Read JSON file
get_data = json.loads(open("activity_net.json").read())
#Parsing Data
my_data=get_data['database']

#Initialize annotations
anot_list=[]

#Initialize ID video list 
list_id=[]

#Initialize name activity list
list_name=[]

#Initialize number of activity frames per activity/video.
list_usedframe=[]

#Initialize total of activty frames per video
total_uframes=[]

#Initialize array with URLs videos per activity
list_url=[]

for key, value in my_data.items():
    
    #print key
    #Initialize number of activity frames
    used_frame=0
    #add ID video into list_id 
    list_id.append(key)
    #get data per ID video
    data_video=my_data[key]
    #get annotations per ID video
    anota=data_video['annotations']
    anot_list.append(anota)
    
    #add url video per ID video  into list_url
    list_url.append(data_video['url'])
  

for i in range (len(anot_list)):
   #add name activity into list_name
   list_name.append(anot_list[i].keys()[0])
   #print anot_list[i].values()
   list_usedframe.append(anot_list[i].values()[0])
   #Initialize accumulator   
   cnt=0
   #determinate number of used frames
   for j in range (len( list_usedframe[i])):
       cnt+=int(list_usedframe[i][j][1]-list_usedframe[i][j][0])
   #add number of used frames into total_uframes list.    
   total_uframes.append(cnt)    
   

#Determinate frequency of names.
names_counter=collections.Counter(list_name)

#Create a name list (203 classes from activity-net.org)
real_namelist=list(names_counter)


#Initialize array with positions per activity
posic_id=[]


for i in range (len(real_namelist)):
    #Initialize temp array with indexs per name
    temp=[]
    for j in range (len(list_name)):
        if real_namelist[i]==list_name[j]:
            temp.append(j)
    
    posic_id.append(temp)
    


"""
//-------------------------
Calculate  total number of used frames per class
//------------------------
"""
#Initialize array total number of used frames per class
used_frames_class=[]



for i in range (len(real_namelist)):
    #Initialize ACC per class with total used frames
    acc=0
    for j in range (len(posic_id[i])):
        acc+=total_uframes[posic_id[i][j]]   
    
    used_frames_class.append(acc)

for i in range (len(real_namelist)):
    print "Class ",real_namelist[i]," has: ",used_frames_class[i]," used frames per class"
    print "" 

#Save array list  in Data file arrays
np.save('data/array_list_names',list_name)
np.save('data/array_list_id',list_id)
np.save('data/array_list_usedframes',total_uframes)
np.save('data/array_list_urls',list_url)
np.save('data/array_namescounter',names_counter)
np.save('data/array_classes',real_namelist)
np.save('data/array_uframesperclass',used_frames_class)
np.save('data/array_posic_id',posic_id)


