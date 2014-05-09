from sys import stdin

#Ignore the first line
stdin.readline()

def count_text(line, text):
    return sum(count_text(line[i + 1:], text[1:])
               for i, c in enumerate(line) if c == text[0])

for l in stdin.readlines():
    print l.split()
    for k,line in enumerate(l.strip()):
        print k,line
    
input()
for i, line in enumerate(l.strip() for l in stdin.readlines()):
    print "Case #%d %04d"%(i + 1, count_text(line, "welcome to code jam"))
    
#second solution#
#second solution#
#second solution#
#second solution#

from sys import stdin

#Ignore the first line
stdin.readline()

def count_text(line, text):
    if text == "":
        return 1
    return sum(count_text(line[i + 1:], text[1:])
               for i, c in enumerate(line) if c == text[0])

for i, line in enumerate(l.strip() for l in stdin.readlines()):
    print "Case #%d %04d"%(i + 1, count_text(line, "welcome to code jam"))