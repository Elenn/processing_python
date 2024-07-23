y=10
x=10

def setup():
    size(640, 360)  
    
def draw():
    background(0) 
    
    global x
    x = x + 1  
    
    circle(x, y, 50) 
    
