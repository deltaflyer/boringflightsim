# sprite for the shipclass 
import pygame
import os
class Plane(pygame.sprite.Sprite):
  def __init__(self, x, y):

      pygame.sprite.Sprite.__init__(self)
      self.imageMaster = pygame.image.load(os.path.join('graphics', 'plane_small.png'))
      self.image = self.imageMaster
      self.rect = self.image.get_rect()
      self.position = [x, y]
      self.rect.centerx, self.rect.centery = self.position
      self.angle = 0

  def update(self):
      self.rect.centerx, self.rect.centery = self.position
      oldCenter = self.rect.center
      self.image = pygame.transform.rotate(self.imageMaster, self.angle)
      self.rect = self.image.get_rect()
      self.rect.center = oldCenter