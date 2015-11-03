# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:08:56 2015

@author: wbarrios
"""

import commands
import numpy as np

usa_url=np.load('data/array_USA_URLS.npy')

error_urls=np.load('data/array_ERROR_URLS.npy')

error_ids=np.load('data/array_ERROR_IDS.npy')
usa_ids=np.load('data/array_USA_IDS.npy')


#print usa_ids
print ""
#print error_ids

usa=np.array_str(usa_url)

print usa[1]

print len(usa)
print ""
print len(usa_url)


print ""
print usa_url
#np.savetxt('usa_urls',usa_url)


ids_nodisp=[]
ids_nodisp.extend(usa_ids)
ids_nodisp.extend(error_ids)
#list(set(usa_ids + error_ids))
print ids_nodisp

print len(ids_nodisp)
print len(usa_ids)+len(error_ids)




file_usa = open("usa_urls_update.txt","w")


for i in range (len(usa_url)):
    
    file_usa.write(np.array_str(usa_url[i]))
    file_usa.write("\n")

    

file_usa.close()

file_error = open("error_urls_update.txt","w")


for i in range (len(error_urls)):
    
    file_error.write(np.array_str(error_urls[i]))
    file_error.write("\n")

    

file_error.close()

print len(usa_ids)
print len(error_ids)
    
    
    
    


