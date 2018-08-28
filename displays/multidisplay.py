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
        self.old_altidude = 0

    def update(self):
        y_offset = 0
        output = []

        if self.plane.gear_down:
            output.append(('GREEN', '[INFO] GEAR DOWN AND LOCKED '))

        if self.plane.air_brake_out:
            output.append(('GREEN', '[INFO] AIR BREAK OUT'        ))

        if self.plane.get_feet() < 250 and (not self.plane.gear_down and self.old_altidude > self.plane.get_feet()):
            output.append(('RED',   '[WARN] TERRAIN - PULL UP'    ))

        if self.plane.get_speed() > 520:
            output.append(('RED',   '[WARN] OVERSPEED - BREAK NOW'))

        if self.plane.get_speed() > 550:
            output.append(('RED',   '[WARN] MAXIMUM SPEED - BREAK '))

        if self.plane.get_speed() < 120 and self.plane.get_feet() > 5:
            output.append(('RED',   '[WARN] UNDERSPEED - ACC NOW  '))

        if len(output) is 0:
            output = [('AMBER', "Multi Display in standby")]

        pygame.draw.rect(self.screen, (0, 0, 0), (self.x - 3, self.y, 250, (len(output) + 1) * 11), 0)
        for line in output:
            color = (255, 194, 0)
            if line[0] == "GREEN":
                color = (36, 255, 0)
            if line[0] == "RED":
                color = ((255, 0, 0))
            multidisplay = self.font_object.render(line[1], 1, color)
            self.screen.blit(multidisplay, (self.x, self.y + y_offset + 3))
            y_offset += 14

        self.old_altidude = self.plane.get_feet()
