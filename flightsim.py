import singleton
import pygame
import sys
import os
from plane import Plane
from scenery import Scenery
from speedindicator import Speedindicator
from heightindicator import Heightindicator

screen = ''
clock = pygame.time.Clock()
fps = 30
plane = ''
scenery = ''
speedindicator = ''
heightindicator = ''

def main():
	global screen, plane, scenery, speedindicator, heightindicator
	screen = init_display()
	plane = Plane(screen)
	scenery = Scenery(screen, 0, 0)
	speedindicator = Speedindicator(screen)
	heightindicator = Heightindicator(screen)
	run_game()

def init_display():
	pygame.init()
	display_info = pygame.display.Info()
	screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
	screen.fill([0, 0, 0])
	icon = pygame.image.load(os.path.join('graphics', 'icon.png'))
	icon = pygame.transform.scale(icon, (32, 32))
	pygame.display.set_icon(icon)
	pygame.display.set_caption('Boring Flightsim')
	return screen

def run_game():
	global screen, plane, clock, fps, speedindicator, heightindicator
	while True:
		clock.tick(30)
		fps = clock.get_fps()
		if fps < 1:
			fps = 30

		# Draw the scenery
		screen.fill([0, 0, 0])
		scenery.update(0,0)

		# Draw the speed indicator
		speedindicator.update(plane.get_speed())

		# Draw the height indicator
		heightindicator.update(plane.get_feet())

		# Draw the plane
		plane.update()
		pygame.display.flip()

		# Handle events
		handle_events(pygame.event.get())


def handle_events(events):
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				# more thrust
				plane.increase_speed()
			if event.key == pygame.K_s:
				# less thrust
				plane.decrease_speed()
			if event.key == pygame.K_UP:
				# pull up
				plane.pull_up()
			if event.key == pygame.K_DOWN:
				# pull up
				plane.push_down()


if __name__ == "__main__":
	main()