circleX = 10

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    circleX = 0 
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, 180, 100)
    
    circleX = circleX + 1; 
