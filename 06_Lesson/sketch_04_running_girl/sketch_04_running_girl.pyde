i = 0 
x = -20

def setup():  
  global runningGirlList 
  size(640, 360)
  
  runningGirlList = []
  runningGirl1 = loadImage("runningGirl1.gif") 
  runningGirl2 = loadImage("runningGirl2.gif") 
  runningGirl3 = loadImage("runningGirl3.gif") 
  runningGirl4 = loadImage("runningGirl4.gif") 
  runningGirl5 = loadImage("runningGirl5.gif") 
  runningGirl6 = loadImage("runningGirl6.gif") 
  runningGirl7 = loadImage("runningGirl7.gif") 
  runningGirl8 = loadImage("runningGirl8.gif") 
  runningGirl9 = loadImage("runningGirl9.gif")
  runningGirl10 = loadImage("runningGirl10.gif") 
  runningGirl11 = loadImage("runningGirl11.gif") 
  runningGirl12 = loadImage("runningGirl12.gif")   
  
  runningGirlList.append(runningGirl1)
  runningGirlList.append(runningGirl2)
  runningGirlList.append(runningGirl3)
  runningGirlList.append(runningGirl4)
  runningGirlList.append(runningGirl5)
  runningGirlList.append(runningGirl6)
  runningGirlList.append(runningGirl7)
  runningGirlList.append(runningGirl8)
  runningGirlList.append(runningGirl9) 
  runningGirlList.append(runningGirl10) 
  runningGirlList.append(runningGirl11) 
  runningGirlList.append(runningGirl12) 

def draw():
   global i
   global x
   background(155) 
   image(runningGirlList[i], x, 150) 
   if(frameCount%10==0):
      if x > width - 100:
          x = 0
      x = x + 10  
      if (i == (len(runningGirlList) - 1)): 
        i = 0 
      else: 
        i = i + 1  
      
       
     
   
    
