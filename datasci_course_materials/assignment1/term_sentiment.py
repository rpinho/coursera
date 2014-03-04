import sys, json
#from pprint import pprint

verbose = False#True

def getSentimentScoresDict(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited.
        scores[term] = int(score)  # Convert the score to an integer
    return scores

def getTweets(response):
    return (json.loads(line) for line in response)

def getTweetText(tweet):
    return tweet['text'].split()

def isWordInDictionary(word, scoresDict):
    return word.encode('utf-8') in scoresDict.keys()

def isTextInTweet(tweet):
    return 'text' in tweet.keys()

def printTweet(tweet):
    if isTextInTweet(tweet): print tweet['text'].encode('utf-8')

def getTweetScore(tweet, scoresDict):
    if not isTextInTweet(tweet):
        return 0
    else:
        return sum([scoresDict[word] for word in getTweetText(tweet)
                    if isWordInDictionary(word, scoresDict)])

def getNewTermScore(newTerm, tweet, scoresDict):
    return getTweetScore(tweet, scoresDict)

def scoreNewTerms(tweet, scoresDict):
    if not isTextInTweet(tweet):
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

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    scoresDict = getSentimentScoresDict(sent_file)
    tweet_file = open(sys.argv[2])
    tweets = getTweets(tweet_file)
    scores = scoreAllNewTerms(tweets, scoresDict)
    for tweet in scores:
        if tweet:
            for term in tweet:
                print term[0].encode('utf-8'), term[1]
        #print '<sentiment:%d>' %score
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
