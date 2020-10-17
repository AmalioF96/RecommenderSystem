'''
Created on 16 oct. 2020

@author: Amalio
'''
import pandas as pd
import numpy as np
from modelo.persistencia.Connection import Connection

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
        self.myConect=conect