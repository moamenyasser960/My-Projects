print("\\" * 28,'\b\\')
all = float(input("===- enter the ball speed: "))
print("//////////////////////////////\\")
all1 = float(input("enter the ball racket speed: "))
print("\\" * 28,'\b\\\\\\\\\\')

import turtle
import winsound

wind = turtle.Screen()
wind.title("block the ball")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

# المضرب الأول

madrab1 = turtle.Turtle()
madrab1.speed(0)
madrab1.shape("square")
madrab1.color("blue")
madrab1.shapesize(stretch_wid=6, stretch_len=1)
madrab1.penup()
madrab1.goto(-377, 0)

# المضرب الثاني

madrab2 = turtle.Turtle()
madrab2.speed(0)
madrab2.shape("square")
madrab2.color("red")
madrab2.shapesize(stretch_wid=6, stretch_len=1)
madrab2.penup()
madrab2.goto(370, 0)

# ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = all
ball.dy = all

# score
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write("Player 1: 0 Player 2: 0", align="center", font=("Courier", 24, "normal"))


# functions

def madrab1_up():
    y = madrab1.ycor()
    y += all1
    madrab1.sety(y)


def madrab1_down():
    y = madrab1.ycor()
    y -= all1
    madrab1.sety(y)


def madrab2_up():
    y = madrab2.ycor()
    y += all1
    madrab2.sety(y)


def madrab2_down():
    y = madrab2.ycor()
    y -= all1
    madrab2.sety(y)


# keyboard bindings

wind.listen()
wind.onkeypress(madrab1_up, "w")
wind.onkeypress(madrab1_down, "s")
wind.onkeypress(madrab2_up, "Up")
wind.onkeypress(madrab2_down, "Down")

while True:
    wind.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    # border check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)
    if ball.ycor() < -280:
        ball.sety(-280)
        ball.dy *= -1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)
        score.clear()
        score.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # khabtet el madrab w coura

    if (350 < ball.xcor() < 365) and (madrab2.ycor() + 70 > ball.ycor() > madrab2.ycor() - 75):
        ball.setx(350)
        ball.dx *= -1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)

    if (-357 > ball.xcor() > -365) and (madrab1.ycor() + 70 > ball.ycor() > madrab1.ycor() - 75):
        ball.setx(-357)
        ball.dx *= -1
        winsound.PlaySound("arabic.mp3", winsound.SND_ASYNC)
