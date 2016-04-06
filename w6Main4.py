"""
@author psj
@since 160406
"""

def sumMultipled3_5(begin,end):
    sum=0
    for i in range(begin, end):
        if (i%3  == 0 or i%5 == 0):
            sum=sum + i
    print sum
    return sum


def leapyear():
    sel=int(raw_input("press the year"))
    if (sel%4 == 0) and (sel%100 !=0 or sel%400 == 0):
        print "this year is leap year"
    else:
        print "this year is not leap year"


def lab6():
    sumMultipled3_5(0,1001)
    leapyear()

def main():
    lab6()

if __name__=="__main__":
    main()

raw_input()