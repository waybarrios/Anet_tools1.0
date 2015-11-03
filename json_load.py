# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 10:39:59 2015

@author: waybarrios
"""

#Librerias de Python usadas
import json 

print "  "
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
  

for i in range (len(anot_list)):
   #add name activity into list_name
   list_name.append(anot_list[i].keys())
   list_usedframe.append(anot_list[i].values())
   
x=list_usedframe[0] 
print x[0]
print list_usedframe[0]     
print len(list_usedframe)   

print len  (list_id)

print len(list_name)


print anot_list[0] 
""" 
    #Get key and value from Annotations key
    for key2,value2 in anota.items():
        #add name activity into list_name
        #print key2
        list_name.append(key2)
        #Get number of activty frames per activity in JSON file
        for i in range (len (value2)):
            x=value2[i]
            used_frame+=int(x[1]-x[0])
            
        
        #add number of activity frames into list_usedframe
        list_usedframe.append(used_frame)
        
 

print len(list_id), len(list_name),len(list_usedframe)

print list_id [0]

print list_usedframe [0]

print list_name[0]





"""
"""
archivo=my_data['I2CocZ1T9-8']

print archivo

print "     "
print "URL: ",archivo['url']
print "     "
print "SUBSET: ",archivo['subset']
print "     "
print "ANNOTATIONS: ",archivo['annotations']

anota=archivo['annotations']

for key, value in anota.items():
    print key, value
    
    
print ""
print 
print anota['Drinking coffee']
strin=anota['Drinking coffee']
#Drinking coffee
#Initialize variable
used_frame=0
#Calculate number of activity frames.
for i in range (len(strin)):
    print ""
    x=strin[i]
    print strin[i]
    used_frame+=x[1]-x[0]
    
used_frame=int(used_frame)
print "Number of Activity frames: ",used_frame, " frames"

"""