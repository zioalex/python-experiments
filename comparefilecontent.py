#!/usr/bin/env python
from memory_profiler import profile
# Memory profiling experiment
#from guppy import hpy
#h = hpy()
#print h.heap()
# Not work


#print matchfile
#print matchfile.readline()
#print matchfile.read()

#matchfile.seek(0)
count=0
minimummatch=2
class color(object):
# Better to inherit the object class.
# http://stackoverflow.com/questions/8924173/how-do-i-print-bold-text-in-python
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

@profile
def rmnewline(string):
    string = string.replace('\n',"")
    return string

#@profile
def match():
    count = 0
    minimummatch = 3
    with open('eachzone.txt','r') as matchfile:
        # while True:
	for line in matchfile:
            line = matchfile.readline()
            # if not line: break
            line=rmnewline(line)
            with open('allzone.txt','r') as allzone:
                if line in allzone.read(): 
                    count=count + 1
                    #print "line %s matched" % line

#matchfile = open('allzone.txt','r')
#print matchfile.read()
#print count
    if  count >= minimummatch: 
        print color.GREEN + color.BOLD + "Minimum match %i reached with a total of %i" % (minimummatch,count) + color.END
    else: 
        print color.RED + color.BOLD + "Minimum match %i not reached with a total of %i" % (minimummatch,count) + color.END

if __name__ == '__main__':
        match()
