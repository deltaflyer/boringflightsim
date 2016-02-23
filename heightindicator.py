import pygame
import os
class Heightindicator(pygame.sprite.Sprite):

  def __init__(self, screen):
    self.screen = screen
    self.position_x = 850
    self.position_y = 10
    self.old_value = 0
    pygame.sprite.Sprite.__init__(self)

    pygame.font.init()
    font_path = os.path.join('fonts', 'digital_display', 'digital_display_tfb.ttf')
    font_size = 28
    self.font_object = pygame.font.Font(font_path, font_size)

  def update(self, current_height):
    color = (0, 0, 0)
    polygon = [[0, 0], [0, 0], [0, 0]]
    relative_offset_x = 122
    relative_offset_y = 8

    speed_display = self.font_object.render("Height: " + str(current_height), 1,(255,255,255))
    self.screen.blit(speed_display, (self.position_x, self.position_y))
    
    # no value changes return
    if self.old_value == current_height:
        return

    if self.old_value > current_height:
        color = (255, 0, 0) # red
        polygon = [[self.position_x + relative_offset_x, self.position_y + relative_offset_y], [self.position_x + relative_offset_x + 20, self.position_y + relative_offset_y], [self.position_x + relative_offset_x + 10, self.position_y + relative_offset_y + 15]]
    else:
        color = (0, 255, 0) # green
        polygon = [[self.position_x + relative_offset_x, self.position_y + relative_offset_y + 15], [self.position_x + relative_offset_x + 20, self.position_y + relative_offset_y + 15], [self.position_x + relative_offset_x + 10, self.position_y + relative_offset_y]]
    pygame.draw.polygon(self.screen, color, polygon)
    self.old_value = current_height