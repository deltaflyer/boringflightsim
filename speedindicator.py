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
    speed = int(current_speed + 0.5)
    speed_display = self.font_object.render("Speed: " + str(speed), 1,(36,255,0))
    pygame.draw.rect(self.screen, (0, 0, 0), (1015, 10 , 100 , 30), 0)
    self.screen.blit(speed_display, (1020, 10))