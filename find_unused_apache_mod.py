#!/usr/bin/python
import fileinput, re, sys
result_array = []


def array_from_string(string):
    ''' As input a string delimited by , (comma) 
    Return only not empty string and remove none value
    '''
    match = re.split(',|\n', string)
    #print type(match),match
    return [x for x in match if x and x != "none"]

def popemptyvalue(array):
    #for i in x:
    #    if i == "":
    #        x.pop()
    return [x for x in array if x]

def findconf():
    for line in fileinput.input():
        #print "%s" % (line)
        match = re.search(r'Module Name: (.*)', line)
        try:
            moduleName = match.group(1)
            print moduleName,
        except:
            pass
        match = re.search(r'Configuration Phase Participation: (.*)', line)
        try:
            confPhaseParticipation = match.group(1)
            #print confPhaseParticipation,
            print len(array_from_string(match.group(1))),
        except:
            pass
        match = re.search(r'Request Phase Participation: (.*)', line)
        try:
            reqPhaseParticipation = match.group(1)
            #print confPhaseParticipation,
            print len(array_from_string(match.group(1))),
        except:
            pass

        match = re.search(r'Current Configuration:', line)
        try:
            reqPhaseParticipation = match.group(0)
            #print confPhaseParticipation,
            print len(array_from_string(match.group(0)))
        except:
            pass

        

def findconfcomp():
    inFile = sys.stdin.read()
    regex = r"Module Name: (.*)\nContent handlers:(.*)\nConfiguration Phase Participation: (.*)\nRequest Phase Participation: (.*)\nModule Directives:[\s]+((.*?\n)+?)(Current Configuration:((.*?\n)+?\n|\n)|(\n))"
    prog = re.compile(regex , re.MULTILINE)
    i = 1
    for result in prog.finditer(inFile):
        print i
        module_name = result.group(1)
        print "Module name %s" % module_name
        conf_phase = array_from_string(result.group(3))
        print "Configuration Phase Participation: %s" % (len(conf_phase))
        req_phase = array_from_string(result.group(4))
        print "Request Phase Participation: %s" % (len(req_phase))
#        print "Module Directives: %s" % result.group(5)
        try:
            currentconf = array_from_string(result.group(8))
            print "Current Configuration: %s \n" % (len(currentconf))
        except:
            currentconf = []
            print "Current Configuration: %s \n" % (len(currentconf))
        i = i + 1
        result_array.append({ "module_name": module_name, "conf_phase": len(conf_phase), "req_phase": len(req_phase), "current_conf": len(currentconf)})
    #return result_array
#    print "Current Configuration: %s" % result.group(7)
#    print inFile

def module_to_remove(array):
    ''' If no configuration is present for the module consider it removable
    '''
    print array,len(array)
    remove_array = []
    work_array = list(array)
    i=0
    for x in work_array:
        if x["current_conf"] == 0:
            print x['module_name'],x["current_conf"]
            remove_array.append(x['module_name'])
        else:
            print "DIFF: ",x['module_name'],x["current_conf"]
        i=i+1
    print i, work_array,len(work_array)
    return remove_array

def array_subtraction(array, toremarray):
    newarray = []
    for x in toremarray:
        i = 0
        for y in array:
            #print "%s TO REMOVE - %s" % (x, y['module_name'])
            if y['module_name'] == x:
                #print "POPPED: ",array.pop(i)
                print "POPPED: ", y['module_name']
            i = i+1
    return [j['module_name'] for j in array]
                

if __name__ == "__main__":
    findconfcomp()
    print result_array
    remove_array = module_to_remove(result_array)
    print result_array
    print "To remove safely:\n",remove_array
    print "\nTo KEEP: ", array_subtraction(result_array, remove_array)


