import pygame
import json
import os
import random


class GroundObjects():
    def __init__(self, screen):
        # Data structures
        self.screen = screen
        self.plane = ''
        self.groundobjects = []
        # Load declarations
        dir_path = os.path.dirname(os.path.realpath(__file__))
        ground_object_path = os.path.join(dir_path, 'ground_objects', 'declaration.json')
        with open(ground_object_path, "r") as fp:
            declarations = json.load(fp)["objects"]
        # Create Ground objects
        for declaration in declarations:
            self.groundobjects.append(
                self.GroundObject(
                    screen,
                    declaration["x"],
                    declaration["y"],
                    declaration["repeat"],
                    declaration["crashable"],
                    declaration["texture"]
                )
            )
        

    def register_plane(self, plane):
        self.plane = plane
        # propage the plane to all groundobjects
        for groundobject in self.groundobjects:
            groundobject.register_plane(plane)

    def update(self):
        for groundobject in self.groundobjects:
            groundobject.update()

    def get_groundobjects(self):
        return self.groundobjects

    class GroundObject(pygame.sprite.Sprite):
        def __init__(self, screen, x, y, repeat, crashable, texture):
            # Initialize members
            self.screen = screen
            self.plane = ''
            self.crashable = crashable
            self.last_travelled_x_distrance = 0
            dir_path = os.path.dirname(os.path.realpath(__file__))
            texture_path = os.path.join(dir_path, 'graphics', texture)
            img = pygame.image.load(texture_path)
            # us a list of rects to repeat the image
            self.image_maps = []
            for current_repetition in range(0, repeat):
                image_map = {}
                # load the image
                image_map["texture"] = img
                image_map["rect"] = image_map["texture"].get_rect()
                width = image_map["rect"].size[0]
                # compute the offset based on the repetition
                image_map["rect"].centerx = x + (width * current_repetition)
                # ground objects are on the ground, in line
                image_map["rect"].centery = y
                image_map["original_centery"] = y
                # append the newly computed rect
                self.image_maps.append(image_map)
            # Init the sprite
            pygame.sprite.Sprite.__init__(self)

        def register_plane(self, plane):
            self.plane = plane
            self.last_travelled_x_distrance = plane.get_travelled_x_distance()

        def is_crashable(self):
            return self.crashable

        def get_image_maps(self):
            return self.image_maps

        def update(self):
            # Compute the new x-offsets
            x_offset = self.plane.get_travelled_x_distance() - self.last_travelled_x_distrance
            # Calculate the correction factor for y based on plane height
            y_offset = self.plane.get_y_coords() - 450
            for i in range(0, len(self.image_maps)):
                # if the image is not on the screen anymore skip processing
                if ((self.image_maps[i]["rect"].centerx < -300) or (self.image_maps[i]["rect"].centerx > 8000)):
                    continue
                else:
                    # Blit the ground texture
                    self.screen.blit(self.image_maps[i]["texture"], self.image_maps[i]["rect"])
                    # update x-coordinates if the plane has moved
                    if x_offset > 0:
                        self.image_maps[i]["rect"].centerx -= x_offset
                    # Correction for ground level
                    if (self.plane.get_y_coords()) < 450:
                        # Restore previous y value
                        self.image_maps[i]["rect"].centery =  self.image_maps[i]["original_centery"] - y_offset
            # Update plane distance:
            self.last_travelled_x_distrance = self.plane.get_travelled_x_distance()
