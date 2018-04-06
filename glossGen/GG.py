from __future__ import absolute_import
from __future__ import print_function
from .keywordExtraction import rake
import operator
import io
import os
import sys
import wikipedia
from .summary import weightedSummary
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer


dirname = os.path.dirname(os.path.abspath(__file__))
stoppath = dirname + "/keywordExtraction/data/stoplists/SmartStoplist.txt"

def getInput(filename="/../target.txt"):
    targetPath = dirname + filename

    sample_file = io.open(targetPath, 'r')
    text = sample_file.read()
    return text

def getKeywords(text):

    rake_object = rake.Rake(stoppath, 5, 2, 2)
    keywords = rake_object.run(text)

    result = []
    for wtuple in keywords:
        result.append(wtuple[0])
    #print(result)
    return result

def curateKeywords(initialList):
    # TODO: put any curation of keywords here and call it from getKeywords
    pass

def extractiveSummarization(keywords, text):
    # Base code from: https://dev.to/davidisrawi/build-a-quick-summarizer-with-python-and-nltk
    # stopWords = set(stopwords.words("english"))
    result = []
    ps = PorterStemmer()
    textWords = word_tokenize(text)
    splitKeys = list(map(ps.stem, sum([kw.lower().split(" ") for kw in keywords], [])))
    print(splitKeys)

    # Fill freq table with words we are looking for
    freqTable = {}
    for key in splitKeys:
        freqTable[key] = 0

    for word in textWords:
        stem = ps.stem(word.lower())
        if stem in freqTable:
            freqTable[stem] += 1
        elif stem in splitKeys:
            freqTable[stem] = 1
        else:
            continue

    orgSentences = sent_tokenize(text)
    stemSent = []
    sentences = []
    for sentence in orgSentences:
        if (len(sentence.split(" ")) > 20):
            continue
        else:
            sentences.append(sentence)
            stemSent.append(" ".join([ps.stem(word.lower()) for word in word_tokenize(sentence)]))

    for keyphrase in keywords:
        splitKeys = list(map(ps.stem, keyphrase.lower().split(" ")))
        print(splitKeys)
        sentenceValue = {}
        sumValues = 0
        for i in range(0, len(stemSent)):
            for key in splitKeys:
                # print(keyphrase + " | " + key + " | " + stemSent[i])
                if key in stemSent[i]:
                    # print(key + " | " + stemSent[i]) 
                    if i in sentenceValue:
                        sentenceValue[i] += freqTable[key]
                        sumValues += freqTable[key]
                    else:
                        sentenceValue[i] = freqTable[key]
                        sumValues += freqTable[key]

        # Average value of a sentence from original text
        if (len(sentenceValue) <= 0):
            average = 0
        else:
            average = int(sumValues/ len(sentenceValue))
        print(sentenceValue)

        summary = ''
        for index, value in sentenceValue.items():
            if value > (1.5 * average):
                summary +=  " " + sentences[index]
        print(keyphrase + " | " + summary)
        if summary.strip() != '':
            result.append((keyphrase, summary))

    return result

def summarize(keywords, text):
    wiki = []
    extractive = []
    for keyphrase in keywords:
        search = []
        wkey = None
        try:
            search = wikipedia.search(keyphrase)
        except:
            print (keyphrase + " | Couldn't search for " + keyphrase)
        for suggestion in search:
            #print(keyphrase.lower() + " " + suggestion.lower())
            if keyphrase.lower() in suggestion.lower():
                wkey = suggestion
                print(keyphrase + " | Found a suggestion: " + wkey)
                break

        if wkey is None:
            # extractive summarization
            print(keyphrase + " | extractive!!!")
            # extractive.append((keyphrase, "extractive!!!!"))
            extractive.append(keyphrase)
        else:
            ws = ""
            try:
                #print("hihi")
                #print(wkey)
                #print(wikipedia.summary(wkey))
                ws = wikipedia.summary(wkey)
            except:
                print(keyphrase + " | Couldn't get summary for " + keyphrase)
            if (ws.strip() != ""):
                wiki.append((keyphrase, weightedSummary(ws)))
            else:
                print (keyphrase)
            #print(weightedSummary(ws))
    
    extractive = extractiveSummarization(extractive, text)
    result = [wiki, extractive]
    return result

def curateSummaries(initialSummaries):
    return map(weightedSummary, initialSummaries)

def formatOutput(summaries):
    mdOut = []
    for key, summary in summaries:
        mdOut.append(u'##{}:\n{}\n'.format(key, summary))
    return '\n'.join(mdOut).encode('utf-8')

def GGmain():
    text = getInput()
    keywords = getKeywords(text)
    if len(keywords) > 100:
        keywords = keywords[:50]
    summaries = summarize(keywords, text)
    return summaries

def main():
    pass

if __name__ == '__main__':
    main()
