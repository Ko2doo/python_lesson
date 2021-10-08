#import lib graph
from graph import *


""" Рисуем квадрат """
penColor("black")
brushColor("green")
rectangle(150, 100, 250, 200)

""" Рисуем полигон в виде треугольника (крыша) """

penColor("black")
brushColor("blue")
polygon([ (100, 100), (200, 50),
			(300, 100) ])


""" Рисуем окно в доме """
# рама
penColor("white")
brushColor("black")
rectangle(100, 150, 50, 200)


run()


