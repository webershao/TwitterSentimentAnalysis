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

    lines = tsFile.readlines()
    for line in lines:
        tally = 0
        dline = json.loads(line)
        if dline.has_key('text'):
            dlt = dline['text']
            words = dlt.split(' ')
            for word in words:
                if scores.has_key(word):
                    tally = tally + scores[word]
        print tally
    
    tsFile.close()

    #print scores.items() # Print every (term, score) pair in the dictionary
    #print 'Hello, world!'

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
