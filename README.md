# processing_lessons_01
![alt text](https://github.com/Elenn/processing_lessons/blob/main/How/01_Lesson_Circle.png?raw=true)
--------------------------------------------- 
0. Задание: 
Нарисуй снеговика
----------------------------------------
1.
- Даунлодим Processing
https://processing.org/download

-  Распаковываем zip
processing-4.3-windows-x64.zip

- Раним processing.exe

- Добавляем Python

Java -> Manage Models -> Python
-> Python Mode for Processing 4 -> Install

--------------------------------------
2. Раню первый скрипт
```
size(640, 360)
circle(320, 180, 100)
```
Где 320 - позиция центра x,
    180 - позиция центра y,
	100 - диаметр
	
circle(0, 0, 100) - координаты идут с верхнего левого угла	

---------------------------------------
3. Сохраняю как папку 
sketch_HelloCircle

в которой файл с кодом сохраняется как

sketch_HelloCircle.pyde

-----------------------------------------
4. setup() & draw()

C:\web\AlicaPython\Git\01_Lesson_Circle\sketch_setup_draw
```
def setup():
  size(640, 360)
  background(0)

def draw():
  noStroke()
  fill(255, 100, 200)
  circle(320, 180, 100)
```
------------------------------------------
5. Ты можешь рисовать и другие фигуры
https://processing.org/reference  

2d Primitives:
	circle() 
	ellipse()  
	line() 
	point() 
	rect() 
	square() 
	triangle()
-----------------------------------------
6. 
- Для того, что бы посмотреть, какие параметры нужны для каждой фигуры
- Выдели название фигуры
- Правая кнопка -> Find in Reference
- Смотрим параметры Parameters
- Так для круга
первый параметр x-coordinate (координата x)
второй параметр y-coordinate (координата y)
третий параметр width and height (ширина и длинна)

 

 
 








