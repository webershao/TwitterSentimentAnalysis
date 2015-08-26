import sys, json
import operator

def hw():
    
    tsFileName = sys.argv[1]
    tsFile = open(tsFileName, 'r')

    tagCountDict = {}
    totalTagCount = 0

    lines = tsFile.readlines()
    for line in lines:
        dline = json.loads(line)
        if dline.has_key('entities'):
            ent = dline['entities']
            if ent.has_key('hashtags'):
                ht = ent['hashtags']
                if len(ht) > 0:
                    for eht in ht:
                        text = eht['text']
                        # If word in dictionary, increment, otherwise
                        # initialize it at count = 1.
                        if text in tagCountDict:
                            tagCountDict[text] += 1
                        else:
                            tagCountDict[text] = 1
                        totalTagCount += 1

    tsFile.close()

    sortedTagCountDict = sorted(tagCountDict.iteritems(), key=operator.itemgetter(1), reverse=True)
    
    for i in range(0, 10):
        pair = sortedTagCountDict[i]
        print pair[0], pair[1]
    

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
