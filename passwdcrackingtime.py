#!/usr/bin/python
'''
Analyze an passwd and tell you how long is needed to crack it with a brute force
attack.

zioalex@gmail.com
'''

import getpass
import math
import re

#passwdxsec = 2800000000 # how many passwd can I try per senconds
# From http://www.mandylionlabs.com/documents/BFTCalc.xls I interpolare the passwdxsec
passwdxsec = (2*2**33)/3600  # how many passwd can I try per senconds

passwddict = {}
passwdDict = { "upperLetter": 26, "lowerLetter": 26, "numeric": 10,
        "specialChar": 33, "randomAlphaNumeric": 62, "comboAll": 94 }
password = ""

special_chars = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ '''

def passwdinput():
    ''' Get the password from the user '''
    #password = raw_input("Please enter your password: ") # clear password
    password = getpass.getpass("Please enter your password: ")
    return password

def countLowerLetter(passwd):
    return (len(re.findall(r'[a-z]',passwd)),passwdDict['lowerLetter']) or 1

def countUpperLetter(passwd):
    return (len(re.findall(r'[A-Z]',passwd)),passwdDict['upperLetter']) or 1

def countNumeric(passwd):
    return (len(re.findall(r'\d',passwd)),passwdDict['numeric']) or 1

def countAlphaNumeric(passwd):
    return (len(re.findall(r'\w',passwd)),passwdDict['randomAlphaNumeric']) or 1

def countSpecial(passwd):
    specialcount = 0
    for special in special_chars:
        lenght = 0
        #print special
        lenght = len(re.findall(r'(\%s)' %special , passwd))
        if lenght > 0:
            #print lenght,special
            specialcount = lenght + specialcount
    return (specialcount,passwdDict['specialChar']) or 1

def countComboAll(passwd):
    return len(re.findall(r'.*',text))

def passwdAnalyzer(passwd):
    ''' Analyze the password to find how long is it and which kind of
    dictionaries were used
    '''
    passwdCombination = 1
    #passwdLenght = len(passwd)
    special = countSpecial(passwd)
    print "SPECIAL CHAR", special
    upper = countUpperLetter(passwd)
    print "UPPER CHAR", upper
    lower =countLowerLetter(passwd)
    print "LOWER CHAR", lower
    numeric=countNumeric(passwd)
    print "NUMERIC", numeric
    for count in special, upper, lower, numeric:
        if count[0] >= 1:
            passwdCombination = math.pow(count[1],count[0]) * passwdCombination
        print count

    return passwdCombination
    

def timetoresolve(passwd):
    ''' Find the time needed to crack the passwd '''
    passwdCombination = passwdAnalyzer(password)
    sectoresolve = passwdCombination / passwdxsec 
    print "%s combination will be solved in\n" % passwdCombination
    print "%.4f sec to resolve or just\n%.4f minutes or\n%.4f hour or\n%.4f days\nor just %.8f years" % ( sectoresolve, sectoresolve/60, sectoresolve/3600, sectoresolve/(3600*24), sectoresolve/(3600*24*365))

if __name__ == '__main__':
    #print passwdDict["letter"]
    print "Starting from the hypothesis to try %s password x second" % passwdxsec
    password = passwdinput()
    #print password
    timetoresolve(password)
            
