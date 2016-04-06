

def leapyear():
    sel=int(raw_input("press the year"))
    if (sel%4 == 0) and (sel%100 !=0 or sel%400 == 0):
        print "this year is leap year"
    else:
        print "this year is not leap year"

leapyear()

raw_input()