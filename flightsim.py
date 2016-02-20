import singleton
import pygame
import sys
import os
from plane import Plane
from scenery import Scenery
from speedindicator import Speedindicator

screen = ''
clock = pygame.time.Clock()
fps = 30
plane = ''
scenery = ''
speedindicator = ''

def main():
	global screen, plane, scenery, speedindicator
	screen = init_display()
	plane = Plane(screen, 200,300)
	scenery = Scenery(screen, 0, 0)
	speedindicator = Speedindicator(screen)
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
	global screen, plane, clock, fps, speedindicator
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
				# less thrus
				plane.decrease_speed()


if __name__ == "__main__":
	main()