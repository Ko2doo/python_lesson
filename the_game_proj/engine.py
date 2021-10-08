'''
Пробуем создать танки

'''

# import module
from graph import *

# Определяем размеры ячеек поля и храним значения в переменных
cellSize = 10
fieldCellWidth = 30
fieldCellHeight = 30
fieldWidth = cellSize * fieldCellWidth
fieldHeight = cellSize * fieldCellHeight


# Используя переменные, создаём функцию и передаём координаты фигуре:
def playingField(y, x):
	return rectangle((x - 1) * cellSize, (y - 1) * cellSize,
					  x * cellSize, y * cellSize)


# Отрисовываем игровое поле, красим в нужные цвета ячейки и обводку:
def initField():
	global field, fieldId # Глобальные переменные
	fild = [ [0] * (fieldCellHeight + 2) for i in range(fieldCellWidth * 2) ]
	fieldId = [ [0] * (fieldCellHeight + 2) for i in range(fieldCellWidth * 2) ]
	penColor("lightgray"); # Цвет пера (обводка)
	brushColor("white") # Цвет заливки ячеек
	# В цикле отрисовываем клетки на игровом поле, по +1 клетке
	for y in range(1, fieldCellHeight + 1):
		for x in range(1, fieldCellWidth + 1):
			fieldId[y][x] = playingField(y, x)


# Рисуем фигуру (танк)
def spawnObj():
	global x, y, rectangleDefault #Объявление глобальных переменных
	x = 30
	y = 30
	penColor("lightgray")
	brushColor("blue")
	rectangleDefault = rectangle(0, 0, x, y)
	return rectangleDefault


# функция контроля объектов
def objControl():
	global obj, rectangleDefault #Объявление глобальных переменных

	obj = rectangleDefault #говорим что переменная obj это rectangleDefault

	'''
	# Вешаем события на клавишы чтобы управлять квадратом на поле
	# VK_RIGHT - право
	# VK_LEFT - лево
	# VK_DOWN - вниз
	# VK_UP - наверх
	'''
	def keyPressed(event):
		if event.keycode == VK_RIGHT:
			moveObjectBy(obj, 5, 0)
		elif event.keycode == VK_LEFT:
			moveObjectBy(obj, -5, 0)
		elif event.keycode == VK_DOWN:
			moveObjectBy(obj, 0, 5)
		elif event.keycode == VK_UP:
			moveObjectBy(obj, 0, -5)
		elif event.keycode == VK_ESCAPE:
			close()

	'''
		используем коллбэк и выззываем наш обработчик клавиш,
		не забываем про функцию onKey(обработчик)
	'''
	return onKey(keyPressed)

# функция принимающая в себя вызов всех функий
def main():
	# Описание функции
	windowSize(fieldWidth, fieldHeight + 45) #размер окна приложения
	canvasSize(fieldWidth, fieldHeight)

	# вызываем все функции программы тут:
	initField()
	spawnObj()
	objControl()
	run()


main()
