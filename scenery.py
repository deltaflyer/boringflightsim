# sprite for scenery
import pygame
import os


class Scenery(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self.screen = screen
        self.plane = ''

    def register_plane(self, plane):
        self.plane = plane

    def update(self, ):
        self.__print_background()
        self.__print_sky()
        self.__print_waters()

    def get_terrain_heigh_in_pixel(self):
        return 64

    def __print_waters(self):
        # if the plane is too high, then print no water
        if self.plane.get_y_coords() < 400:
            return
        x = 0
        correction_y = 0
        water = self.__get_water()

        # Calculate the correction factor for y based on plane height
        if (self.plane.get_y_coords()) < 450:
            correction_y = self.plane.get_y_coords() - 450

        # Print water
        water[1].centery = 730 - correction_y
        for i in range(1, 25):
            water[1].centerx = x
            self.screen.blit(water[0], water[1])
            x = x + 64

    def __get_water(self):
        water_img = pygame.image.load(os.path.join('graphics', 'water.png')).convert()
        water_rect = water_img.get_rect()
        return (water_img, water_rect)

    def __print_sky(self):
        # if the plane is too high, then print no water
        if self.plane.get_y_coords() < 350:
            return
        x = 0
        correction_y = 0
        sky = self.__get_sky()

        # Calculate the correction factor for y based on plane height
        if (self.plane.get_y_coords()) < 450:
            correction_y = self.plane.get_y_coords() - 450

        # Print water
        sky[1].centery = 650 - correction_y
        for i in range(1, 16):
            sky[1].centerx = x
            self.screen.blit(sky[0], sky[1])
            x = x + 112

    def __get_sky(self):
        sky_img = pygame.image.load(os.path.join('graphics', 'sky-layer.png')).convert()
        sky_rect = sky_img.get_rect()
        return (sky_img, sky_rect)

    def __print_background(self):
        self.screen.fill((182, 211, 225))
