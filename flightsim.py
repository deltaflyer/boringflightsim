import pygame
import sys
import os
from plane import Plane
from scenery import Scenery
from cloudgenerator import Cloudgenerator
from speedindicator import Speedindicator
from heightindicator import Heightindicator
from thrustindicator import Thrustindicator
from debug import Debug

class Flightsim():

	def __init__(self):
		self.fps = 30
		self.clock = pygame.time.Clock()
		self.screen = self.__init_display()

		self.scenery = Scenery(self.screen)
		self.plane = Plane(self.screen, self.scenery)
		self.scenery.register_plane(self.plane)
		self.speedindicator = Speedindicator(self.screen)
		self.heightindicator = Heightindicator(self.screen)
		self.thrustindicator = Thrustindicator(self.screen)

		self.debug = Debug(self.screen, self.plane)

	def __init_display(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1280, 745))
		self.screen.fill([0, 0, 0])
		icon = pygame.image.load(os.path.join('graphics', 'icon.png'))
		icon = pygame.transform.scale(icon, (32, 32))
		pygame.display.set_icon(icon)
		pygame.display.set_caption('Boring Flightsim')
		return self.screen

	def run_game(self):
		while True:
			self.clock.tick(30)
			self.fps = self.clock.get_fps()
			if self.fps < 1:
				self.fps = 30

			# Draw the self.scenery
			self.screen.fill([0, 0, 0])
			self.scenery.update()

			# Draw the speed indicator
			self.speedindicator.update(self.plane.get_speed())

			# Draw the height indicator
			self.heightindicator.update(self.plane.get_feet())

			# Draw the thrust indicator
			self.thrustindicator.update(self.plane.get_thrust())

			# Draw self.debug infos
			self.debug.update()

			# Draw the self.plane
			self.plane.update()
			pygame.display.flip()

			# Handle events
			self.__handle_events(pygame.event.get())


	def __handle_events(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_w:
					# more thrust
					self.plane.increase_speed()
				if event.key == pygame.K_s:
					# less thrust
					self.plane.decrease_speed()
				if event.key == pygame.K_UP:
					# pull up
					self.plane.pull_up()
				if event.key == pygame.K_DOWN:
					# pull up
					self.plane.push_down()

				# self.debug code
				if event.key == pygame.K_t:
					# pull up
					self.plane.set_speed(200)



if __name__ == "__main__":
	flightsim = Flightsim()
	flightsim.run_game()