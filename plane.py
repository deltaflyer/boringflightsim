import pygame
import os
class Plane(pygame.sprite.Sprite):

  def __init__(self, screen):

    # static
    self.TAKEOFFSPEED = 100

    pygame.sprite.Sprite.__init__(self)

    self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small.png'))
    self.plane_rect = self.plane_img.get_rect()
    self.plane_rect.centerx = 400
    self.plane_rect.centery = 660

    self.screen = screen

    self.angle = 0
    self.angle_old = 0
    self.set_angle = 0

    self.thrust = 0
    self.thrust_old = 0
    self.set_thrust = 0

    # 485 Knots = 900 km/h
    self.knots = 0

    self.feet = 0
    self.feet_old = 0

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
    if self.set_thrust < 100:
      self.set_thrust = self.set_thrust + 10

  def decrease_speed(self):
    if self.set_thrust > 0:
      self.set_thrust = self.set_thrust - 10

  def get_speed(self):
    return self.knots

  def push_down(self):
    if self.set_angle > -90 and self.feet > 0:
      self.set_angle= self.set_angle - 5

  def pull_up(self):
    if self.set_angle < 90 and self.knots > self.TAKEOFFSPEED:
      self.set_angle= self.set_angle + 5

  def get_feet(self):
    return self.feet

  def get_thrust(self):
    return self.thrust

  def update(self):
    # Bring real angle to set_angle
    self.__update_angles()

    self.__update_thrust()

    self.__update_knots()

    # Incrementally rotate the plane sprite
    if int(self.angle) is not int(self.angle_old):
      int_angle = int(self.angle + 0.5)
      self.plane_img = self.images_computes[int_angle][0]
      self.plane_rect = self.images_computes[int_angle][1]

    # Incrementally change the height
    if self.feet is not self.feet_old:
      self.feet_old = self.feet
      self.feet = self.feet + self.__calculate_climbrate(self.angle, self.knots)

    self.screen.blit(self.plane_img, self.plane_rect)

  def __update_thrust(self):
    # Incrementally change the thrust
    if self.thrust is self.set_thrust:
      return
    self.thrust_old = self.thrust
    if self.thrust < self.set_thrust:
      self.thrust = self.thrust + 1
    if self.thrust > self.set_thrust:
      self.thrust = self.thrust - 1

  def __update_angles(self):
    if int(self.angle) is not int(self.set_angle):
      self.angle_old = self.angle
      # Climb and reduce speed
      if self.angle < self.set_angle:
        self.angle = self.angle + 0.5
        self.knots = self.knots - 0.5
        if self.knots > 100:
          self.feet = self.feet + 0.5

      # Sink and increse speed
      if self.angle > self.set_angle:
        self.angle = self.angle - 0.5
        self.knots = self.knots + 0.5
        if self.knots > 100:
          self.feet = self.feet - 0.5

  def __calculate_climbrate(self, angle, speed):
    if int(self.angle) is 0 and int(self.set_angle) is 0:
      return 0
    value = 3 # default
    if speed < 100:
      return 0
    if speed < 200:
      value = 1
    if speed < 400:
      value = 2
    if angle < 0:
      return value * -1
    return value

  def __update_knots(self):
    # Bring real knots to set_knots
    self.knots = self.knots + self.__calculate_acceleration(self.angle, self.thrust);

  def __calculate_acceleration(self, angle, thrust):
    # in case of climb decrease acceleration based on angle
    if int(angle) > 0:
      return (angle * - 1) + thrust

    # in case of decent increas acceleration based on angle
    if int(angle) < 0:
      return angle + thrust

    # in horizontal and moving
    if int(angle) == 0 and self.knots > 0:
      if thrust < 10:
        return -3
      else:
        return int((thrust / 2) + 0.5)

    # in horizontal and standing

    if angle == 0 and self.knots <= 0:
      return thrust * 2

    return 0
