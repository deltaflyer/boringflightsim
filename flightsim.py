import singleton
import pygame
import sys
from plane import Plane

screen = ''
clock = pygame.time.Clock()
fps = 30
plane = Plane([500, 230])

def main():
	global screen
	screen = init_display()
	run_game()

def init_display():
	pygame.init()
	display_info = pygame.display.Info()
	screen = pygame.display.set_mode((display_info.current_w, display_info.current_h))
	screen.fill([0, 0, 0])
	return screen

def run_game():
	global screen, plane, clock, fps
	while True:
		clock.tick(30)
		fps = clock.get_fps()
		if fps < 1:
			fps = 30

		# Draw the ship
		screen.fill([0, 0, 0])
		plane.update()
		screen.blit(plane.image, plane.rect)
		pygame.display.flip()

		# Handle events
		handle_events(pygame.event.get())

def handle_events(events):
	for event in events:
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				pass


if __name__ == "__main__":
	main()