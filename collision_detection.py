import os
import pygame

class CollisionDetection(pygame.sprite.Sprite):
    def __init__(self, screen, flightsim):
        # Data structures
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.plane = ''
        self.flightsim = flightsim
        self.groundobjects = ''
        # Font initialization
        pygame.font.init()
        font_path = os.path.join('fonts', 'int10h', 'PxPlus_IBM_VGA9.ttf')
        font_size = 20
        self.font_object = pygame.font.Font(font_path, font_size)

    def register_plane(self, plane):
        self.plane = plane

    def register_groundobjects(self, groundobjects):
        # Filter only for ground-objects that have been marked as crashable
        self.filtered_groundobjects = [x for x in groundobjects if x.is_crashable()]

    def __handle_collision(self, reason):
        self.plane.set_speed(0)
        self.flightsim.stop_simulation()
        speed_display = self.font_object.render("Simulation Ended! Reason: {}".format(reason), 1, (0, 0, 0))
        self.screen.blit(speed_display, (350, 400))

    def update(self):
        # TODO (oliver): check is the plane has crashed into the ground at high sink-rate
        # check if plane has crashed into a ground object
        current_plane_rect = self.plane.get_rect()
        for current_groundobject in self.filtered_groundobjects:
            for current_imagemap in current_groundobject.get_image_maps():
            # Skip objects that are behind the airplane
                if (current_plane_rect.x) > current_imagemap["rect"].x:
                    continue
            # Check if a collision occured
                if current_imagemap["rect"].colliderect(current_plane_rect):
                    self.__handle_collision("Crash into a ground object.")
