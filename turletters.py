import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)

    elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.fd(30)
	tur.left(90)
	tur.fd(20)
	tur.left(90)
	tur.fd(30)
	tur.backward(20)
	tur.right(90)
	tur.fd(30)
	tur.left(90)
	tur.fd(20)
    elif letter == "C": 
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.fd(30)
	tur.backward(30)
	tur.left(90)
	tur.fd(50)
	tur.right(90)
	tur.fd(30)
    elif letter == "D":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.circle(25,180)
    elif letter == "E":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.fd(30)
	tur.backward(30)
	tur.left(90)
	tur.fd(25)
	tur.right(90)
	tur.fd(30)
	tur.backward(30)
	tur.left(90)
	tur.fd(25)
	tur.right(90)
	tur.fd(30)
    elif letter == "F":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.backward(25)
	tur.left(90)
	tur.fd(30)
	tur.backward(30)
	tur.left(90)
	tur.fd(25)
	tur.right(90)
	tur.fd(30)
    elif letter == "G":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.fd(30)
	tur.left(90)
	tur.fd(15)
	tur.right(90)
	tur.fd(3)
	tur.backward(10)
	tur.pu()
	tur.left(90)
	tur.fd(35)
	tur.left(90)
	tur.pd()
	tur.fd(20)
	tur.backward(20)
    elif letter == "H":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.backward(25)
	tur.left(90)
	tur.fd(30)
	tur.left(90)
	tur.fd(25)
	tur.backward(50)
    elif letter == "I":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.left(90)
	tur.pu()
	tur.fd(15)
	tur.right(90)
	tur.pd()
	tur.fd(50)
    elif letter == "J":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.left(90)
	tur.fd(30)
	tur.backward(15)
	tur.right(90)
	tur.fd(50)
	tur.right(90)
	tur.fd(15)
	tur.right(90)
	tur.fd(10)
    elif letter == "K":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.backward(25)
	tur.left(50)
	tur.fd(35)
	tur.backward(35)
	tur.left(70)
	tur.fd(30)
    elif letter == "L":
	tur.width(5)
	tur.pu()
	tur.setheading(0)
	tur.fd(5)
	tur.right(90)
	tur.fd(5)
	tur.pd()
	tur.fd(50)
	tur.left(90)
	tur.fd(30)
	tur.backward(30)
	tur.left(90)
	tur.fd(50)
	tur.right(90)
    elif letter == "M": #END
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	    pass
    elif letter == "R":
	    pass
    elif letter == "S":
	    pass
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
