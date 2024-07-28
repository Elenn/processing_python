
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