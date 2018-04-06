from __future__ import absolute_import
from __future__ import print_function
import six
import rake
import operator
import io
import os


dirname = os.path.dirname(os.path.abspath(__file__))
trainDir = dirname + "/data/500N-KPCrowd-v1.1/CorpusAndCrowdsourcingAnnotations/train"

for filename in os.listdir(trainDir):
    if filename.endswith(".key"):
        name = filename.split(".key")[0]
        print (filename)
        
        marujoVals = []
        with open(trainDir + "/" + filename, 'r') as mf:
            for line in mf:
                marujoVals.append(line)
