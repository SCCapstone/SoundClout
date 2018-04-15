import matplotlib.pyplot as plt


#runs through file and returns list of ones in each slot
def getnumberofOnes(cyclelength,numberofslots,filename):
    f=open(filename,'r')
    y = f.read()
    counter=0
    listforplot =[]
    perslot =cyclelength*36000/numberofslots
    for p in xrange(0,numberofslots):
        counter=0
        for x in y[p*perslot:(p+1)*perslot]:
            if x == "1":
                counter=counter+1
        listforplot.append(counter)
    return(listforplot)
#plots timeline based on iputs
def plot(numberofslots,listofgroup):
    slotlist=[]
    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=.73, left=.08, right=.95, top=.99, hspace=.35,wspace=0)
    z=len(listofgroup)
    colorlist = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    listofgroup.reverse()
    newlist =[]
    for x in xrange(0,z):
        newlist.append(x*2.5)
        a =getnumberofOnes(1,numberofslots,str(x+1)+".soundclout")
        for y in xrange(0,numberofslots):
            slotlist.append(y)
            if a[y]!=0:
                ax.broken_barh([(slotlist[y], 1)],(2.5*x,2.5), facecolors='blue')
        ax.set_ylim(0 ,2.5*len(newlist))
        ax.set_xlim(0, numberofslots)
        ax.set_xlabel('slots')
        ax.set_ylabel('Groups')
        ax.set_yticks(newlist)
        ax.set_yticklabels(listofgroup)
    plt.savefig('timeline.png',bbox_inches='tight',frameon=False)
    #plt.show()
#z= ['group1','group2','group3']
#plot(10,z)
