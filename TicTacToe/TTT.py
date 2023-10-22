import turtle

wn = turtle.Screen()
wn.title("Tic Tac Toe")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

X = []
O = []

pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -150)
pen.write("   |   |\n"
"   |   |\n"
"___|___|___\n"
"   |   |\n"
"   |   |\n"
"___|___|___\n"
"   |   |\n"
"   |   |\n"
"   |   |\n", align="center", font=("Courier", 24, "bold"))

def A1():
    if A1 in X:
        print("X")
    elif A1 in O:
        print("O")
    else:
        print("")

def A2():
    if A2 in X:
        print("X")
    elif A2 in O:
        print("O")
    else:
        print("")

def A3():
    if A3 in X:
        print("X")
    elif A3 in O:
        print("O")
    else:
        print("")

def B1():
    if B1 in X:
        print("X")
    elif B1 in O:
        print("O")
    else:
        print("")

def B2():
    if B2 in X:
        print("X")
    elif B2 in O:
        print("O")
    else:
        print("")

def B3():
    if B3 in X:
        print("X")
    elif B3 in O:
        print("O")
    else:
        print("")

def C1():
    if C1 in X:
        print("X")
    elif C1 in O:
        print("O")
    else:
        print("")

def C2():
    if C2 in X:
        print("X")
    elif C2 in O:
        print("O")
    else:
        print("")

def C3():
    if C3 in X:
        print("X")
    elif C3 in O:
        print("O")
    else:
        print("")

while True:
    wn.update()

    turn = 1

    if turn == 1:
        wn.listen()
        wn.onkeypress(X.append(A1), "1")
        wn.onkeypress(X.append(A2), "2")
        wn.onkeypress(X.append(A3), "3")
        wn.onkeypress(X.append(B1), "4")
        wn.onkeypress(X.append(B2), "5")
        wn.onkeypress(X.append(B3), "6")
        wn.onkeypress(X.append(C1), "7")
        wn.onkeypress(X.append(C2), "8")
        wn.onkeypress(X.append(C3), "9")
    
    turn = 0

    if turn == 0:
        wn.listen()
        wn.onkeypress(O.append(A2), "2")
        wn.onkeypress(O.append(A1), "1")
        wn.onkeypress(O.append(A3), "3")
        wn.onkeypress(O.append(B1), "4")
        wn.onkeypress(O.append(B2), "5")
        wn.onkeypress(O.append(B3), "6")
        wn.onkeypress(O.append(C1), "7")
        wn.onkeypress(O.append(C2), "8")
        wn.onkeypress(O.append(C3), "9")
