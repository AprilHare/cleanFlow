#imports flow data from a directory
import FlowCytometryTools
import os
import numpy as np

from FlowCytometryTools import FCMeasurement, FCPlate
from pylab import *


def importFlow(directory):
    toImport = os.listdir(directory)
    toImport = [entry for entry in toImport if entry[-4:] == '.fcs']

    samples = [FCMeasurement(ID=entry, datafile=directory+'/'+entry) for entry in toImport]
    return samples


