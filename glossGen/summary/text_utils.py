from utils import DefaultDict

import re

def getSentences(rawText):
    sentences = []
    sentence = []
    rawText = rawText.replace('\n', ' ').replace('\r', '')
    for word in rawText.split():
        sentence.append(word)
        if word[-1] == '.' or word[-1] == '?' or word[-1] == '!':
            sentences.append(' '.join(sentence))
            sentence = []
    return sentences

def loadKeywords(filename):
    with open(filename, 'r') as infile:
        return infile.read().split('\n')[:-1]

def readFile(filename):
    with open(filename, 'r') as infile:
        return getSentences(infile.read())

def getKeywordSentences(keywords, sentences):

    # Get a dictionary of words to indices of sentences containing the words
    wordToSen = DefaultDict(initialize=lambda: list())

    for i, sen in enumerate(sentences):
        for word in keywords:
            if word in sen:
                wordToSen[word].append(i)
    return wordToSen

def stupidSummary(keywords, sentences, wordToSen, n):
    ''' A dumb summary techinque -- Return first up to n sentences with the keyword'''
    summaries = []
    for word in keywords:
        i = 0
        summary = ['*' + word + '* :']
        while i < n and i < len(wordToSen[word]):
            summary.append(sentences[wordToSen[word][i]])
            i += 1
        summaries.append(' '.join(summary))
    return summaries

def regexDefine(keyword, text, regexs):
    matches = []
    for regex in regexs:
        match = re.search(regex.format(name=keyword), text)
        if match is not None:
            matches.append(match.group(0))
    return '\n'.join(matches)


FILENAME = 'test.txt'
KEYWORD_FILE = 'keys.txt'

REGEX = ['{name} and related .*s\.',
         '.* \(\s*{name},.*\.',
         '.*, {name}\.',
         ', a {name} .*',
         '\(\s*{name}\s*.*\),',
         'form of .*, {name}.*\.',
         'for .*, {name} and',
         'cell .*, {name}',
         'as {name}, .* and']

def main():
    sens = readFile(FILENAME)
    keywords = loadKeywords(KEYWORD_FILE)
    kwrds2Sen = getKeywordSentences(keywords, sens)
    #for summary in stupidSummary(keywords, sens, kwrds2Sen, 3):
    #    print(summary)

    for keyword in keywords:
        print("{}: {}".format(keyword, regexDefine(keyword, ' '.join(sens), REGEX)))

if __name__ == '__main__':
    main()
