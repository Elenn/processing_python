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
    circleSize = random(50, 120);
     
    noStroke()
    fill(0, 255, 0, 28);
    circle(circleX, circleY, circleSize)
    
    circleX = circleX + 1; 
