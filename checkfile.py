#!/usr/bin/env python
# http://stackoverflow.com/questions/82831/check-if-a-file-exists-using-python
dname="/tmp/botolog"
fname="/tmp/botodebugenabled"
import os.path
if os.path.isfile(fname):
    print "File exist"
else:
    print "File not present"
# http://stackoverflow.com/questions/273192/in-python-check-if-a-directory-exists-and-create-it-if-necessary
if not os.path.exists(dname):
   print "create dir" 
   os.makedirs(dname)
