import sys, json

def hw():
    afinnfile = open(sys.argv[1])
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.

    afinnfile.close()

    tsFileName = sys.argv[2]
    tsFile = open(tsFileName, 'r')

    otherWordScoreDict = {}
    otherWordCountDict = {}

    lines = tsFile.readlines()
    for line in lines:
        tally = 0
        dline = json.loads(line)
        if dline.has_key('text'):
            dlt = dline['text']
            if ' ' not in dlt:
                continue
            words = dlt.split(' ')
            if len(words) < 2:
                continue
            otherWordList = []
            for word in words:
                if scores.has_key(word):
                    tally = tally + scores[word]
                else:
                    #if not '\u' in word and not '@' in word:
                    #if re.match('[a-zA-Z]+', word) is not None:
                    otherWordList.append(word)
            for otherWord in otherWordList:
                if otherWordCountDict.has_key(otherWord):
                    otherWordScoreDict[otherWord] += tally
                    otherWordCountDict[otherWord] += 1
                else:
                    otherWordScoreDict[otherWord] = tally
                    otherWordCountDict[otherWord] = 1                    
    
    tsFile.close()
    
    for otherWord in otherWordCountDict.keys():
        myScore = 1.0 * otherWordScoreDict[otherWord] / otherWordCountDict[otherWord]
        print otherWord, myScore
    

def lines(fp):
    print str(len(fp.readlines()))

def main():
    #sent_file = open(sys.argv[1])
    #tweet_file = open(sys.argv[2])
    hw()
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
