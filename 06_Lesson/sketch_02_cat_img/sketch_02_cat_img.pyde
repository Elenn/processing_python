bonusImage 

def setup(): 
  global bonusImage
  size(640, 360)
  bonusImage = loadImage("catRight.gif")  

def draw():
   background(255)
   image(bonusImage, 50, 150) 
   
    
