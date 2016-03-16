import pygame
import os


class Multidisplay(pygame.sprite.Sprite):
    def __init__(self, screen, plane):
        self.screen = screen
        self.plane = plane
        pygame.sprite.Sprite.__init__(self)
        pygame.font.init()
        font_path = os.path.join('fonts', 'int10h', 'PxPlus_IBM_VGA9.ttf')
        font_size = 14
        self.font_object = pygame.font.Font(font_path, font_size)
        self.x = 420
        self.y = 10

    def update(self):
        y_offset = 0
        output = []

        if self.plane.gear_down:
            output.append('[INFO]    GEAR DOWN')

        if len(output) is 0:
            output = ["Multi Display in standby"]

        for line in output:
            speed_display = self.font_object.render(line, 1, (36, 255, 0))
            pygame.draw.rect(self.screen, (0, 0, 0), (self.x - 3, self.y, 250, 20), 0)
            self.screen.blit(speed_display, (self.x, self.y + y_offset + 3))
            y_offset += 14
