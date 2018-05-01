#ToDo: take in list from timeline
#if loop finds a 1 then devices randomly goes off in that time. need to translate
import io
from random import randint
from reroll import reroll
from bitarray import bitarray
import sys
class TLR:
    def __init__(self,slotList, timelineLength):
            self.slotList = slotList[:]
            #self.timelineLength = timelineLength #in hours
            if len(self.slotList) != 0:
                #print("Slot has at least 1 element")
                self.periodLength = int((timelineLength*36000)/len(self.slotList))
                self.instructionStringLength = int(self.periodLength*len(slotList))
                self.instructions = []
                for i in xrange(len(self.slotList[0].groupList)):
                    tmpinstructions = bitarray(self.instructionStringLength)
                    tmpinstructions.setall(False)
                    self.instructions.append(tmpinstructions)
            else:
                self.periodLength = 0







    def makeTimeline(self):

        print("Period Length" + str(self.periodLength))
        for i in xrange(len(self.slotList)):
            print(self.slotList[i].name)
            for j in xrange(len(self.slotList[i].groupList)):
                b = binarySequence(self.periodLength,self.slotList[i].groupList[j].eventLength, self.slotList[i].groupList[j].eventAmount)
                print("# of events" + str(self.slotList[i].groupList[j].eventAmount))
                index = 0
                start = self.periodLength*i
                self.instructions[j][start:start+self.periodLength] = bitarray(b.makeBinString())
                print(self.instructions[j])
        self.apply_triggers()
        self.writeToFile()
        #print(self.instructions[0])

    def apply_triggers(self):
        print("Test1")
        print(self.instructions[0])

        for i in xrange(len(self.slotList)):
            for j in xrange(len(self.slotList[i].groupList)):
                start=self.periodLength*i



                L = self.slotList[i].groupList[j].triggerList
                for k in xrange(len(L)):
                    index2 = self.matchGroupIndex(L[k][1])

                    print(self.instructions[j])

                    print(self.instructions[0])
                    print(" Before trigger function")

                    print(self.instructions[j][start:start+self.periodLength])
                    self.instructions[index2][start:start+self.periodLength] = self.trigger(L[k][0], self.instructions[j][start:start+self.periodLength], self.instructions[index2][start:start+self.periodLength])



    def matchGroupIndex(self, aName):

		for i in xrange(0, len(self.slotList[0].groupList)):
			if aName == self.slotList[0].groupList[i].name:
				return i


    def trigger(self, chance, bArr1, bArr2):
        print (chance)
        print (bArr1)
        print (bArr2)

        for i in xrange(len(bArr1)):
            if bArr1[i] == 1:
                bArr2[i] = reroll(int(chance*100))

                print(bArr2)
        return(bArr2)

    def writeToFile(self):
        file = open("save1.txt", "w+")
        file.truncate()
        print(len(self.instructions))
        for i in xrange(len(self.instructions)):
            file.write(self.instructions[i].to01() + '\n')
        file.close()





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
        return ''.join(randString)




#TODO create reroll function. Have it be choice 0 or 1 but weighted
