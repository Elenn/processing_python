

![alt text](https://github.com/Elenn/processing_python/blob/main/02_Lesson/how/lesson_02.png?raw=true)

0. Задание:
- Создай фигуру, состоящую из 
rect(), square(), triangle(), circle() or line()
- Перенеси код для фигуры в метод
- Вызови этот метод несколько раз с разными параметрами, так, что бы фигура
оказалась нарисована несколько раз
-----------------------------------------------
1. - Создай фигуру, в которой используются

    rect()
    square()  
    triangle() 
    circle()

- Раскрась их в разные цвета с помошью fill()
- Образец:
```
def setup():
    size(640, 360)
    
def draw():
    background("#FFFFCC")
    
    fill("#006600")
    rect(390, 135, 30, 100)
    square(320, 200, 100) 
    
    fill("#666600")
    triangle(320, 200, 370, 150, 420, 200) 
    
    square(350, 240, 40) 
    fill("#666600")
    
    fill("#FFFF00")
    circle(10,10,100) 
```	
------------------------------------------------------
2. - Перенеси код для твоей фигуры в метод
- Вызови твой метод внутри метода draw()
- Образец:

```
def setup():
    size(640, 360)
    frameRate(1)
    
def house():
    fill("#006600")
    rect(390, 135, 30, 100)
    square(320, 200, 100) 
    
    fill("#666600")
    triangle(320, 200, 370, 150, 420, 200) 
    
    square(350, 240, 40) 
    fill("#666600")  
    
def draw():
    background("#FFFFCC")  
     
    house() 
    
    fill("#FFFF00")
    circle(10,10,100) 
```
---------------------------------------------------
3. Метод с параметрами
- Я хочу вызывать метод несколько раз с разными
значениями параметра x
- В результате будет нарисовано несколько фигур
```
x = 320
y = 135

def setup():
    size(640, 360)
    frameRate(1)
    
def house(x,y):
    fill("#006600")
    rect(x + 70, y, 30, 100)
    square(x, 200, 100) 
    
    fill("#666600")
    triangle(x, y + 65, x + 50, y + 15, x + 100, 200) 
    
    square(x + 30, y + 105, 40) 
    fill("#666600") 
        
    
def draw():
    background("#FFFFCC")  
     
    house(x,y)
    house(x+150,y)
    house(x-150,y)
    
    fill("#FFFF00")
    circle(10,10,100)
``` 





     
