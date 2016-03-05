# sprite for scenery
import pygame
import os
import random

class Cloudgenerator():
	def __init__(self, screen):
		self.screen = screen
		self.plane = ''
		self.clouds = []
		self.cloud_cover_threshold = random.randint(1500,3000)


	def register_plane(self, plane):
		self.plane = plane

	def update(self):
		self.clouds = self.__add_cloud(self.clouds)
		self.clouds = self.__add_clouds(self.clouds)
		self.clouds = self.__remove_invisible_clouds(self.clouds)

	def __add_cloud(self, cloud_array):
		# Above the threshold there are no clouds
		if self.plane.get_feet() > self.cloud_cover_threshold:
			return cloud_array
		
		# add a cloud every 1000. frame
		if 0 == random.randint(0,1000):
			y = random.randint(200, 900)
			cloud = Cloud(self.screen, 2000, y)
			cloud.register_plane(self.plane)
			cloud_array.append(cloud)

	def __update_clouds(self, cloud_array):
		for cloud in cloud_array:
			cloud.update()
		return cloud_array

	def __remove_invisible_clouds(self, cloud_array):
		# Above the threshold there are no clouds
		if self.plane.get_feet() > self.cloud_cover_threshol:
			return cloud_array

		# Remove clouds which are not visible anymore
		new_clouds = []
		for cloud in cloud_array:
			if cloud.get_x() < 0:
				continue
			else:
				new_clouds.append(cloud)
		return new_clouds


	class Cloud(pygame.sprite.Sprite):
		def __init__(self, screen, start_x, start_y):
			file_name = str(random.randint(1,3)) + '.png'
			self.cloud_img = pygame.image.load(os.path.join('graphics', file_name))
			self.cloud_rect = self.cloud_img.get_rect()
			self.cloud_rect.centerx = start_x
			self.cloud_rect.centery = start_y
			pygame.sprite.Sprite.__init__(self)
			self.screen = screen
			self.plane = ''

		def register_plane(self, plane):
			self.plane = plane

		def update(self,):
			self.cloud_img.cloud_rect_x = self.cloud_img.cloud_rect_x - 5
			self.screen.blit(self.cloud_img, self.cloud_rect)

	