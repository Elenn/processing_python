i = 0 
x = -20
y = 350
jump = False
score = 10

def setup():  
  global runningGirlList 
  size(1140, 660)
  
  textSize(18)
  
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
  
def keyPressed():
  global y 
  global jump
  global beforeJumpY
  if (key == CODED):  
    if (keyCode == UP):
      beforeJumpY = y 
      jump = True
      y = y - 100   

def draw():
   global i
   global x
   global y
   global score 
   background(155) 
   image(runningGirlList[i], x, y) 
   rect(250, 475, 20, 20 )
   rect(750, 475, 20, 20 )
   
   textSize(22) 
   fill(0)
   #strokeWeight(16)
   formatedText = "Your score: %s" % score
   text(formatedText, 10, 50);
   
   #TODO: если сталкивается с пеньком, уменьшаем очки на 1
   #TODO: добавить бонус мешочки, до которых можно допрыгнуть
   #TODO: если очки будут равны нулю, то Gave Over 
   
   if(frameCount%10==0):
      x = x + 10
      #после прыжка возвращаемся на свой уровень по y
      if(jump and y < beforeJumpY):
          i = 4
          y = y + 5
          
      #если добежал до правого края, возвращаем в начало    
      elif x > width - 100:
          x = 0
          
      #если доходим до последнего имиджа в листе runningGirlList, то начинаем с первого имиджа     
      elif (i == (len(runningGirlList) - 1)): 
          i = 0 
      else: 
          i = i + 1 
          
       
            
      
       
     
   
    
