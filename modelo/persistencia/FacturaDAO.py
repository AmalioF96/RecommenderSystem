'''
Created on 16 oct. 2020

@author: Amalio
'''

from modelo.persistencia.bbdd.Connection import Connection as myConect

import pandas as pd
import numpy as np
import datetime


class FacturaDAO(object):
    '''
    classdocs
    '''

    myConect=None;
    def __init__(self, conect):
        '''
        Constructor
        '''
        myConect=conect