import sys, json

def hw():
    
    tsFileName = sys.argv[1]
    tsFile = open(tsFileName, 'r')

    wordCountDict = {}
    totalWordCount = 0

    lines = tsFile.readlines()
    for line in lines:
        dline = json.loads(line)
        if dline.has_key('text'):
            dlt = dline['text']
            words = dlt.split()
            for word in words:
                if wordCountDict.has_key(word):
                    wordCountDict[word] += 1
                else:
                    wordCountDict[word] = 1
                totalWordCount += 1

    tsFile.close()
    
    for word in wordCountDict.keys():
        freq = 1.0 * wordCountDict[word] / totalWordCount
        print word, freq
    

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
