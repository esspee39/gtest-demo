import glob
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime

def getMutantKillInfo():
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
                 survived = []
                 killed = []
                 for element in root[0]:
                     if(element.tag == "Test"):
                         print (element[0].text)
                         print (element.attrib.get("Status"))
                     if(element.attrib.get("Status") == "passed"):
                         survived.append(element[0].text)
                     elif(element.attrib.get("Status") == "failed"):
                         killed.append(element[0].text)
                 print ("\n")
                 print ("Killed")
                 total = (len(survived) + len(killed))
                 survivedscore = int((len(survived) / total * 100))
                 killedscore = int((len(killed) / total * 100))
                 for x in killed:
                     print(x)
                 print ("\n")
                 print ("Survived")
                 for y in survived:
                     print(y)
                 print ("\n")
                 print ("Survived Score: " + str(survivedscore) + "%")
                 print ("Killed Score: " + str(killedscore) + "%")


getMutantKillInfo()
