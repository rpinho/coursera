import sys, json

def getSentimentScoresDict(afinnfile):
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited.
        scores[term] = int(score)  # Convert the score to an integer
    return scores

def getTweets(response):
    return (json.loads(line) for line in response)

def getTweetScore(tweet, scoresDict):
    if 'text' not in tweet.keys():
        return 0
    else:
        return sum([scoresDict[word] for word in tweet['text'].split()
                    if word.encode('utf-8') in scoresDict.keys()])

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
    scores = getAllTweetsScores(tweets, scoresDict)
    for score in scores:
        print score
        #print '<sentiment:%d>' %score
    #hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
