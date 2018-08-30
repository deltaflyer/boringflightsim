import os
import pygame
import sys

from cloudgenerator import Cloudgenerator
from debug import Debug
from displays.heightindicator import Heightindicator
from displays.thrustindicator import Thrustindicator
from displays.speedindicator import Speedindicator
from displays.multidisplay import Multidisplay
from displays.navigation import Navigation
from plane import Plane
from scenery import Scenery
from groundobjects import GroundObjects
from collision_detection import CollisionDetection


class Flightsim():
    def __init__(self):
        self.is_game_running = True
        self.fps = 30
        self.clock = pygame.time.Clock()
        self.screen = self.__init_display()
        self.scenery = Scenery(self.screen)
        self.groundobjects = GroundObjects(self.screen)
        self.plane = Plane(self.screen, self.scenery)
        self.scenery.register_plane(self.plane)
        self.groundobjects.register_plane(self.plane)
        self.collision_detection = CollisionDetection(self.screen, self)
        self.collision_detection.register_plane(self.plane)
        self.collision_detection.register_groundobjects(self.groundobjects.get_groundobjects())
        self.cloudgenerator = Cloudgenerator(self.screen)
        self.cloudgenerator.register_plane(self.plane)
        self.speedindicator = Speedindicator(self.screen)
        self.heightindicator = Heightindicator(self.screen)
        self.thrustindicator = Thrustindicator(self.screen)
        self.multidisplay = Multidisplay(self.screen, self.plane)
        self.navigationdisplay = Navigation(self.screen)

        self.debug = Debug(self.screen, self.plane, self.cloudgenerator)

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
            self.scenery.update()

            # Draw the groundobjects
            self.groundobjects.update()

            # Update the cloud-generator
            self.cloudgenerator.update()

            # Draw the speed indicator
            self.speedindicator.update(self.plane.get_speed())

            # Draw the height indicator
            self.heightindicator.update(self.plane.get_feet())

            # Draw the thrust indicator
            self.thrustindicator.update(self.plane.get_thrust())

            # Draw the flight multidisplay
            self.multidisplay.update()

            # Draw the navigation display
            self.navigationdisplay.update(self.plane.get_travelled_x_distance())

            # Draw self.debug infos
            self.debug.update()

            # Draw the self.plane
            self.plane.update()

            # Check is a collision occured
            self.collision_detection.update()

            # Do the final draw operation
            pygame.display.flip()

            # Handle events
            self.__handle_events(pygame.event.get())

    def stop_simulation(self):
        self.is_game_running = False

    def __handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif (event.type == pygame.KEYDOWN) and self.is_game_running:
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
                if event.key == pygame.K_g:
                    # Toggle gear
                    self.plane.toggle_landing_gear()
                if event.key == pygame.K_a:
                    # Toggle Airbreak
                    self.plane.toggle_airbrake()

                # self.debug code
                if event.key == pygame.K_t:
                    # pull up
                    self.plane.set_speed(200)


if __name__ == "__main__":
    flightsim = Flightsim()
    flightsim.run_game()
