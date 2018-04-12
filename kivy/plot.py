import matplotlib.pyplot as plt



def getnumberofOnes(cyclelength,slotlength,filename):
    f=open(filename,'r')
    y = f.read()
    counter=0
    listforplot =[]
    perslot =cyclelength*36000/slotlength
    for p in xrange(0,slotlength):
        #print(str(p*perslot)+ "to " +str((p+1)*perslot))
        counter=0
        for x in y[p*perslot:(p+1)*perslot]:
            #print(str(p*perslot)+ "to " +str((p+1)*perslot))
            if x == "1":
                counter=counter+1
        listforplot.append(counter)
        #print(listforplot)
    return(listforplot)

def plot(oneslist,numberofslots):
    slotlist=[]
    for y in xrange(1,numberofslots+1):
        slotlist.append(y)
    plt.subplot(221)
    plt.plot(slotlist, oneslist)
    plt.yscale('linear')
    plt.grid(True)
    plt.show()
a =getnumberofOnes(1,12,"1.soundclout")
b= plot(a,12)
