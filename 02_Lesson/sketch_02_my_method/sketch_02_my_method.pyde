def setup():
    size(640, 360)
    frameRate(1)
    
def house():
    fill("#006600")
    rect(390, 135, 30, 100)
    square(320, 200, 100) 
    
    fill("#666600")
    triangle(320, 200, 370, 150, 420, 200) 
    
    square(350, 240, 40)  
    
def draw():
    background("#FFFFCC")  
     
    house() 
    
    fill("#FFFF00")
    circle(10,10,100) 
