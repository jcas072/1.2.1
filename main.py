# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----game configuration----
spotColor = "pink"
spotShape = "circle"
spotSize = 2
score = 0
font_setup = ("Arial", 20, "normal")

timer = 15
counter_interval = 1000  #1000 represents 1 second
timer_up = False

#-----initialize turtle-----
spot = trtl.Turtle()

spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.penup()

score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(-180, 170)

counter = trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(50, 170)


#-----game functions--------
def spot_clicked(x, y):
  if timer_up == False:
    change_position()
    update_score()


def change_position():
    new_xpos = rand.randint(-180, 180)
    new_ypos = rand.randint(-140, 140)
    spot.hideturtle()
    spot.goto(new_xpos, new_ypos)
    spot.showturtle()


def update_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)


def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=font_setup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=font_setup)
        timer -= 1
        counter.getscreen().ontimer(countdown, counter_interval)


#-----events----------------
spot.onclick(spot_clicked)

wn = trtl.Screen()
wn.ontimer(countdown, counter_interval)
wn.mainloop()
