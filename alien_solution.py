import sys, re
fp = file(sys.argv[1])

#read params
(l, d, n) = [int(x) for x in fp.next().split()]
#read words
words = [fp.next() for x in range(d)]

#read pattern
for i in range(1, n+1):
    searchStr = fp.next().replace("(","[").replace(")","]")
    print searchStr
    
    
    searchIt = re.compile(searchStr).search
    print str(searchIt)
    print re.match(re.compile(searchStr),words)
    input()
    print "Case #%d: %d" % (i, len(filter(searchIt, words)))
fp.close()

