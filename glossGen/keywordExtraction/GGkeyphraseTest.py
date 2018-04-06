from __future__ import absolute_import
from __future__ import print_function
import rake
import operator
import io
import os
import sys


dirname = os.path.dirname(os.path.abspath(__file__))
stoppath = dirname + "/data/stoplists/SmartStoplist.txt"
targetPath = dirname + "/../../target.txt"

def runRAKE():
    rake_object = rake.Rake(stoppath, 5, 2, 2)
    sample_file = io.open(targetPath, 'r')
    text = sample_file.read()
    keywords = rake_object.run(text)
    return keywords

def GGkeyphrase():
    rakeresult = runRAKE()
    result = []
    for wtuple in rakeresult:
    	result.append(wtuple[0])
    print(result)
    return result

def main():
	GGkeyphrase()

if __name__ == "__main__":
	main()