# sprite for scenery
import pygame
import os

class Scenery(pygame.sprite.Sprite):
	def __init__(self, screen):
		pygame.sprite.Sprite.__init__(self)

		self.screen = screen
		self.plane = ''

	def register_plane(self, plane):
		self.plane = plane

	def update(self,):
		self.__print_sky()
		self.__print_grass()

	def get_terrain_heigh_in_pixel(self):
		return 64

	def __print_grass(self):
		# if the plane is too high, then print no gras
		if self.plane.get_y_coords() < 400:
			return

		x = 0
		correction_y = 0
		gras = self.__get_gras()

		# Calculate the correction factor for y based on plane height
		if (self.plane.get_y_coords()) < 450:
			correction_y = self.plane.get_y_coords() - 450

		# Print gras
		gras[1].centery = 730 - correction_y
		for i in range(1, 25):
			gras[1].centerx = x
			self.screen.blit(gras[0], gras[1])
			x = x + 64

	def __get_gras(self):
		gras_img = pygame.image.load(os.path.join('graphics', 'gras.png')).convert()
		gras_rect = gras_img.get_rect()
		return (gras_img, gras_rect)

	def __print_sky(self):
		self.screen.fill((182, 211, 225))