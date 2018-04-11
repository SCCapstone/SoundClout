from reroll import reroll
from timelinereader import *
class Trigger:
    def __init__(self,name,percentage,binarysequenceOne,binarysequenceTwo):
           self.name = name
           self.percentage = percentage
           self.binarysequenceOne = binarysequenceOne
           self.binarysequenceTwo = binarysequenceTwo


    def Trigger(self):
        #print("before: " +self.binarysequenceTwo)
        tmp =self.binarysequenceTwo
        listtmp = list(tmp)
        tmp2 = self.binarysequenceOne
        a = len(self.binarysequenceOne)
        b = len(self.binarysequenceTwo)
        replacestring  = ""
        for x in xrange(0,a):
            if tmp2[x] == "1":
                listtmp[x]  = str(reroll(self.percentage))
        return(''.join(listtmp))
#testing
#newList=[0,1,1,38]
#newList2=[0,1,1,24]
#j = timelineReader(newList,24,5,"group1",20)
#k = timelineReader(newList2,24,5,"group2",20)
#tmp1=j.MonthGroupBehavior()

#tmp2=k.MonthGroupBehavior()

#a = Trigger("woodfalling",10,tmp1,tmp2)
#file = open( "output.soundclout", "w")
#x=a.Trigger()
#file.write(str(x))
#file.close
