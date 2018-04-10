#ToDo: take in list from timeline
#if loop finds a 1 then devices randomly goes off in that time. need to translate
import io
from random import randint
import sys
class timelineReader:
    def __init__(self,settingsList, cyclelength, eventLength,groupname):
            self.settingsList = settingsList
            self.cyclelength = cyclelength
            self.eventLength = eventLength
            self.groupname = groupname

    def MonthGroupBehavior(self):
        #1 bit is 1/10th of a second
        cycleLengthBits = self.cyclelength*36000 #converts cyclelength to bits and is calculated if cyclelength is given in hours
        monthLength = int(cycleLengthBits/12)
        eventLengthBits = self.eventLength*600 #converts event length to bits and is calculated if eventlength is given in minutes
        marker = self.settingsList[2]
        numEvents = self.settingsList[3]
        binaryString = '';
        if marker==True:
            p=binarySequence(monthLength,eventLengthBits,numEvents)
            a = p.makeBinString()
            file = open(self.groupname +".soundclout", "w+")
            print(self.settingsList[1]*monthLength)
            file.seek(self.settingsList[1]*monthLength)
            file.write(''.join(a))
            binaryString = ''.join(a)
            #print("addding : " + binaryString)

            file.close
        if marker==False:
            p=binarySequence(monthLength,0,0)
            b = p.makeBinString()

            file = open(self.groupname +".soundclout", "w+")
            print(self.settingsList[1*monthLength])
            file.seek(self.settingsList[1]*monthLength)
            file.write(''.join(b))
            binaryString = ''.join(b)
            #print("addding : " + binaryString)

            file.close
        return binaryString

class binarySequence:
    def __init__(self, timeLength, eventLength, eventAmount):
        self.timeLength = timeLength
        self.eventLength = eventLength
        self.eventAmount = eventAmount

    def makeBinString(self):
        randString = list("")
        #makes string length of timeLength
        for x in range(self.timeLength):
            randString = randString + list("0")
        #takes random position and turn it and the following eventLength-1 spots into 1s
        for x in range(self.eventAmount):
            eventPosition = randint(0, self.timeLength-1)
            randString[eventPosition] = '1'
            for y in range(1,self.eventLength,1):
                if(eventPosition+y < self.timeLength):
                    randString[eventPosition+y] = '1'
                else:
                    break
        return randString




#TODO create reroll function. Have it be choice 0 or 1 but weighted


#testing
newList=[0,2,1,2]
j = timelineReader(newList,1,5,"group1")
j.MonthGroupBehavior()
