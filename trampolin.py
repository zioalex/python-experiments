#!/usr/bin/env python
import time
import threading

# see https://pypi.python.org/pypi/greenlet as a thread alternative.

TIMEOUT = 1    # in minutes
sec = TIMEOUT * 60
input = ""
inputarray = []


def trampotimer(fieldnum, timeout):
    sec = timeout
    print "Field %r started" % (fieldnum)
    while (sec > 0):
        sec -= 1
        time.sleep(1)
    print "The %r field time is over" % (fieldnum)

def checkfield(fieldnum):
    pass

def stop_timer(fieldnum):
    pass

def bg_trampotimer(fieldnum, timeout):
    trampo_thread = threading.Thread(target=trampotimer, args=(fieldnum, timeout))
    trampo_thread.start()

if __name__ == "__main__":
    print "Please enter the field to start with the format 'start 1'\nor 'exit' to quit"
    while (input != "exit"):
        input = raw_input("> ")
        inputarray = input.split()
        try:
            if inputarray[0] == "start":
                field = inputarray[1]
                #trampotimer(field, sec)
                bg_trampotimer(field, sec)
            elif inputarray[0] == "status":
                print "Status"
        except:
            continue
    print "ByeBye Baby"
