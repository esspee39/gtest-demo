import glob
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from collections import defaultdict

def nestedDict():
    return defaultdict(nestedDict)

class Test:
    mutant = ""
    test = ""
    status = ""

def getMutantKilledInfo(mutant):
    #get current year
    now = datetime.now()
    year = now.strftime("%Y")

    #tree = ET.parse('Test.xml')

    for name in glob.glob('../build/Testing/'+ year +'*'):
        path = name
        if os.path.exists(path + "/Test.xml"):
            with open(path + "/Test.xml") as f:
                tree = ET.parse(f)
                 
    root = tree.getroot()
    tests = []

    for element in root[0]:
        if(element.tag == "Test"):
            if mutant in element[0].text:
                #print("MUTANT NAME: " + mutant)
                testname = element[0].text.split(".")[1]
                mutantname = mutant
                #print("TEST NAME: " + testname)
                #print("INSERTED " + mutantname + ": " + testname + ": " + element.attrib.get("Status"))
                newtest = Test()
                newtest.mutant = mutant
                newtest.test = testname
                newtest.status = element.attrib.get("Status")
                tests.append(newtest)

    killed_by = []
    #mutant_status = {}
    #mutant_status[mutant] = "survived"
    for test in tests: 
        if(mutant == test.mutant and test.status == "failed"):
    #       mutant_status[mutant] = "killed"
            killed_by.append(test.test)
    #    print("Mutant: " + test.mutant + " Test: " + test.test + " Status: " + test.status)

    #for key in mutant_status:
    #    print("DICT")
    #    print(key + ": " + mutant_status[key])
 
    #killed = 0
    #survived = 0
    #print ("\n")
    #print ("Killed")
    #for key in mutant_status:
    #    if(mutant_status[key] == "killed"):
    #       print(key)
    #       killed += 1

    #print ("\n")
    #print ("Survived")
    #for key in mutant_status:
    #    if(mutant_status[key] == "survived"):
    #        print(key)
    #        survived += 1
    
    #total = len(mutant_names)
    #survivedscore = survived / total * 100
    #killedscore = killed / total * 100

    #print ("Survived Score: " + str(survivedscore) + "%")
    #print ("Killed Score: " + str(killedscore) + "%")
    #print(killed_by)
    
    return killed_by

#blah = "ArithmeticPlusToMinus"
#getMutantKilledInfo(blah)
