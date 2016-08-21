# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 12:59:02 2016

@author: jerry
"""

def getData(fName, Tags):
    import string
    
    temp = Tags.split(',')
    tagsChk = map(string.strip, temp)
    
    with open('../../data/%s'% fName) as dataFile:
        for line in dataFile:
            temp = line.split('#')
            dataWithTags = map(string.strip, temp)
            
            for tag in tagsChk:
                if tag in dataWithTags[1:]:
                    print('\item %s' % dataWithTags[0])
                    break
                