"""
@author psj
@since 160411
"""


def sumList(aList):
    
    for i in range(1,1001):
        if(i%4==0 and i%5!=0):
            print i
            aList.append(i)

    print len(aList)
    sum=0

    for i in range(0,len(aList)):
        sum=sum+aList[i]

    print sum



def lab6():
	aList=list()
	sumList(aList)


def main():
	lab6()


if __name__=="__main__": 
	main() 
 
 
raw_input() 
