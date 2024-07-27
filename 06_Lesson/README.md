
![alt text](https://github.com/Elenn/processing_python/blob/main/06_Lesson/how/listShow.png?raw=true)

0. - Задача: Есть лист, который содержит положительные и отрицательные целые значения
```
myList = [3, -9, 8, 8, -1, 2]
```
- Если значение отрицательное, то заменить его на соответствующее положительное значение,
то есть -3 на 3.
- Представить в виде набора прямоугольников соответствующей длинны, перед которыми написано значение

---------------------------------------------------
1. - Слайдер
- Определяем расстояние от положения курсора до линии слайдера:
- d = dist(mouseX, mouseY, x, height/2)
- первые два параметра это x,y положения курсора
- x - положение (x) кнопки слайдера
- height/2 - положение (y) слайдера по горизонтали

- соотносим ширину слайдера со шкалой от 0 до 100:
- map(mouseX, 50, width-50, 0, 100)
- первый параметр - это x положение курсора
- 2ой и 3ый параметра это реальное положение в пикселях н
начала и конца слайдера
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