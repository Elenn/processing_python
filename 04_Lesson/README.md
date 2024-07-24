0. Задание: Написать код, когда при нажатии мышки
меняется цвет круга на случайный: r = random(0, 255)
- то есть использовать в fill(255, 100, 200) 
переменные fill(r,b,g)
- что бы их изменить в методе mousePressed()
надо обявить эти три переменные global
----------------------------------------------
1. mousePressed()

```
circleX = 10

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    circleX = 0 
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, 180, 100)
    
    circleX = circleX + 1; 
```	
----------------------------------------------
2. mouseX
   mouseY
   
```
circleX = 10
circleY = 180

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    circleX = mouseX 
    circleY = mouseY
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(255, 100, 200)
    circle(circleX, circleY, 100)
    
    circleX = circleX + 1; 
``` 
-----------------------------------------------
3. move mouse => change background
```
def setup():
  size(640, 360) 
  

def draw():  
  if mouseX > 320:
     background(255)
  else:
     background(0) 
   
  
  stroke(127)
  strokeWeight(4)
  line(320,0,320, height)
```
----------------------------------------------
4. степень прозрачности для fill(), четвертый параметр
- random(50, 120) - случайное значение от 50 до 120
 
``` 
circleX = 10
circleY = 180

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    circleX = mouseX 
    circleY = mouseY
        
    
def draw():
    global circleX
    background("#FFFFCC")  
    circleSize = random(50, 120);
     
    noStroke()
    fill(0, 255, 0, 28);
    circle(circleX, circleY, circleSize)
    
    circleX = circleX + 1;
```
---------------------------------------------------------
5. toggle
startMoving = not startMoving
- нажимаем первый раз - движение останавливается
- нажимаем второй раз - движение начинается

```
circleX = 10
circleY = 180
startMoving = True

def setup():
    size(640, 360)
        
def mousePressed():
    global circleX
    global circleY
    global startMoving
    circleX = mouseX 
    circleY = mouseY
    startMoving = not startMoving
    print(startMoving)
        
    
def draw():
    global circleX
    background("#FFFFCC")  
     
    noStroke()
    fill(0, 255, 0);
    circle(circleX, circleY, 80)
    
    if startMoving:
        circleX = circleX + 1; 
```	
   
   
   
   
   