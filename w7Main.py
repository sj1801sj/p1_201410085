import turtle
wn=turtle.Screen()
t1=turtle.Turtle()


def drawSquareAtSave(size, pos): 
    tracks=list()
    t1.penup() 
    t1.setpos(pos) 
    for i in range(0,4): 
        t1.pendown()
        t1.dot()
        t1.penup()
        t1.forward(size)
        t1.pendown()
        t1.dot()
        t1.penup()
        t1.right(90)
        tracks.append(t1.pos())
    return tracks

def lab7():
    size=100
    pos=t1.pos()
    mytracks=drawSquareAtSave(size,pos)
    print mytracks



def main():
    lab7()

if __name__=="__main__":
    main()

raw_input()