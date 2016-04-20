import turtle
wn=turtle.Screen()
t1=turtle.Turtle()

def drawSquareFromList(tracks):
    t1.penup()
    for i in range(0, len(tracks)):
        t1.goto(tracks[i])
        t1.pendown()
        for j in range(0,4):
            t1.forward(100)
            t1.right(90)
        t1.penup()

points = [(-200, 350), (-100, -275), (120, -200), (-270, -120), (320, 52), (0, 0), (224,289), (-20, 400), (-190, 10), (-255, 120)]
drawSquareFromList(points)
