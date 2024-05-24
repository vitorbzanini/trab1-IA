# importing the required libraries
import pygame as pg
import sys
import time
from pygame.locals import *
import numpy as np
import pickle 
from statistics import mode

# declaring the global variables

# for storing the 'x' or 'o'
# value as character
#XO = 'x'
XO = 0

# storing the winner's value at
# any instant of code
winner = 2 

# to check if the game is a draw
draw = None

# to set width of the game window
width = 400

# to set height of the game window
height = 400

# to set background color of the
# game window
white = (255, 255, 255)

# color of the straightlines on that
# white game board, dividing board
# into 9 parts
line_color = (0, 0, 0)

# setting up a 3 * 3 board in canvas
board = np.array([[-1]*3, [-1]*3, [-1]*3])


# initializing the pygame window
pg.init()

# setting fps manually
fps = 30

# this is used to track time
CLOCK = pg.time.Clock()

# this method is used to build the
# infrastructure of the display
screen = pg.display.set_mode((width, height + 100), 0, 32)

# setting up a nametag for the
# game window
pg.display.set_caption("My Tic Tac Toe")

# loading the images as python object
initiating_window = pg.image.load("original.jpg")
x_img = pg.image.load("X_modified.png")
y_img = pg.image.load("o_modified.png")
restart_img = pg.image.load("restart1.jpg")

# resizing images
#initiating_window = pg.transform.scale(
initiating_window = pg.transform.scale(initiating_window, (width, height + 100))
x_img = pg.transform.scale(x_img, (80, 80))
o_img = pg.transform.scale(y_img, (80, 80))
restart_img = pg.transform.scale(restart_img, (400, 400))

screen.blit(initiating_window, (0, 0))
pg.display.update()
time.sleep(3)

def game_initiating_window():

	# displaying over the screen
	#screen.blit(initiating_window, (0, 0))

	# updating the display
	#pg.display.update()
	#time.sleep(3)
	screen.fill(white)

	# drawing vertical lines
	pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
	pg.draw.line(screen, line_color, (width / 3 * 2, 0),
				(width / 3 * 2, height), 7)

	# drawing horizontal lines
	pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
	pg.draw.line(screen, line_color, (0, height / 3 * 2),
				(width, height / 3 * 2), 7)
	draw_status()


def draw_status():

	# getting the global variable draw
	# into action
	global draw

	message = ""
	if winner == 3: 
		message = "Empate"
	elif winner == 2:
		message = "Tem jogo"
	elif winner == 1:
		message = "O ganhou"
	elif winner == 0:
		message = "X ganhou"

	# setting a font object
	font = pg.font.Font(None, 50)

	# setting the font properties like
	# color and width of the text
	text = font.render(message, 1, (255, 255, 255))	

	# copy the rendered message onto the board
	# creating a small block at the bottom of the main display
	screen.fill((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center=(width / 2, 500-50))
	screen.blit(text, text_rect)
	pg.display.update()


def check_win():
	global board, winner, draw

	print("board: ", board.flatten())

	loaded_model_KNN = pickle.load(open("KNN_model.sav", 'rb'))
	loaded_model_DTC = pickle.load(open("DTC_model.sav", 'rb'))
	loaded_model_MLP = pickle.load(open("MLP_model.sav", 'rb'))

	predict_KNN = loaded_model_KNN.predict([board.flatten()])
	predict_DTC = loaded_model_DTC.predict([board.flatten()])
	predict_MLP = loaded_model_MLP.predict([board.flatten()])

	# 0 x ganhou, 1 o ganhou, 2 tem jogo, 3 empate
	print("result KNN: ", predict_KNN)
	print("result DTC: ", predict_DTC)
	print("result MLP: ", predict_MLP)

	winner = mode([predict_MLP[0], predict_KNN[0], predict_DTC[0]])

	print("winner: ", winner)

	#0 x ganhou, 1 o ganhou, 2 tem jogo, 3 empate

	# 0 = x , 1 = o , -1 = b

	draw_status()


def drawXO(row, col):
	global board, XO

	# for the first row, the image
	# should be pasted at a x coordinate
	# of 30 from the left margin
	if row == 1:
		posx = 30

	# for the second row, the image
	# should be pasted at a x coordinate
	# of 30 from the game line
	if row == 2:

		# margin or width / 3 + 30 from
		# the left margin of the window
		posx = width / 3 + 30

	if row == 3:
		posx = width / 3 * 2 + 30

	if col == 1:
		posy = 30

	if col == 2:
		posy = height / 3 + 30

	if col == 3:
		posy = height / 3 * 2 + 30

	# setting up the required board
	# value to display
	board[row-1][col-1] = XO

	#if(XO == 'x'):
	if(XO == 0):

		# pasting x_img over the screen
		# at a coordinate position of
		# (pos_y, posx) defined in the
		# above code
		screen.blit(x_img, (posy, posx))
		#XO = 'o'
		XO = 1
	else:
		screen.blit(o_img, (posy, posx))
		#XO = 'x'
		XO = 0
	pg.display.update()


def user_click():
	# get coordinates of mouse click
	x, y = pg.mouse.get_pos()

	print("x: ", x, "y: ", y)

	# get column of mouse click (1-3)
	if(x < width / 3):
		col = 1

	elif (x < width / 3 * 2):
		col = 2

	elif(x < width):
		col = 3

	else:
		col = False

	# get row of mouse click (1-3)
	if(y < height / 3):
		row = 1

	elif (y < height / 3 * 2):
		row = 2

	elif(y < height):
		row = 3

	else:
		row = False

	print("row and col: ", (row and col and board[row-1][col-1] == 2))

	# after getting the row and col,
	# we need to draw the images at
	# the desired positions
	if(row and col and board[row-1][col-1] == -1):
		global XO
		drawXO(row, col)
		check_win()

def reset_game():
	global board, winner, XO, draw
	#screen.blit(x_img, (posy, posx))
	screen.blit(restart_img, (0,0))
	# setting a font object
	font = pg.font.Font(None, 50)

	# setting the font properties like
	# color and width of the text
	text = font.render("", 1, (255, 255, 255))	

	# copy the rendered message onto the board
	# creating a small block at the bottom of the main display
	screen.fill((0, 0, 0), (0, 400, 500, 100))
	text_rect = text.get_rect(center=(width / 2, 500-50))
	screen.blit(text, text_rect)
	
	pg.display.update()
	time.sleep(3)
	#XO = 'x'
	XO = 0
	draw = False

	winner = 2
	board = np.array([[-1]*3, [-1]*3, [-1]*3])
	game_initiating_window()


game_initiating_window()

while(True):
	for event in pg.event.get():
		if event.type == pg.QUIT:
			print("caraio1")
			pg.quit()
			sys.exit()
		if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
			user_click()
			if(winner != 2):
				print("penis")
				time.sleep(1)
				reset_game()
	pg.display.update()
	CLOCK.tick(fps)