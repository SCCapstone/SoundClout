from reroll import reroll
from timelinereader import *
class Trigger:
    def __init__(self,percentage,binarysequenceOne,timelength,effectedgroup,effectedslot,numberofslots):
           self.percentage = percentage
           self.binarysequenceOne = binarysequenceOne
           self.timelength =timelength
           self.effectedgroup =effectedgroup
           self.numberofslots =numberofslots
           self.effectedslot =effectedslot


    def Trigger(self): #creates an empty binary sequence. then for evey 1 in input sequence apply percent and update the binary sequence
        cycleLengthBits = self.timelength*36000 #converts cyclelength to bits and is calculated if cyclelength is given in hours
        monthLength = int(cycleLengthBits/self.numberofslots)
        tmp =binarySequence(monthLength,0,0)
        newtemp =(tmp.makeBinString())
        tmp2 = self.binarysequenceOne
        a = len(self.binarysequenceOne)
        replacestring  = ""
        for x in xrange(0,a):
            if tmp2[x] == "1":
                newtemp[x]=str(reroll(self.percentage))
        open(self.effectedgroup+"stuff.txt",'a').close()
        file = open(+"stuff.txt", "r+b")
        file.seek((self.effectedslot-1)*monthLength)
        b=''.join(newtemp)
        file.write(''.join(b))
        return(newtemp)
#testing
#newList=[1,3,1,12]
#j = timelineReader(newList,1,1,"group1",3)
#tmp1=j.MonthGroupBehavior()
#a = Trigger(50,tmp1,1,'3',3,3)
#a.Trigger()
