# sprite for the shipclass 
import pygame
import os
class Plane(pygame.sprite.Sprite):

  def __init__(self, screen, x, y):
    pygame.sprite.Sprite.__init__(self)

    self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small.png'))
    self.plane_rect = self.plane_img.get_rect()

    self.screen = screen
    self.x = x
    self.y = y
    self.angle = 0

  def update(self, x, y, angle):
    # Only rotate if necessary
    if self.angle != angle:
        self.plane_img = pygame.transform.rotate(self.plane_img, angle)
    self.x = x
    self.y = y
    self.angle = angle
    self.plane_rect.centerx = self.x
    self.plane_rect.centery = self.y
    self.screen.blit(self.plane_img, self.plane_rect)