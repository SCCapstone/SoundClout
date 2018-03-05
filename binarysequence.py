import io
from random import randint
import sys

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
            for y in xrange(1,self.eventLength,1):
                if(eventPosition+y < self.timeLength):
                    randString[eventPosition+y] = '1'
                else:
                    break
        return randString


    """    randString = ""
        for x in range(10):
            randInt = randint(0, 1)
            randString = randString + str(randInt)
        return randString
    """

file = open("binarysequence.txt","r+")

bins = binarySequence(20,10,1)

file.write(''.join(bins.makeBinString()))

file.close
