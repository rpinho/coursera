import sys, json, itertools, operator
#from pprint import pprint
from collections import Counter

verbose = False#True

## TEMPLATE
def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def getSentimentScoresDict(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited.
        scores[term] = int(score)  # Convert the score to an integer
    return scores

## BOOLS
def isWordInDictionary(word, scoresDict):
    return word.encode('utf-8') in scoresDict.keys()

def hasField(field, tweet):
    return field in tweet.keys() and tweet[field]

def hasText(tweet):
    return hasField('text', tweet)

def hasPlace(tweet):
    return hasField('place', tweet)

def hasHashtags(tweet):
    return hasField('entities', tweet) and hasField('hashtags', tweet['entities'])

def hasUserScreenName(tweet):
    return hasField('user', tweet) and hasField('screen_name', tweet['user'])

def fromUS(tweet):
    if hasPlace(tweet): return tweet['place']['country_code'] == 'US'

## PRINT

def printText(unicodeString):
    print unicodeString.encode('utf-8')

def printTweet(tweet):
    if hasText(tweet): printText(tweet['text'])

##

def getTweets(response):
    return (json.loads(line) for line in response)

def getTweetText(tweet):
    if not hasText(tweet):
        return []
    else:
        return tweet['text'].split()

def getTweetScore(tweet, scoresDict):
    if not hasText(tweet):
        return 0
    else:
        return sum([scoresDict[word] for word in getTweetText(tweet)
                    if isWordInDictionary(word, scoresDict)])

def getNewTermScore(newTerm, tweet, scoresDict):
    return getTweetScore(tweet, scoresDict)

def scoreNewTerms(tweet, scoresDict):
    if not hasText(tweet):
        return 0
    else:
        if verbose: printTweet(tweet)
        return ((word, getNewTermScore(word, tweet, scoresDict))
                for word in getTweetText(tweet)
                if not isWordInDictionary(word, scoresDict))

def scoreAllNewTerms(tweets, scoresDict):
    return (scoreNewTerms(tweet, scoresDict) for tweet in tweets)

def getAllTweetsScores(tweets, scoresDict):
    return (getTweetScore(tweet, scoresDict) for tweet in tweets)

def getTweetState(tweet):
    if fromUS(tweet): return tweet['place']['full_name'].split(', ')[-1]

def getAllStates(tweets):
    return set([getTweetState(tweet) for tweet in tweets])

def scoreStates(tweets, scoresDict):
    tweets = list(tweets)
    states = getAllStates(tweets)
    scores = dict(zip(states, [0]*len(states)))
    for tweet in tweets:
        if fromUS(tweet) and hasText(tweet):
            state = getTweetState(tweet)
            score = getTweetScore(tweet, scoresDict)
            scores[state] += score
    return scores

def getHappiestState(scores):
    scores.pop('US', None)
    return max(scores, key=scores.get)

def getHashtags(tweet):
    if hasHashtags(tweet): return tweet['entities']['hashtags']

def getHashtagsText(tweet):
    hashtags = getHashtags(tweet)
    if hashtags: return [hashtag['text'] for hashtag in hashtags]

def getAllHashtagsText(tweets):
    return [getHashtagsText(tweet) for tweet in tweets if hasHashtags(tweet)]

def main():
    #sent_file = open(sys.argv[1])
    #scoresDict = getSentimentScoresDict(sent_file)
    tweet_file = open(sys.argv[1])
    tweets = getTweets(tweet_file)

    hashtags = getAllHashtagsText(tweets)
    hashtags = itertools.chain.from_iterable(hashtags)
    counter = Counter(hashtags)
    for pair in counter.most_common(10):
        print pair[0], pair[1]

    ## happiest_state.py
    #scores = scoreStates(tweets, scoresDict)
    #print getHappiestState(scores)

    ## tweet_sentiment.py
    #scores = getAllTweetsScores(tweets, scoresDict)

    ## frequency.py
    '''
    allWords = [getTweetText(tweet) for tweet in tweets]
    allWords = itertools.chain.from_iterable(allWords)
    counter = Counter(allWords)
    n = sum(counter.values())
    for word, count in counter.iteritems():
        print word.encode('utf-8'), count
    '''

    ## term_sentiment.py
    '''
    scores = scoreAllNewTerms(tweets, scoresDict)
    for tweet in scores:
        if tweet:
            for term in tweet:
                print term[0].encode('utf-8'), term[1]
        #print '<sentiment:%d>' %score
    '''

    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
