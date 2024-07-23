y=10
x=10
speedX = 1
speedY = 1

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
    global y
    global speedX
    global speedY
    
    if(x == 0  or x > width ): 
        speedX = speedX * -1 
    elif( y == 0  or y > height):
        speedY = speedY * -1   
                                   
    x = x + speedX
    y = y + speedY
    
    circle(x, y, 50) 
    
