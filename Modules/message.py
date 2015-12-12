import pygame
import time
import random

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,120,0)

pixel_x=800
pixel_y=700

gameDisplay = pygame.display.set_mode((pixel_x,pixel_y))
## CLASS FOR THE TEXT SENT TO THE SCREEN
class message:
	## VARIOUS FONTS STYLES
	small_font =  pygame.font.SysFont(None,25)
	med_font =  pygame.font.SysFont(None,40)
	large_font =  pygame.font.SysFont(None,60)
	
	def __init__(self):
		pass
	## MAKING TEXT MSG ENTERED TO AN OBJECT
	def text_objects(self,text,color,size="small"):
		if size =="small":
			textSurface = message.small_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="medium":
			textSurface = message.med_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
		elif size =="large":
			textSurface = message.large_font.render(text,True,color)
			return textSurface,textSurface.get_rect()
	## DISPLAYING SCORE	
	def display_score(self,msg):
		screen_text = message.med_font.render(msg,True,black)	
		gameDisplay.blit(screen_text,[0,0])

	## DISPLAYING  THE TEXT OBJECT
	def message_to_screen(self,msg,color,y_displace=0,size="small"):
		textSurf , textRect = self.text_objects(msg,color,size)
		textRect.center = (pixel_x/2),(pixel_y/2)+y_displace
		gameDisplay.blit(textSurf,textRect)	

				
if __name__=="__main__":
	a =message()
	b= game_intro()
	gameDisplay.fill(white)
	a.display_score('msg')	
	a.message_to_screen("Pranav",black,size="large")
	pygame.display.update()	
	print b.intro_l2()
