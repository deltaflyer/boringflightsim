import pygame
import os
import json
class Navigation(pygame.sprite.Sprite):

  def __init__(self, screen):
    # Initialize Graphic Subsystem
    self.screen = screen
    pygame.sprite.Sprite.__init__(self)
    pygame.font.init()
    font_path = os.path.join('fonts', 'int10h', 'PxPlus_IBM_VGA9.ttf')
    font_size = 14
    self.font_object = pygame.font.Font(font_path, font_size)
    # Read the offset arrivial airport
    dir_path = os.path.dirname(os.path.realpath(__file__))
    ground_object_path = os.path.join(dir_path, '..', 'ground_objects', 'arrival_airport.json')
    with open(ground_object_path, "r") as fp:
      self.ARRIVAL_AIRPORT_DISTANCE = json.load(fp)["x-offset"]

  def update(self, travelled_plane_x_distance):
    distance = self.ARRIVAL_AIRPORT_DISTANCE - travelled_plane_x_distance
    if distance < 0:
      distance = 0
    navidisplay = self.font_object.render("Destination-Aiport: {}m".format(distance), 1,(36,255,0))
    pygame.draw.rect(self.screen, (0, 0, 0), (1015, 60, 220, 14), 0)
    self.screen.blit(navidisplay, (1020, 60))