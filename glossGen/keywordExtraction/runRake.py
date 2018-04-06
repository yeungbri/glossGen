from __future__ import absolute_import
from __future__ import print_function
import six
import rake
import operator
import io
import os
import sys

stoppath = "data/stoplists/SmartStoplist.txt"

# 1. initialize RAKE by providing a path to a stopwords file
#rake_object = rake.Rake(stoppath, 4, 2, 1)

# 2. run on RAKE on all training data
dirname = os.path.dirname(os.path.abspath(__file__))
trainDir = dirname + "/data/500N-KPCrowd-v1.1/CorpusAndCrowdsourcingAnnotations/train"
resultsDir = dirname + "/results/"
dataDir = dirname + "/data/"

def runRake(rake_object):
    for filename in os.listdir(trainDir):
        if filename.endswith(".txt") and not "justTitle" in filename:
            filepath = os.path.join(trainDir, filename)
            
            sample_file = io.open(filepath, 'r')

            text = sample_file.read()

            keywords = rake_object.run(text)

            # 3. print results
            name = filename.split(".txt")[0]
            resultsFile = resultsDir + "rake_" + name + ".key"
            # Only top values
            with open(resultsFile, 'w+') as fp:
                #print (name + str(len(keywords)))
                if len(keywords) > 0:
                    maxVal = keywords[0][1]
                else:
                    maxVal = 0
                for kv in keywords:
                    #print (kv[0] + " " + str(kv[1]))
                    if kv[1] >= maxVal:
                        fp.write(kv[0].encode('utf-8') + "\n")
            # All values
            resultsFile = resultsDir + "rakeall_" + name + ".key"
            with open(resultsFile, 'w+') as fp:
                for kv in keywords:
                    fp.write(kv[0].encode('utf-8') + "\n")


                #print (">>> top precision: " + str(topPrec))
          
def main():
    #runRake()
    #compare()
    fn = sys.argv[1]
    for filename in os.listdir(dataDir):
        if fn in filename:
            filepath = os.path.join(dataDir, filename)
            rake_object = rake.Rake(stoppath, 5, 2, 2)
            sample_file = io.open(filepath, 'r')
            text = sample_file.read()
            keywords = rake_object.run(text)
            print(keywords)
            break

if __name__ == "__main__":
    main()
    
        
