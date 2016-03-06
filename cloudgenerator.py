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
		self.clouds = self.__update_clouds(self.clouds)
		self.clouds = self.__remove_invisible_clouds(self.clouds)

	def get_number_of_clouds(self):
		return len(self.clouds)

	def __add_cloud(self, cloud_array):
		# Above the threshold there are no clouds
		#if self.plane.get_feet() < self.cloud_cover_threshold:
		#	return cloud_array
		
		# add a cloud every 1000. frame
		if 0 == random.randint(0,50):
			y = random.randint(100, 550)
			cloud = self.Cloud(self.screen, 2000, y)
			cloud.register_plane(self.plane)
			cloud_array.append(cloud)
		return cloud_array

	def __update_clouds(self, cloud_array):
		for cloud in cloud_array:
			cloud.update()
		return cloud_array

	def __remove_invisible_clouds(self, cloud_array):
		# Above the threshold there are no clouds
		#if self.plane.get_feet() > self.cloud_cover_threshold:
		#return cloud_array

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
			file_name = 'cloud%s.png' % str(random.randint(1,3))
			self.cloud_img = pygame.image.load(os.path.join('graphics', file_name))
			self.cloud_rect = self.cloud_img.get_rect()
			self.cloud_rect.centerx = start_x
			self.cloud_rect.centery = start_y
			pygame.sprite.Sprite.__init__(self)
			self.screen = screen
			self.plane = ''

			self.plane_current_feet = 0
			self.plane_old_feet = 0

		def register_plane(self, plane):
			self.plane = plane

		def update(self):
			# Caclulate X correction factor for plane speed
			x_movement = int( (self.plane.get_speed() / 40) + 0.5 )

			# Calculate Y correction factor for plane climb / sink
			self.plane_old_feet = self.plane_current_feet
			self.plane_current_feet = self.plane.get_feet()
			if self.plane.get_y_coords() == 280:
				if self.plane_current_feet > self.plane_old_feet:
					y_movement = 1
				if self.plane_current_feet < self.plane_old_feet:
					y_movement = -1
				if self.plane_current_feet == self.plane_old_feet:
					y_movement = 0
			else:
				y_movement = 0
			
			self.cloud_rect.centerx = self.cloud_rect.centerx - x_movement
			self.cloud_rect.centery = self.cloud_rect.centery + y_movement
			self.screen.blit(self.cloud_img, self.cloud_rect)

		def get_x(self):
			return self.cloud_rect.centerx

	