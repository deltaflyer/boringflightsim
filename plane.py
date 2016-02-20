import pygame
import os
class Plane(pygame.sprite.Sprite):

  def __init__(self, screen):
    pygame.sprite.Sprite.__init__(self)

    self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small.png'))
    self.plane_rect = self.plane_img.get_rect()
    self.plane_rect.centerx = 200
    self.plane_rect.centery = 300


    self.screen = screen
    self.angle = 0
    self.angle_old = 0

    self.knots = 0
    self.feet = 0

    self.images_computes = self.__precompute_rotated_plane(self.plane_img, self.plane_rect)

  def __precompute_rotated_plane(self, image, rect):
    images_computes = {}
    for degree in xrange(-180, 180):
      images_computes[degree] = self.__rot_center(image, rect, degree)
    return images_computes

  def __rot_center(self, image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return (rot_image, rot_rect)

  def increase_speed(self):
    if self.knots < 485: # 485 Knots = 900 km/h
      self.knots = self.knots + 10

  def decrease_speed(self):
    if self.knots > 0:
      self.knots = self.knots - 10

  def get_speed(self):
    return self.knots

  def push_down(self):
    if self.feet > 0:
      self.feet = self.feet - 10

  def pull_up(self):
    if self.feet < 45000:
      self.angle_old = self.angle
      self.feet = self.feet + 10
      if self.angle < 160:
        self.angle = self.angle + 20

  def get_feet(self):
    return self.feet

  def update(self):
    if self.angle > 0:
      self.angle_old = self.angle
      self.angle = self.angle -1
    if self.angle is not self.angle_old:
      self.plane_img = self.images_computes[self.angle][0]
      self.plane_rect = self.images_computes[self.angle][1]

    self.screen.blit(self.plane_img, self.plane_rect)
    print self.angle

  def __rotate_center(self, angle):
    self.plane_img = pygame.transform.rotate(self.plane_img, angle)
    self.plane_rect = self.plane_img.get_rect(center = self.plane_rect.center)