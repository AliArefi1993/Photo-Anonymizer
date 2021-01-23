#photoanonymizer.pyw
# This porogram draw a face on photo
# Writen by: ALi Arefi

from tkinter.filedialog import askopenfilename
from graphics import *

def radius(p1,p2):
    return ((p1.getX()  - p2.getX()) ** 2 +(p1.getY()  - p2.getY()) ** 2 ) ** 0.5

def drawFace(center, size, win):
    face = Circle(center, size)
    face.setOutline("black")
    face.setFill("white")
    face.draw(win)
    X = center.getX()
    Y = center.getY()
    
    left_eye = Circle(Point(X-size/2, Y+size/2), size/10)
    left_eye.setOutline("black")
    left_eye.setFill("blue")
    left_eye.draw(win)
    right_eye = left_eye.clone()
    right_eye.move(size,0)
    right_eye.draw(win)
    
    left_eyebrow = Oval(Point(X-size*3/4, Y+size/2+size/7),
                        Point(X-size*1/4, Y+size/2+size/4))
    left_eyebrow.setOutline("black")
    left_eyebrow.setFill("black")
    left_eyebrow.draw(win)
    right_eyebrow = left_eyebrow.clone()
    right_eyebrow.move(size,0)
    right_eyebrow.draw(win)

    nose = Rectangle(Point(X-size/7,Y-size/7), Point(X+size/7,Y+size/2+size/10))
    nose.setOutline("black")
    nose.setFill("grey")
    nose.draw(win)

    mouth = Oval(Point(X-size/2,Y-size/2), Point(X+size/2,Y-size/2+size/5))
    mouth.setOutline("black")
    mouth.setFill("red")
    mouth.draw(win)


def main():
    win = GraphWin("",300,300)
    win.setCoords(0,0,20,23)
    
    filename = askopenfilename()
    pic = Image(Point(10,10), filename)
    pic.draw(win)
    message = Text(Point(10,22.3), "How many face are to be blocked? ")
    entryN = Entry(Point(8,20.6), 3).draw(win)
    message.draw(win)
    message2 = Text(Point(14,20.6), "if you sure click!").draw(win)
    win.getMouse()
    entryN.undraw()
    message2.undraw()
    n = int(entryN.getText())
    for i in range(n):
        message.setText("Click the center of face")
        P1 = win.getMouse()
        message.setText("Click the center edge of face")
        P2 = win.getMouse()
        drawFace(P1, radius(P1,P2), win)


    message.setText("Click to quit")
    win.getMouse()
    win.close()

main()
         
