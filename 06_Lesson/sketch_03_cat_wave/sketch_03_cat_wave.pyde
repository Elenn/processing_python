i = 0 
x = 100

def setup():  
  global catImageList 
  size(640, 360)
  
  catImageList = []
  catRight = loadImage("catRight.gif") 
  catUp = loadImage("catUp.gif") 
  
  catImageList.append(catRight)
  catImageList.append(catUp)  

def draw():
   global i
   global x
   background(255) 
   image(catImageList[i], x, 150) 
   if(frameCount%30==0):
      x = x + 10  
      if (i == (len(catImageList) - 1)): 
        i = 0 
      else: 
        i = i + 1  
      
       
     
   
    
