import turtle as trtl 

# set turtle pencolor to teal
trtl.pencolor("teal")

# draw six hexagons
for i in range(6):
  trtl.circle(50, 360, 6)
  trtl.penup()
  trtl.forward(10)
  trtl.pendown()