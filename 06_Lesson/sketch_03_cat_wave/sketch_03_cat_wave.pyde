i = 0 

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
   background(255) 
   image(catImageList[i], 50, 150) 
   if (frameCount%30==0 and i == (len(catImageList) - 1)): 
      i = 0
   elif(frameCount%30==0): 
      i = i + 1   
      
       
     
   
    
