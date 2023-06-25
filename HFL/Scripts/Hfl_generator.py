#!/usr/bin/python
# -*- coding: utf-8 -*-
from datagen_helper import *
from collections import OrderedDict

#==============================================================================
#========================CONFIGURATION=========================================
##=============================================================================
#Glocabl Constants for accessing data in xml
_TAG_SIGNAL      = "Signal"
_TAG_CCPEVENT      = "CCPEvent"
_TAG_BUFFERSIZE    = "BufferSize"
_TAG_OPERATIONMODE = "OperationMode"
_TAG_SHEET    = "HFL_Data"
_TAG_ITERATOR = "iterator"
#==============================================================================
#===============================UTILITIES======================================
##=============================================================================
#read data from XML
data = pandas_read_excel(__kwargs__.datasource, encoding='unicode')

def  _get_tag_data(tags,sheet):
    """Return data from xml depending on the tag (column name) and variant"""
    datadict     = {}
    counter      = 0

    #initialise data dictionary
    for tag in tags:
        datadict.update({tag:[]})
    # create a new tag for iteration
    datadict.update({_TAG_ITERATOR:[]})
    # create a new tag for variant handling
    # datadict.update({variant:[]})
    #update tags with data from excel
    for idx in range(len(data[sheet])):
        for tag in tags:            
            datadict[tag].append(data[sheet][tag][idx])

        datadict[_TAG_ITERATOR].append(counter)
        counter   = counter + 1

    return datadict

#==============================================================================
#============================CREATE DATA STORAGE===============================
##=============================================================================

_HFL_CAL      =   _get_tag_data( 
                                        [_TAG_SIGNAL,
                                         _TAG_CCPEVENT,
                                         _TAG_BUFFERSIZE,
                                         _TAG_OPERATIONMODE
                                         ],
                                        _TAG_SHEET )
print(_HFL_CAL)



