import turtle
import math
tt = turtle
tt.shape('turtle')


def draw_regular_poligon(h , side_len):
    """
        Функция рисует многоугольныик
        h: количество вершин многоугольника
        side_len: длина стороны
    """
    for i in range(h):
        angle = 360/h
        tt.left(angle)
        tt.forward(side_len)
"""
# Упражнение 9  Вложеные многоугольники
n_poligons = 8 # уровень вложености
r1 = 30 # радиус описаной окружности наименьшей фигуры
h = 3   # начинаем с треугольника
dr1 = 20   # шаг увеличения радиуса

for i in range(n_poligons):
    a = 2*r1*math.sin(3.141592653589793*2/(2*h))
    ang = 360/h
    tt.penup()
    tt.goto(r1,0)
    tt.pendown()
    tt.left((180-ang)/2)
    draw_regular_poligon(h, a)
    tt.right((180-ang)/2)
    r1=r1+dr1
    h +=1
"""

def draw_round_L(step, quan_step):
    """
       рисуем влево
       Функция рисует круг двигаясь пошагово с  поворотом на угол
       который определяется количеством шагов
       step: длина шага
       quan_step: количество шагов
    """
    
    for i in range(quan_step):
        tt.forward(step)
        tt.left(360/quan_step)
        
def draw_round_R(step, quan_step): 
    """
         рисуем вправо
         Функция рисует круг двигаясь пошагово с  поворотом на угол
         который определяется количеством шагов
         step: длина шага
         quan_step: количество шагов
    """
    
    for i in range(quan_step):
        tt.forward(step)
        tt.right(360/quan_step)
        

def draw_flower(k):
    """
        рисуем из окружностей цветок
        k: количество лепестков
    """        
    for n in range(k):
        draw_round(10, 24)
        tt.left(360/k)

"""
# Упражнение 10 Цветок
draw_flower(5)
"""

# Упражнение 11 Бабочка

def draw_baterfly(n):
    """
        функция рисует бабочку из окружностей
        n: вложеность крыла бабочки
    """
    a = 10
    tt.left(90)
    for i in range(n):
        draw_round_L(a, 24)
        draw_round_R(a, 24)
        a += 2

"""
# Упражнение 11 Бабочка
draw_baterfly(6)
"""

def draw_2helf_round(step, quan_step):
    """
        функция рисует большой полукруг и заканчивает малым
        выглядит как один виток пружины
    """
    for i in range(quan_step):
        tt.forward(step)
        tt.right(180/quan_step)
    for i in range(quan_step):
        tt.forward(step/6)
        tt.right(180/quan_step)

def draw_spring(len_spring, Hi, quan_step):
    """
        Функция рисует пружину
        len_spring: длина витков пружины
        Hi: высота витка
        quan_step: количество шагов для рисования круга
    """
    tt.penup()
    tt.setx(-200)
    tt.pendown()
    tt.left(90)
    step = Hi/3.8
    
    for i in range(len_spring):
        draw_2helf_round(step, quan_step)
            
"""
# Упражнение 11 Пружина
draw_spring(10, 20, 18)
"""

def draw_smile(x, y, R):
    """
        Функция рисует смайл
        x, y: координаты центра окружности смайла
        R: радиус смайла
    """
    tt.speed(0)
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.begin_fill()
    tt.pencolor("black")
    tt.fillcolor("yellow")
    tt.pensize(2)
    tt.circle(R)
    tt.end_fill()
    Lipsy = y + R*2/3
    Lipsx = x + R/2
    tt.penup()
    tt.goto(Lipsx, Lipsy)
    tt.right(120)
    tt.pendown()
    tt.pencolor("red")
    tt.pensize(R/15)
    tt.circle(-(R*3/5), 120, None)
    tt.penup()
    Yeysy = y + R*3/2
    tt.goto(x-R/4, Yeysy)
    tt.pendown()
    tt.pensize(2)
    tt.begin_fill()
    tt.pencolor("black")
    tt.fillcolor("blue")
    tt.circle(R/6)
    tt.end_fill()
    tt.penup()
    tt.goto(x+R*6/12, Yeysy)
    tt.pendown()
    tt.pensize(2)
    tt.begin_fill()
    tt.pencolor("black")
    tt.fillcolor("blue")
    tt.circle(R/6)
    tt.end_fill()
    tt.penup()
    tt.goto(x, y+R)
    tt.pendown()
    tt.pensize(R/15)
    tt.pencolor("black")
    tt.setheading(270)
    tt.forward(R/3)
    tt.ht()

"""
Упражнение 13  Смайл 
draw_smile(20, 20, 100)
"""

def draw_star(n, size, collir):
    """
        функция рисует звезды с нечетным числом вершин
        n: количество вершин
        size: размер звезды
        collir: цвет звезды
    """
    if n%2 != 0:
        angle=180/n
        tt.begin_fill()
        tt.fillcolor(collir)
        tt.pencolor(collir)
        for i in range(n):
            tt.forward(size)
            tt.left(180-angle)
        tt.end_fill()
        tt.ht()
    else:
        print('Введено четное количество вершин. ')


"""
Упражнение 14 Звезды  
draw_star(7, 60, "green")
"""
