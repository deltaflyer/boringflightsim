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
    self.angle_old = 0

    self.knots = 0
    self.feet = 0

  def increase_speed(self):
    if self.knots < 485: # 485 Knots = 900 km/h
      self.knots = self.knots + 10

  def decrease_speed(self):
    if self.knots > 0:
      self.knots = self.knots - 10

  def get_speed(self):
    return self.knots

  def pull_up(self):
    if self.feet > 0:
      self.feet = self.feet - 10

  def push_down(self):
    if self.feet < 45000:
      self.feet = self.feet + 10

  def get_feet(self):
    return self.feet

  def update(self):
    # Only rotate if necessary
    if self.angle != self.angle_old:
      self.plane_img = pygame.transform.rotate(self.plane_img, self.angle)
    self.plane_rect.centerx = self.x
    self.plane_rect.centery = self.y
    self.screen.blit(self.plane_img, self.plane_rect)