import turtle
import winsound

wn = turtle.Screen()

wn.title("PONG")

wn.bgcolor("black")

wn.setup(width=800, height=600)

wn.tracer(0)

score_a=0

score_b=0

paddle_a=turtle.Turtle()

paddle_a.speed(0)

paddle_a.shape("square")

paddle_a.shapesize(stretch_wid=5,stretch_len=1)

paddle_a.color("white")

paddle_a.penup()

paddle_a.goto(-350,0)




paddle_b=turtle.Turtle()

paddle_b.speed(0)

paddle_b.shape("square")

paddle_b.shapesize(stretch_wid=5,stretch_len=1)

paddle_b.color("white")

paddle_b.penup()

paddle_b.goto(350,0)



ball=turtle.Turtle()

ball.speed(0)

ball.shape("square")

ball.color("white")

ball.penup()
ball.goto(0,0)
ball.dx=0.2

ball.dy=0.2

pen = turtle.Turtle()



pen.color("white")

pen.penup()

pen.hideturtle()

pen.goto(0,260)

pen.write(f"Player A : {score_a}  Player B : {score_b}",align="center",font=("beauti_font.otf",24,"normal"))

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    if(y>=250):
        y=250
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    if(y<=-250):
        y=-250
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    if(y>=250):
        y=250
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    if(y<=-250):
        y=-250
    paddle_b.sety(y)

wn.listen()

wn.onkeypress(paddle_a_up,"w")
wn.onkeypress(paddle_a_down,"s")

wn.onkeypress(paddle_b_up,"Up")
wn.onkeypress(paddle_b_down,"Down")

while True:
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    if ball.ycor()>=290:
        winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy*=-1
    
    if ball.xcor()>=390:
        score_a+=1
        pen.clear()
        pen.write(f"Player A : {score_a}  Player B : {score_b}",align="center",font=("beauti_font.otf",24,"normal"))
        ball.goto(0,0)
        ball.dx*=-1

    if ball.ycor()<=-290:
        winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()<=-390:
        score_b+=1
        pen.clear()
        pen.write(f"Player A : {score_a}  Player B : {score_b}",align="center",font=("beauti_font.otf",24,"normal"))
        ball.goto(0,0)
        ball.dx*=-1
        
    
    if ball.xcor()>=330 and ball.xcor()<=350 and ball.ycor()<=paddle_b.ycor()+60 and ball.ycor()>=paddle_b.ycor()-60:
        winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
        ball.dx*=-1
    
    if ball.xcor()<=-330 and ball.xcor()>=-350 and ball.ycor()<=paddle_a.ycor()+60 and ball.ycor()>=paddle_a.ycor()-60:
        winsound.PlaySound("collision.wav",winsound.SND_ASYNC)
        ball.dx*=-1
    
    wn.update()