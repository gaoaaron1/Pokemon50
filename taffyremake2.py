import random
import stddraw
import math 
import color 
import picture
import pygame
import time

pygame.init()
pikachuClick = pygame.mixer.Sound("newPikachu.wav")
charmanderClick = pygame.mixer.Sound("NewCharmander.wav")
bulbasaurClick = pygame.mixer.Sound("newBulbasaur2.wav")
squirtleClick = pygame.mixer.Sound("newSquirtle.wav")
magikarpClick = pygame.mixer.Sound("magikarp_new.wav")

gameMusic = pygame.mixer.music.load("violetcity_newtheme2.wav")
pygame.mixer.music.play(-1) 

#colors 
darkred = color.Color(153, 0, 0)
darkpurple = color.Color(0, 0, 26)
lightblue = color.Color(204, 255, 255)

Game = True
gameSpeed = 0.02
gameScore = 0
gameTries = 25
returnSwap = False
scoreBoard = 0

a = random.randrange(0,7)


arrayNew =  [[0 for i in range(7)] for j in range(9)]

for i in range(9):
	for j in range(7):
		arrayNew[i][j] = random.randrange(1,7)
		temp = arrayNew[i][j]
		if (i >= 0 and i < 9):
			if (j >= 0 and j < 7):

				if arrayNew[i][j] == arrayNew[i-1][j]:
					if arrayNew[i][j] == arrayNew[i-2][j]:
						arrayNew[i][j] = random.randrange(1,7)
						while arrayNew[i][j] == temp:
							arrayNew[i][j] = random.randrange(1,7)


				if arrayNew[i][j] == arrayNew[i][j-1]:
					if arrayNew[i][j] == arrayNew[i][j-2]:
						temp2 = arrayNew[i][j]
						arrayNew[i][j] = random.randrange(1,7)
						while arrayNew[i][j] == temp or arrayNew[i][j] == temp2:
							arrayNew[i][j] = random.randrange(1,7)



#X and Y to draw the layout.
x = len(arrayNew[0]) #x = 7
y = len(arrayNew) #y = 9


#Mouse clicks.
mx = 0
my = 0

class pictures():
	def picture_pikachu(x, y):
		stddraw.picture(picture.Picture('Pikachu_Sprite3.png'), x, y)
	def picture_squirtle(x, y):
		stddraw.picture(picture.Picture('Squirtle_Sprite2.png'), x, y)
	def picture_bulbasaur(x, y):
		stddraw.picture(picture.Picture('Bulbasaur_Sprite2.png'), x, y)
	def picture_charmander(x, y):
		stddraw.picture(picture.Picture('Charmander_Sprite2.png'), x, y)
	def picture_snorlax(x, y):
		stddraw.picture(picture.Picture('Snorlax_Sprite2.png'), x, y)
	def picture_magikarp(x, y):
		stddraw.picture(picture.Picture('Magikarp_Sprite2.png'), x, y)
	def background_cave(x, y):
		stddraw.picture(picture.Picture('caveinterior.png'), x, y)
	def background_wallpaper(x, y):
		stddraw.picture(picture.Picture('wallpaperpokemon.png'), x, y)
	def pokelogo(x, y):
		stddraw.picture(picture.Picture('pokelogo.png'), x, y)
	def fivelogo(x, y):
		stddraw.picture(picture.Picture('5logo.png'), x, y)
	def pokeball(x, y):
		stddraw.picture(picture.Picture('pokeball.png'), x, y)

myPictures = pictures()

def print_border():
	print('')
	for i in arrayNew[::-1]:
		print(i)

def drawScreen():
	stddraw.setCanvasSize(575, 575)
	stddraw.setXscale(-1, x+1)
	stddraw.setYscale(-1, y+4)

def drop_border():
	#row 1
    for j in range(0,8):
    	for k in range(0,7):
	        if arrayNew[j][k] == 0:
	            for i in range(j,8):
	                arrayNew[i][k] = arrayNew[i+1][k]
	                arrayNew[8][k] = random.randrange(1,7)
	        if arrayNew[8][k] == 0:
	            arrayNew[8][k] = random.randrange(1,7)

			print_border()
			check_border()
			check_border2()
			print_border()
			drawScreen()
			drawButtons()
	        stddraw.show(0.02 * 15000)




def drawButtons():
	global gameScore
	global turn
	grid = [[0 for i in range(x+1)] for j in range(y)]

	pictures.background_wallpaper(3.5, 6.05)
	stddraw.setPenColor(darkpurple)
	stddraw.filledRectangle(-0.05, -0.55, 7.1, 10.1)
	stddraw.setPenColor(stddraw.WHITE)
	stddraw.filledRectangle(0, -0.5, 7, 10)
	pictures.pokelogo(3.5, 11)
	pictures.fivelogo(5.7, 11.25)
	pictures.pokeball(6.7, 11.25)

	for i in range(x): #draws squares
   		for j in range(y):
   			if arrayNew[j][i] == 0:
   				stddraw.setPenColor(stddraw.WHITE)
   				stddraw.filledRectangle(i, j, 0.5, 0.5)
   				#pictures.background_cave(i+0.5,j+0.48)

   			if arrayNew[j][i] == 1:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_magikarp(i+0.5, j+0.5)

   			if arrayNew[j][i] == 2:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_bulbasaur(i+0.5, j+0.5)

   			if arrayNew[j][i] == 3:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_pikachu(i+0.5, j+0.5)

   			if arrayNew[j][i] == 4:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_snorlax(i+0.5, j+0.5)

   			if arrayNew[j][i] == 5:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_charmander(i+0.5, j+0.5)

   			if arrayNew[j][i] == 6:
   				#pictures.background_cave(i+0.5,j+0.48)
   				pictures.picture_squirtle(i+0.5, j+0.5)

	if turn == 1:
		stddraw.setPenRadius(0.003)
		stddraw.setPenColor(stddraw.ORANGE)
		stddraw.rectangle(mx+0.1, my, 0.75, 1)		

	stddraw.setPenColor(stddraw.BLACK)
	stddraw.setFontSize(25)	
	stddraw.text(0.5,10,'Score:' + str(gameScore))	
	stddraw.text(6.25,10,'Turns:' + str(gameTries))	

	'''
   	#vertical lines
	for i in range(x + 1): #draws lines
		stddraw.setPenColor(stddraw.BLACK)
		stddraw.line(i, 0, i, y)

    #horizontal lines
	for i in range(y + 1): #draws lines
		stddraw.setPenColor(stddraw.BLACK)
		stddraw.line(0, i, x, i)
	'''
def gameVictory():
	stddraw.setPenColor(stddraw.BLACK)
	stddraw.setFontSize(25)	
	stddraw.text(3.5,12.5,'Congratulations, you have reached a score 50 and above!')	

def gameFailure():
	stddraw.setPenColor(stddraw.BLACK)
	stddraw.setFontSize(25)	
	stddraw.text(3.5,12.5,'Sorry, you did not reach a score of at least 50.')	


turn = 0

def clickButtons(arraySwap0, arraySwap1):
	global turn
	global mx
	global my

	if stddraw.mousePressed():
		mx = math.floor(stddraw.mouseX())
		my = math.floor(stddraw.mouseY())

		for i in range(0,x):
			for j in range(0,y):
				if (mx == i and my == j):

				# if turn == 0:
				# 	turn = 1
				# elif turn == 1:
				# 	turn = 0

					if stddraw.hasNextKeyTyped():
							Game = False

					stddraw.clear()

					if (turn == 0):
						print("One")
						# arraySwap0.append([mx, my])
						arraySwap0.append(mx)
						arraySwap0.append(my)
						print("Array ID", arraySwap0)
						if arrayNew[arraySwap0[1]][arraySwap0[0]] == 3:
							pygame.mixer.Sound.play(pikachuClick)
						elif arrayNew[arraySwap0[1]][arraySwap0[0]] == 5:
							pygame.mixer.Sound.play(charmanderClick)
						elif arrayNew[arraySwap0[1]][arraySwap0[0]] == 2:
							pygame.mixer.Sound.play(bulbasaurClick)
						elif arrayNew[arraySwap0[1]][arraySwap0[0]] == 6:
							pygame.mixer.Sound.play(squirtleClick)
						elif arrayNew[arraySwap0[1]][arraySwap0[0]] == 1:
							pygame.mixer.Sound.play(magikarpClick)


						stddraw.setPenRadius(0.005)
						stddraw.setPenColor(stddraw.ORANGE)
						stddraw.rectangle(mx+0.05, my, 0.9, 0.9)
						turn += 1

					elif (turn == 1):
						print("Two")
						# arraySwap1.append([mx, my])
						arraySwap1.append(mx)
						arraySwap1.append(my)
						print("Array ID", arraySwap1)
						if arrayNew[arraySwap1[1]][arraySwap1[0]] == 3:
							pygame.mixer.Sound.play(pikachuClick)
						elif arrayNew[arraySwap1[1]][arraySwap1[0]] == 5:
							pygame.mixer.Sound.play(charmanderClick)
						elif arrayNew[arraySwap1[1]][arraySwap1[0]] == 2:
							pygame.mixer.Sound.play(bulbasaurClick)
						elif arrayNew[arraySwap1[1]][arraySwap1[0]] == 6:
							pygame.mixer.Sound.play(squirtleClick)
						elif arrayNew[arraySwap1[1]][arraySwap1[0]] == 1:
							pygame.mixer.Sound.play(magikarpClick)
						'''
						stddraw.setPenRadius(0.01)
						stddraw.setPenColor(stddraw.RED)
						stddraw.rectangle(mx-0.02, my-0.02, 0.55, 0.55)
						'''
						turn += 1
			


def swapButtons(arraySwap0, arraySwap1):
	global gameTries
	print('')
	print("click 1:", arraySwap0[0],arraySwap0[1])
	print("click 2:", arraySwap1[0],arraySwap1[1])

	if arraySwap0[0] == arraySwap1[0] and arraySwap0[1] == arraySwap1[1]+1:
		temporaryArray = arrayNew.copy()
		if (arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] != temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]):

			arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] = temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]


	if arraySwap0[0] == arraySwap1[0] and arraySwap0[1] == arraySwap1[1]-1:
		temporaryArray = arrayNew.copy()
		if (arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] != temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]):

			arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] = temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]

	if arraySwap0[0] == arraySwap1[0]+1 and arraySwap0[1] == arraySwap1[1]:
		temporaryArray = arrayNew.copy()
		if (arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] != temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]):

			arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] = temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]

	if arraySwap0[0] == arraySwap1[0]-1 and arraySwap0[1] == arraySwap1[1]:
		temporaryArray = arrayNew.copy()
		if (arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] != temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]):

			arrayNew[arraySwap0[1]][arraySwap0[0]],arrayNew[arraySwap1[1]][arraySwap1[0]] = temporaryArray[arraySwap1[1]][arraySwap1[0]],temporaryArray[arraySwap0[1]][arraySwap0[0]]


arraySwap0 = []
arraySwap1 = []


def playScreen():
	global gameTries
	global gameScore
	global turn
	global arraySwap0
	global arraySwap1
	global arrayNew
	global returnSwap
	global scoreBoard
	while gameTries > 0:

		#Array swaps.
		clickButtons(arraySwap0, arraySwap1)
		if turn == 2:
			turn = 0
			swapButtons(arraySwap0, arraySwap1)
			check_border()
			check_border2()
			drawButtons()
			if scoreBoard != gameScore:
				scoreBoard = gameScore 
				returnSwap = False
			if returnSwap == True:
				stddraw.show(1)
				time.sleep(1)
				swapButtons(arraySwap0, arraySwap1)
				returnSwap = False
			elif returnSwap == False:
				gameTries -= 1

			arraySwap0 = []
			arraySwap1 = []
		check_border()
		check_border2()
		drawButtons()
		stddraw.show(0.02 * 17500)
	else:
		if gameScore >= 50:
			gameVictory()
			gameScore = 0
			gameTries = 25
		elif gameTries < 50:
			gameFailure()
			gameScore = 0
			gameTries = 25

		stddraw.show(1)
		time.sleep(4)

		arrayNew =  [[0 for i in range(7)] for j in range(9)]

		for i in range(9):
			for j in range(7):
				arrayNew[i][j] = random.randrange(1,7)
				temp = arrayNew[i][j]
				if (i >= 0 and i < 9):
					if (j >= 0 and j < 7):

						if arrayNew[i][j] == arrayNew[i-1][j]:
							if arrayNew[i][j] == arrayNew[i-2][j]:
								arrayNew[i][j] = random.randrange(1,7)
								while arrayNew[i][j] == temp:
									arrayNew[i][j] = random.randrange(1,7)


						if arrayNew[i][j] == arrayNew[i][j-1]:
							if arrayNew[i][j] == arrayNew[i][j-2]:
								temp2 = arrayNew[i][j]
								arrayNew[i][j] = random.randrange(1,7)
								while arrayNew[i][j] == temp or arrayNew[i][j] == temp2:
									arrayNew[i][j] = random.randrange(1,7)
		playScreen()


#horizontal
def check_border():
	global gameScore 
	global returnSwap
	for i in range(0,9):

		if arrayNew[i][0] == arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5] == arrayNew[i][6]:
			gameScore += 5
			returnSwap = False
			for k in range(0,7):
				arrayNew[i][k] = 0

		elif arrayNew[i][0] == arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5]:
			gameScore += 4
			returnSwap = False
			for k in range(0,6):
				arrayNew[i][k] = 0

		elif arrayNew[i][0] == arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4]:
			gameScore += 3
			returnSwap = False
			for k in range(0,5):
				arrayNew[i][k] = 0

		elif arrayNew[i][0] == arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3]:
			gameScore += 2
			returnSwap = False
			for k in range(0,4):
				arrayNew[i][k] = 0

		elif arrayNew[i][0] == arrayNew[i][1] == arrayNew[i][2]:
			gameScore += 1
			returnSwap = False
			for k in range(0,3):
				arrayNew[i][k] = 0

		#Next phase.

		if arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5] == arrayNew[i][6]:
			gameScore += 4
			returnSwap = False
			for k in range(1,7):
				arrayNew[i][k] = 0

		elif arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5]:
			gameScore += 3
			returnSwap = False
			for k in range(1,6):
				arrayNew[i][k] = 0


		elif arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4]:
			gameScore += 2
			returnSwap = False
			for k in range(1,5):
				arrayNew[i][k] = 0

		elif arrayNew[i][1] == arrayNew[i][2] == arrayNew[i][3]:
			gameScore += 1
			returnSwap = False			
			for k in range(1,4):
				arrayNew[i][k] = 0


		#Next phase.		

		if arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5] == arrayNew[i][6]:
			gameScore += 3
			returnSwap = False
			for k in range(2,7):
				arrayNew[i][k] = 0


		elif arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5]:
			gameScore += 2
			returnSwap = False
			for k in range(2,6):
				arrayNew[i][k] = 0

		elif arrayNew[i][2] == arrayNew[i][3] == arrayNew[i][4]:
			gameScore += 1
			returnSwap = False
			for k in range(2,5):
				arrayNew[i][k] = 0

		if arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5] == arrayNew[i][6]:
			gameScore += 2
			returnSwap = False
			for k in range(3,7):
				arrayNew[i][k] = 0


		elif arrayNew[i][3] == arrayNew[i][4] == arrayNew[i][5]:
			gameScore += 1
			returnSwap = False
			for k in range(3,6):
				arrayNew[i][k] = 0

		if arrayNew[i][4] == arrayNew[i][5] == arrayNew[i][6]:
			gameScore += 1
			returnSwap = False
			for k in range(4,7):
				arrayNew[i][k] = 0

		else:
			returnSwap = True

	drop_border()

#vertical
def check_border2():
	global gameScore
	global returnSwap
	for i in range(0,7):
		if arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 7
			returnSwap = False
			for k in range(0,9):
				arrayNew[k][i] = 0

		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 6
			returnSwap = False
			for k in range(0,8):
				arrayNew[k][i] = 0


		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i]:
			gameScore += 5
			returnSwap = False
			for k in range(0,7):
				arrayNew[k][i] = 0


		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i]:
			gameScore += 4
			returnSwap = False
			for k in range(0,6):
				arrayNew[k][i] = 0


		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i]:
			gameScore += 3
			returnSwap = False
			for k in range(0,5):
				arrayNew[k][i] = 0


		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i]:
			gameScore += 2
			returnSwap = False
			for k in range(0,4):
				arrayNew[k][i] = 0


		elif arrayNew[0][i] == arrayNew[1][i] == arrayNew[2][i]:
			gameScore += 1
			returnSwap = False
			for k in range(0,3):
				arrayNew[k][i] = 0

		#Next phase.

		if arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 6
			returnSwap = False
			for k in range(1,9):
				arrayNew[k][i] = 0


		elif arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 5
			returnSwap = False
			for k in range(1,8):
				arrayNew[k][i] = 0			


		elif arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i]:
			gameScore += 4
			returnSwap = False
			for k in range(1,7):
				arrayNew[k][i] = 0		


		elif arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i]:
			gameScore += 3
			returnSwap = False
			for k in range(1,6):
				arrayNew[k][i] = 0



		elif arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i]:
			gameScore += 2
			returnSwap = False
			for k in range(1,5):
				arrayNew[k][i] = 0


		elif arrayNew[1][i] == arrayNew[2][i] == arrayNew[3][i]:
			gameScore += 1
			returnSwap = False
			for k in range(1,4):
				arrayNew[k][i] = 0

		#Next phase.

		if arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 5
			returnSwap = False
			for k in range(2,9):
				arrayNew[k][i] = 0	


		elif arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 4
			returnSwap = False
			for k in range(2,8):
				arrayNew[k][i] = 0	


		elif arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i]:
			gameScore += 3
			returnSwap = False
			for k in range(2,7):
				arrayNew[k][i] = 0	


		elif arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i]:
			gameScore += 2
			returnSwap = False
			for k in range(2,6):
				arrayNew[k][i] = 0		

		elif arrayNew[2][i] == arrayNew[3][i] == arrayNew[4][i]:
			gameScore += 1
			returnSwap = False
			for k in range(2,5):
				arrayNew[k][i] = 0

		
		#Next phase.		

		if arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 4
			returnSwap = False
			for k in range(3,9):
				arrayNew[k][i] = 0


		elif arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 3
			returnSwap = False
			for k in range(3,8):
				arrayNew[k][i] = 0


		elif arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i]:
			gameScore += 2
			returnSwap = False
			for k in range(3,7):
				arrayNew[k][i] = 0


		elif arrayNew[3][i] == arrayNew[4][i] == arrayNew[5][i]:
			gameScore += 1
			returnSwap = False
			for k in range(3,6):
				arrayNew[k][i] = 0

		#Next phase.		

		if arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 3
			returnSwap = False
			for k in range(4,9):
				arrayNew[k][i] = 0


		elif arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 2
			returnSwap = False
			for k in range(4,8):
				arrayNew[k][i] = 0


		elif arrayNew[4][i] == arrayNew[5][i] == arrayNew[6][i]:
			gameScore += 1
			returnSwap = False
			for k in range(4,7):
				arrayNew[k][i] = 0

		#Next phase.

		if arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 2
			returnSwap = False
			for k in range(5,9):
				arrayNew[k][i] = 0


		elif arrayNew[5][i] == arrayNew[6][i] == arrayNew[7][i]:
			gameScore += 1
			returnSwap = False
			for k in range(5,8):
				arrayNew[k][i] = 0


		if arrayNew[6][i] == arrayNew[7][i] == arrayNew[8][i]:
			gameScore += 1
			returnSwap = False
			for k in range(6,9):
				arrayNew[k][i] = 0

		else:
			returnSwap = True
	drop_border()


#functions
print_border()
check_border()
check_border2()
print_border()
drawScreen()
drawButtons()
playScreen()






