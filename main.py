import turtle as trtl 

# set turtle pencolor to teal
trtl.pencolor("teal")

trtl.speed(10)
# draw six hexagons
for i in range(6):
  trtl.circle(50, 360, 6)
  trtl.penup()
  trtl.forward(10)
  trtl.pendown()

# move turtle to (0, -100)
trtl.penup()
trtl.goto(0, -100)
trtl.pendown()

# make turtle pencolor green
trtl.pencolor("green")

# draw five triangles
for i in range (5):
  trtl.circle(50, 360, 3)
  trtl.penup()
  trtl.forward(20)
  trtl.pendown()