import pygame
import os
class Speedindicator(pygame.sprite.Sprite):

  def __init__(self, screen):
    self.screen = screen
    pygame.sprite.Sprite.__init__(self)

    pygame.font.init()
    font_path = os.path.join('fonts', 'digital_display', 'digital_display_tfb.ttf')
    font_size = 28
    self.font_object = pygame.font.Font(font_path, font_size)

  def update(self, current_speed):
    speed_display = self.font_object.render("Speed: " + str(current_speed), 1,(255,255,255))
    self.screen.blit(speed_display, (1000, 10))