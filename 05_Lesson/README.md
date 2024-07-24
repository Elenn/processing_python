0. Задание: Создать поле из разноцветных квадратов (см. картинку)
случайных цветов
--------------------------
1. - for loop, range
- range(0, 64) вызываем исполнения кода внутри for loop 
каждый раз от 0 до 63 
-(то есть x принимает последовательно значения 0, 1, 2, 3 . . .63)
```
def setup():
   size(640, 360) 
 
def draw():
   background(0);
   fill(255) 
   
   for x in range(0, 64): 
       circle(x*10, 180, 10)
```	   
----------------------------
2. - for loop, range, increment by 10
- вызываем исполнения кода внутри for 
каждый раз от 0 до 639 с шагом 10
-(то есть x принимает последовательно значения 0, 10, 20, 30 . . .630)

```
def setup():
   size(640, 360) 
 
def draw():
   background(0);
   fill(255) 
   
   for x in range(0, 640, 10): 
       circle(x, 180, 10)
```	 
-------------------------------------
3. - Вложенные циклы: Nested for loops;
- noLoop() - вызываем метод draw() только одина раз 
- то есть мы повторяем созданную нами строчку из кругов еще и по высоте (y)
ellipseMode(CORNER)
- ellipseMode(CORNER): круг, это часный случай элипса, когда ширина равна высоте,
поэтому мы используем ellipseMode 
- значение CORNER - значит, что позицию x и y мы определяем у левого верхнего
угла квадрата, в который вписан наш круг
```
def setup():
   size(640, 360)
   noLoop()   
 
def draw():
   background(0);
   fill(255)
   circleWidth = 60 
   
   ellipseMode(CORNER)  
   
   for x in range(0, 640/circleWidth + 1): 
       for y in range(0, 360/circleWidth): 
           circle(x*circleWidth, y*circleWidth, circleWidth)
```		   







  