# sprite for scenery
import pygame
import os

class Scenery(pygame.sprite.Sprite):
	def __init__(self, screen, x, y):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.x = x
		self.y = y

	def update(self, x, y):
		self.x = x
		self.y = y
		self.__print_sky()
		if self.y <  64:
			self.__print_grass()

	def get_terrain_heigh_in_pixel(self):
		return 64

	def __print_grass(self):
		x = 0
		gras = self.__get_gras()
		for i in range(1, 25):
			gras[1].centerx = x
			self.screen.blit(gras[0], gras[1])
			x = x + 64

	def __get_gras(self):
		gras_img = pygame.image.load(os.path.join('graphics', 'gras.png')).convert()
		gras_rect = gras_img.get_rect()
		gras_rect.centery = 730
		return (gras_img, gras_rect)

	def __print_sky(self):
		self.screen.fill((0, 0, 255))