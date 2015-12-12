import pygame
import time
import random

from Brick import *
from Player import *
from Level import *
from message import *

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

background = pygame.image.load("Assets/bck.png")

screenWidth = 800
screenHeight = 600
fps = 60

gameDisplay = pygame.display.set_mode((screenWidth,screenHeight))

levelobj = Level(0)
brickList = []
level = levelobj.level_design()

for y in range(len(level)):
	for x in range(len(level[y])):
		if (level[y][x] == 1):
			brickList.append(Brick(x*32,y*32,(205,155,100)))
			
for brick in brickList:
	brick.render(gameDisplay)

def game_intr():
	game = message()
	intro = True 
	while intro:
			gameDisplay.fill(white)
			game.message_to_screen("Welcome to Makeway",green,-60,"large")
			game.message_to_screen("Press c to continue.",black,-10)
			game.message_to_screen("Press q to Quit",green,10,)
			pygame.display.update()
			clock.tick(15)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return 0
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						return 0
						
					elif event.key == pygame.K_c:
						intro=False
						gamem()		

def gamem():
	lead_x_change = 0
	lead_y_change = 0
	block_size = 32
	gameOver = False
	gameExit = False
	while not gameExit:
		## OUTER LOOP FOR GAME  	
		while gameOver == True :
			## INNER LOOP FOR GAME OVER
			gameDisplay.fill(white)
			game.message_to_screen("Game over",red,y_displace=-50,size="large")
			game.message_to_screen(" Press C to play again or Q to quit ",black,y_displace = 50,size="medium")
			pygame.display.update()	
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver =False
					gameExit = True
					
				elif event.type== pygame.KEYDOWN :
					if event.key == pygame.K_q:
						gameOver =False
						gameExit = True
					elif event.key == pygame.K_c:
						gameOver =False
						gameExit = True
						game_intr()	
			
		## READING OF THE USER INPUT THROUGH KEYBOARD

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					gameOver = True		
				elif event.key == pygame.K_LEFT: 	
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:	
					lead_x_change = block_size
					lead_y_change = 0
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					lead_x_change = 0
					lead_y_change = 0
					
		gameDisplay.fill(white)
		gameDisplay.blit(background, (0,0))	
		for brick in brickList:
			brick.x -= lead_x_change
			brick.render(gameDisplay)	
		pygame.display.update()			
		clock.tick(fps)

game_intr()
pygame.quit()
quit()					
