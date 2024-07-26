speedX = 1
speedY = 1
rectX = 50
rectY = 310
x = random(10, 50)
y = 10

def setup():
    size(640, 360)
    
def keyPressed():
  global rectX 
  if (key == CODED): 
    if (keyCode == RIGHT):
      rectX = rectX + 5;
    elif (keyCode == LEFT):
      rectX = rectX - 5;  
    
def draw():
    background(0) 
    score = 0
    textSize(25);
    fill(255); 
    
    global x
    global y
    global speedX
    global speedY
    
    if(x <= 0  or x > width ): 
        speedX = speedX * -1 
    if( y <= 0 ):
        speedY = speedY * -1 
    if (y > rectY and x > rectX  and x < (rectX + 200)):
        speedY = speedY * -1
        score = score + 1
    if y >= height: 
        speedX = 0
        speedY = 0  
        text("Game over", 10, 50);                   
                                   
    x = x + speedX
    y = y + speedY
    
    fill(255,0,0)
    circle(x, y, 30)
    
    fill(0,255,0) 
    rect(rectX,rectY,200,20)
    
