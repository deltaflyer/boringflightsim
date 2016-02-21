import pygame
import os
class Debug(pygame.sprite.Sprite):

  def __init__(self, screen, plane):
    self.plane = plane
    self.screen = screen
    pygame.sprite.Sprite.__init__(self)

    pygame.font.init()
    font_path = os.path.join('fonts', 'int10h', 'PxPlus_IBM_VGA9.ttf')
    font_size = 14
    self.font_object = pygame.font.Font(font_path, font_size)

  def update(self):
    y_offset = 0
    output = []
    output.append("Feet:       " + str(self.plane.feet))
    output.append("Old Feet:   " + str(self.plane.feet_old))
    output.append("Angle:      " + str(self.plane.angle))
    output.append("Set Angle:  " + str(self.plane.set_angle))
    output.append("Thrust:     " + str(self.plane.thrust))
    output.append("Set Thrust: " + str(self.plane.set_thrust))
    for line in output:
        speed_display = self.font_object.render(line, 1,(255,255,255))
        self.screen.blit(speed_display, (1150, 20 + y_offset))
        y_offset += 14