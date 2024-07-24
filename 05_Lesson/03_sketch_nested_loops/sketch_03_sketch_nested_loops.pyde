def setup():
   size(640, 360)
   noLoop()   
 
def draw():
   background(0);
   fill(255)
   circleWidth = 60 
   
   ellipseMode(CORNER)  
   
   for x in range(0, 640/circleWidth + 1): 
       for y in range(0, 360/circleWidth): 
           circle(x*circleWidth, y*circleWidth, circleWidth)
 
   
   
 
