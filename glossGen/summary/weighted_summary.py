import nltk
from nltk.corpus import stopwords

DEFAULT_WEIGHTS = ['NN', 'VB']

def topN(l, n):
    s = list(reversed(sorted(l)))
    out = []
    i = 0
    while i < len(l) and i < n:
        out.append(s[i])
        i += 1
    return out


def weightedSummary(summary_text, n=3):
    ''' Save the highest weighing n sentences from the given summary'''
    sentences = nltk.sent_tokenize(summary_text)
    stops = set(stopwords.words('english'))
    # The first sentence from wikipedia is always worth keeping
    final = []
    try:
        # Weird error where tokenize is returning empty list
        final = [(1000, sentences.pop(0))]
    except:
        print("tokenize gone wrong")

    for sen in sentences:
        lsen = sen.lower()
        weight = 0
        for word in nltk.word_tokenize(lsen):
            if word not in stops:
                weight += 1
        final.append((weight, sen))


    return ' '.join(map(lambda x: x[1], topN(final, n)))
