# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 15:05:12 2015

@author: wbarrios
"""
#Python lib
import numpy as np
import collections
import matplotlib.pyplot as plt
import os, sys


"""
///----------------------------------------------------------------------

Use useful  functions

///----------------------------------------------------------------------
"""
def ratio (array1,array2):
    """ Calculate total frames per video.
    
            Args:
                - array1
                - array2
                
            Return:
                -array3: [Array] Ratio between array 1 and array2
               
    """
    array3=[]
    
    if len(array1)==len(array2):    
        for i in range (len(array1)):
            if  array2[i]==0: 
                """
                Recall  0 means Video not available.
                Division by zero is not allowed for it puts the value of 0. 
                The list of URL is in error_urls_update.txt and usa_urls_update.txt
                 
                Note:"0" means an unavailable video, in order to maintain the positions of 28134 videos and 
                thus don't create another array (If this happens positions is lost). 
                However, when graphing data occurs these info (Zeros) won't be taken into account 
                since there aren't information about metadata.          
                """
                temp=0
            else:
                temp=float (float(array1[i])/float(array2[i]))
               
                       
            array3.append(temp)
    return array3

def calc_total_frames (meta,uframes):
    """ Calculate total frames per video.

        Args:
            - vmeta: Array with all metadata videos
            -uframes: Array with number of activity frames
            
        Return:
            -frames: [Array] Ratio: Activity frames/Total Frames per video.
           
    """
    frames=[]
    for i in range (len(meta)):
        #Calculate total frames per video
        # Total frames= Frame per second * duration  (in seconds)
        #meta[i][0] has Duration data and meta[i][3] has VideoFrameRate 
        frames.append(int(meta[i][0])*int(meta[i][3]))
    return frames
    
def extract_metadata(position,meta):
    """
    This function extracts all specific information from metadata videos array. 
    The length of the output array corresponds to 28134 
    that is the whole videos analysands on JSON activity-net.org
    
    Then the values following of position means:
    
    Position = 1 the output array contains the resolution of the videos
    Position = 2 the output array contains bitrate videos
    Position = 3 the output array contains FPS videos
    
        Args:
            -position: data position into  meta array 
            -meta: Array with metadata videos
            
            
        Return:
            -array: [Array] Array with any metadata (Resolution,Bitrate,FPS, or ratio frames activity/total).
    
    """
    
    array=[]
    
    for i in range(len(meta)):
        array.append(meta[i][position])
    
    return array
    

def perclass (array,class_ids):
    """
    This function organizes metadata information regarding 
    class of each video (based on the organization of classes activity-net.org)
   

        Args:
         
            -Array: Array with the information to be organized
            -class_ids: Array with index videos per class
            
            
        Return:
            -Array2: [Array] any metadata info per class (Resolution,Bitrate,FPS, ratio frames activity/total).
            Note: len (Array2)=203 (# Classes)
            
            Array2[1] has all info depends of input array's values from Drinking coffee class
            
            For example:
            If input array has info about resolution,
            so array[1] has all info about  resolution 
            of all videos from Drinking coffee class.
            
            Class names is located in path: data/array_classes.npy 
            
            
    """
    array2=[]
    for i in range (len(class_ids)):
        temp=[]
        for j in range (len(class_ids[i])):
            temp.append(array[class_ids[i][j]])
        array2.append(temp)
        
    
    return array2
    
def eliminate_value(value,array):
    array2=[]
    for i in range(len(array)):
        if array[i]==value:
           continue
        else:
            array2.append(array[i])
    return array2
    
def plot_bar_chart(x_axis,freq,unit,category,rota,font,path):
    
    plt.figure(figsize=(26,15))
    plt.bar(range(len(freq)),freq, align='center',width=1,color='r')
    plt.xticks(range(len(x_axis)),x_axis,size='small',fontsize=font,rotation=rota)#size='small'
    plt.yticks(fontsize=font)
    
    if unit=="Ratio":
        plt.xlabel("VIDEO")
        plt.ylabel('RATIO (%)')
        axes = plt.gca()
        axes.set_ylim([0,100])
    else:
        plt.xlabel(unit)
        plt.ylabel('Frequency (# Videos)')
        
    plt.title("Histogram of "+category+" : "+unit)
    plt.autoscale(True)
    plt.get_scale_names()
    plt.grid(True)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.savefig(path,papertype='letter',orientation='landscape')
    plt.show()
    plt.close()
    
    
    
    
    
    return

def create_folders (array):
    
    for i in range (len(array)):
        newpath = 'graphs/'+array[i] 
        if not os.path.exists(newpath): os.makedirs(newpath)
    
    
def plot_perclass (unit_perclass,names,unit,rota,font):
    
    if unit=="Resolution(pixels)":
        value='0'
        opc=1
    elif unit=="Ratio":
        value=0
        opc=2
    else:
        value=0
        opc=3
    
    for i in range (len(unit_perclass)):
        print "-----------------------------------------------------------------------"
        print "Plotting con i=",i
        print "CLASE:",names[i]
        print ""
        
        temp=unit_perclass[i]
        #Array with unit info without zeros
        temp_nozeros=eliminate_value(value,temp)
        if opc==1:
            array_plot=collections.Counter(sorted(temp_nozeros))
            x_axis=array_plot.keys()
            y_axis=array_plot.values()
            
        elif opc==2:
            print "entre ratio"
            y_axis=temp_nozeros
            print "valor maximo", max(temp_nozeros)
            print "tamaño: ",len(temp_nozeros)
            x_axis=[i+1 for i in range(len(temp_nozeros))]
            
        else: #OPC FPS
            temp_nozeros=np.array(temp_nozeros)
            temp_nozeros=map(int, temp_nozeros)            
            array_plot=collections.Counter(temp_nozeros)
            x_axis=array_plot.keys()
            y_axis=array_plot.values()
        
        path = 'graphs/'+names[i]+'/'+unit+'.png'
        plot_bar_chart(x_axis, y_axis,unit,names[i],rota,font,path)
       
    return
            
  
      
            
def calc_hist_bitrate (bitrate,path,title):

    bitrate=np.array(bitrate)
    bitrate=map(int, bitrate)
    bitrate_nozeros=eliminate_value(0,bitrate)
    xmax=max(bitrate_nozeros)
    xmin=min(bitrate_nozeros)
    rang=xmax-xmin
    
    """
    STURGES's LAW:

    log(N)*3.322 + 4  round to closest integer 
    19=#bins

    """
    bins=int (round (np.log10(len(bitrate_nozeros))*3.322 + 4))
    step=rang/bins
    bins_array=np.linspace(xmin, xmax, (xmax-xmin)/step)
    bins_array=np.around(bins_array,decimals=0)
    bins_array=map(int,bins_array)
    
    #Compute Histogram
    bit_hist,bit_bin=np.histogram(bitrate_nozeros,bins=bins_array)
    
    plt.figure(figsize=(26,15))
    plt.bar(range(len(bit_hist)),bit_hist, align='center',width=1,color='r')
    plt.xticks(range(len(bins_array)),bins_array,size='small',fontsize=12,rotation="horizontal")#size='small'
    plt.yticks(fontsize=12)
    axes = plt.gca()
    axes.set_xlim([min(bins_array),max(bins_array)])
    axes.set_ylim([min(bit_hist),max(bit_hist)])
    plt.title("Histogram of "+str(title)+" :  Bitrate (KBPS)")
    plt.xlabel("BINS (KBPS)")
    plt.ylabel('Frequency (#Videos)')
    plt.autoscale(True)
    plt.get_scale_names()
    plt.grid(True)
    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.savefig(path,papertype='letter',orientation='landscape')
    plt.show()
    plt.close()
    
    return 
    
def bitrate_perclass(unit_perclass,names):
    
    for i in range (len(unit_perclass)):
        path='graphs/'+names[i]+'/'+'Bitrate(KBPS)'+'.png'
        print "-----------------------------------------------------------------------"
        print "Plotting con i=",i
        print "CLASE:",names[i]
        print ""
        calc_hist_bitrate(unit_perclass[i],path,names[i])    
    
    

              
"""    
*********************************************************************
"""


#Load array with index videos per class.
posid_perclass=np.load('data/array_posic_id.npy')

#Load array with class names
class_names=np.load('data/array_classes.npy')

#Load array with metadata videos (all 28134 videos on activity-net.org)
metadata=np.load('data/array_metadata_videosv3.npy')

#load array with number of activity frames per video
used_frames=np.load('data/array_list_usedframes.npy')

"""

CREATE FOLDERS WITH GRAPHS PER CLASS

"""

#Create folders with graphs per class
create_folders(class_names)


#Calculate total frames per video
total_frames=calc_total_frames (metadata,used_frames)

#Calculate ratio between activity frames and total frames per video
ratio_frames=ratio(used_frames,total_frames)

"""
/////////////////////////////////////////////////////////
"""
cnt=0
for i in range(len(ratio_frames)):
    if (ratio_frames[i]>=1):
        cnt+=1
        print i
print "Total",cnt

"""
////////////////////////////////////////////////////////
"""
#Array with info about Resolution (all video)
resolu_all=extract_metadata(1,metadata)

#Array with info about Bitrate (all video)
bit_all=extract_metadata(2,metadata)


#Array with info about FPS (all video)
fps_all=extract_metadata(3,metadata)
fps_all=np.array(fps_all)
fps_all=map(int, fps_all)




#Array with info about ratio frames per class
ratio_perclass=perclass(ratio_frames,posid_perclass)

#Array with info about ratio frames per class
resol_perclass=perclass(resolu_all,posid_perclass)

#Array with info about ratio frames per class
bit_perclass=perclass(bit_all,posid_perclass)

#Array with info about ratio frames per class
fps_perclass=perclass(fps_all,posid_perclass)

"""

PLOTTING FPS:ALL VIDEOS


"""
#Ploting FPS All videos
fps_counter=collections.Counter(fps_all)
#plot_bar_chart(fps_counter.keys()[1:],fps_counter.values()[1:],"Video_Frame_Rate(FPS)","All_Videos","horizontal",12,'graphs/All_Videos_info/Video_Frame_Rate(FPS)_All_Videos.png')

"""

PLOTTING RESOLUTION:ALL VIDEOS


"""

#Array with resolution info without zeros
resl_out_0=eliminate_value('0',resolu_all)
res_w0=collections.Counter(sorted (resl_out_0))

#Separate array to aid visualization
r_axis_y=[res_w0.values()[0:122],res_w0.values()[122:244],res_w0.values()[244:366],res_w0.values()[366:480]]
r_axis_x=[res_w0.keys()[0:122],res_w0.keys()[122:244],res_w0.keys()[244:366],res_w0.keys()[366:480]]

#Plotting 4 parts about resolution info (all videos)
#plot_bar_chart(r_axis_x[0],r_axis_y[0],"Resolution(pixels)","All_Videos_Part1","vertical",12)
#plot_bar_chart(r_axis_x[1],r_axis_y[1],"Resolution(pixels)","All_Videos_Part2","vertical",12)
#plot_bar_chart(r_axis_x[2],r_axis_y[2],"Resolution(pixels)","All_Videos_Part3","vertical",12)
#plot_bar_chart(r_axis_x[3],r_axis_y[3],"Resolution(pixels)","All_Videos_Part4","vertical",12)



"""
PLOTTING BITRATE ALL VIDEOS

"""
#calc_hist_bitrate (bit_all,'graphs/All_Videos_info/Bitrate(KBPS)_All_Videos.png','All_Videos')


"""
PLOTTING BITRATE PER CLASS
"""
#bitrate_perclass(bit_perclass,class_names)



"""

PLOTTING FPS PER CLASS

"""


#plot_perclass (fps_perclass,class_names,'Video_Frame_Rate(FPS)',"vertical",12)


"""

PLOTTING RESOLUTION PER CLASS

"""
#plot_perclass (resol_perclass,class_names,'Resolution(pixels)',"vertical",14)


"""

PLOTTING RATIO PER CLASSS

"""

#plot_perclass (ratio_perclass,class_names,'Ratio',"vertical",14)






