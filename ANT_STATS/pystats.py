# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:01:25 2015

@author: waybarrios
"""

import os, json
import collections
import matplotlib.pyplot as plt
import numpy as np
import plotly.plotly as py
from plotly.graph_objs import *


def get_index(index1,index2):
    posic_id=[]
    for i in range (len(index1)):
    #Initialize temp array with indexs per name
        temp=[]
        for j in range (len(index2)):
            if index1[i]==index2[j]:
                temp.append(j)
        posic_id.append(temp)
    return posic_id
    
def load_json (paths):
    data=[]
    for i in range (len (paths)):
        data.append(json.loads(open("results.global/"+paths[i]).read()))
    return data
    
def verif_values (json_array,ids):
    output=[]
    for i in range (len (ids)):
        cnt1=0
        cnt2=0
        cnt3=0
        for j in ids[i]:
            related=json_array[j]['isRelated']
            positive=json_array[j]['isPositive']
            if related==True and positive==True:
                cnt1+=1
            elif related==True and positive==False:
                cnt2+=1
            else:
                cnt3+=1
        output.append([cnt1,cnt2,cnt3])
    return output
    
def calculate_percent(part_array):
    vect1=[]
    vect2=[]
    vect3=[]
    
    for i in range (len (part_array)):
        rel_posit= (float(part_array[i][0])/sum(part_array[i]))*100
        rel=(float(part_array[i][1])/sum(part_array[i]))*100
        not_rel=(float(part_array[i][2])/sum(part_array[i]))*100
        vect1.append(rel_posit)
        vect2.append(rel)
        vect3.append(not_rel)        
        
    return vect1,vect2,vect3
           
        
#Read JSON file
get_data = json.loads(open("anet_temporal.json").read())['database']

#Get path from older called results.global
path_to_json = 'results.global'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

#Array with json data per videoid
json_data=load_json(json_files)

#Get video ids
video_ids= [json_files[idx][0:json_files[idx].index('.json')] for idx in range (len( json_files))]

#Activities list
class_videos=[get_data[video_ids[idx]].keys()[0] for idx in range (len(video_ids))]
cnt=collections.Counter(class_videos)
names=cnt.keys()


#Get array positions
array_ids=get_index(cnt.keys(),class_videos)

out=verif_values (json_data,array_ids)



#Partition into 4 groups

#Data
part1=out[0:51]
part2=out[51:102]
part3=out[102:153]
part4=out[153:203]

#Activities
nam1=names[0:51]
nam2=names[51:102]
nam3=names[102:153]
nam4=names[153:203]


#Calculate percentages

rel_true1,rel1,notrel1=calculate_percent(part1)
rel_true2,rel2,notrel2=calculate_percent(part2)
rel_true3,rel3,notrel3=calculate_percent(part3)
rel_true4,rel4,notrel4=calculate_percent(part1)




#plt.figure(1)
#plt.bar(nam1, rel_true1,width=0.2,color='b',align='center')
#plt.bar(nam1, rel1,width=0.2,color='g',align='center')
#plt.bar(nam1, notrel1,width=0.2,color='r',align='center')
#
#
#plt.show()




#Sorting list in descent order

reltrue1_sorter=[y for (x,y,w,z) in sorted (zip (notrel4,rel_true4,rel4,nam4),reverse=True) ]
rel1_sorter=[w for (x,y,w,z) in sorted (zip (notrel4,rel_true4,rel4,nam4),reverse=True) ]
nam1_sorter=[z for (x,y,w,z) in sorted (zip (notrel4,rel_true4,rel4,nam4),reverse=True) ]
notrel1_sorter=sorted (notrel4,reverse=True)

#print sorted (zip (notrel1,rel_true1,rel1,nam1),reverse=True)
#
#s=[y for (x,y) in sorted (zip (notrel1,rel_true1,rel1,nam1),reverse=True) ]
#print s
#
#nam2_sorter=[y for (x,y) in sorted(zip (notrel2,nam2),reverse=True) ]
#notrel2_sorter=sorted (notrel2,reverse=True)
#
#nam3_sorter=[y for (x,y) in sorted(zip (notrel3,nam3),reverse=True) ]
#notrel3_sorter=sorted (notrel3,reverse=True)
#
#nam4_sorter=[y for (x,y) in sorted(zip (notrel4,nam4),reverse=True) ]
#notrel4_sorter=sorted (notrel4,reverse=True)


#data = Data([
#    Bar(
#        x=nam4_sorter,
#        y=np.array(notrel4_sorter),
#        name='No related videos'
#    )
#])
#
#layout = Layout(
#    title='NO RELATED VIDEOS PART 4',
#    #width=1920,
#    #height=1080,
#    
#    
#     yaxis=YAxis(
#        title='Percentage (%)',
#        titlefont=Font(
#           
#            size=14
#            
#        )
#    )
#    
#)
#
#fig = Figure(data=data, layout=layout)
#py.plot(fig, filename='NO RELATED VIDEOS PART 4')
#
#
#
#

trace1 = Bar(
    x=nam1_sorter,
    y=np.around(reltrue1_sorter, decimals=1),
    name='Related and True Positive'
)
trace2 = Bar(
    x=nam1_sorter,
    y=np.around(rel1_sorter, decimals=1),
    name='Related and False Positive'
)

trace3 = Bar(
    x=nam1_sorter,
    y=np.around(notrel1_sorter, decimals=1),
    name='No Related'
)

data = Data([trace1, trace2,trace3])
layout = Layout(
    title='PART 4 SORTED BY NO RELATED VIDEOS',
    #width=1920,
    #height=720,
    barmode='group',
       yaxis=YAxis(
        title='Percentage (%)',
        titlefont=Font(
           
            size=14
            
        )
)
)
fig = Figure(data=data, layout=layout)
py.plot(fig, filename='PART 4')
