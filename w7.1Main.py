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
	tracks.append(t1.pos())
	t1.penup()
	t1.forward(size)
	t1.right(90)
    return tracks

def drawSquareFromList(tracks):
    t1.penup()
    t1.goto(tracks[0])
    t1.pendown()
	for i in range(0,4):
	t1.forward(size)
	t1.right(90)



def lab7():
    mytracks=list()
    size=100
    pos=t1.pos()
    mytracks=drawSquareAtSave(size,pos)
    drawSquareFromList(mytracks)




def main():
    lab7()

if __name__=="__main__":
    main()

raw_input()