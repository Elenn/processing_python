y=10
x=10

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
    global y
    x = x + 1 
    y = y + 1 
    
    circle(x, y, 50) 
    
