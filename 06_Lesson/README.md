
![alt text](https://github.com/Elenn/processing_python/blob/main/06_Lesson/how/listShow.png?raw=true)

0. - Задача: Есть лист(список), который содержит положительные и отрицательные целые значения
```
myList = [3, -9, 8, 54, -1, 2]
```
- Если значение отрицательное, то заменить его на соответствующее положительное значение,
то есть -3 на 3.
- Представить в виде набора прямоугольников соответствующей длинны, перед которыми написано значение

---------------------------------------------------
1. Показываем содержимое листа(списка) в виде графика
```
def setup():
  textSize(18) 
  fill(0)
  strokeWeight(16)
  strokeCap(SQUARE)
  size(640, 360)
  noLoop()

def draw(): 
  background(0,255,0,16)
  myList = [3, -9, 8, 54, -1, 2]
  y = 100
  
  for value in myList: 
     if value < 0:
         value = value * -1
         
     text(value, 35, y + 6)    
     line(70, y, value*10 + 70, y)
     y =  y + 30 
```
----------------------------------------------------
2. Показываем имидж
```
bonusImage 

def setup(): 
  global bonusImage
  size(640, 360)
  bonusImage = loadImage("catRight.gif")  

def draw():
   background(255)
   image(bonusImage, 50, 150) 
```
----------------------------------------------------
3. - Котенок, который машет лапой
- Сохраняем несколько имиджей в лист
-  Меняем вызов имиджа (не на каждом вызове митодо draw, а только на каждом трицатом)
```
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
```
-------------------------------------------------------
4. #TODO: если сталкивается с пеньком, уменьшаем очки на 1
   #TODO: добавить бонус мешочки, до которых можно допрыгнуть
   #TODO: если очки будут равны нулю, то Gave Over 
```
i = 0 
x = -20
y = 350
jump = False
score = 10

def setup():  
  global runningGirlList 
  size(1140, 660) 
  
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
     
   fill(0)
   textSize(22) 
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
```


----------------------------------------------------
5. - Слайдер
- Определяем расстояние от положения курсора до линии слайдера:
- d = dist(mouseX, mouseY, x, height/2)
- первые два параметра это x,y положения курсора
- x - положение (x) кнопки слайдера
- height/2 - положение (y) слайдера по горизонтали

- соотносим ширину слайдера со шкалой от 0 до 100:
- map(mouseX, 50, width-50, 0, 100)
- первый параметр - это x положение курсора
- 2ой и 3ый параметра это реальное положение в пикселях начала и конца слайдера
- мы соотрносим начало слайдера значению 0, а конец слайдера значению 100
- это 4ый и 5ый параметры 

```
x = 50
score = 0 

def setup():
  textSize(50)
  textAlign(CENTER)
  fill(255)
  strokeWeight(16)
  size(640, 360)


def draw():
  global x
  global score
  background(0,255,0,16)
  line(50, height/2, width-50, height/2)
  
  ellipse(x, height/2, width/10, width/10)
  
  
  d = dist(mouseX, mouseY, x, height/2)
  
  if(d < 100 and mouseX > 50 and mouseX < width - 50):
    x = mouseX;
    score =  round(map(mouseX, 50, width-50, 0, 100)) 
    scoreText = "number: %s" % score
   
    text(scoreText, width/2, height/8)
```  