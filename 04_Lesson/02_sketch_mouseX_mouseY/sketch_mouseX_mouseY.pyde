circleX = 10
circleY = 180

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    circleX = mouseX 
    circleY = mouseY
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, circleY, 100)
    
    circleX = circleX + 1; 
