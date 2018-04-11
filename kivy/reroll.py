import random
def reroll(percentOne):
        percentTwo = 100-percentOne
        if ((isinstance(percentOne, int)==True)):
                my_list = [0]*percentTwo+[1]*percentOne

                choose = random.choice(my_list)
                #print(choose)
                x=(choose)
                return(x)
        else:
            print("error please only use integers")

#testing
#reroll(100)
