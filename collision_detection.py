import os
import pygame

class CollisionDetection(pygame.sprite.Sprite):
    def __init__(self, screen, flightsim):
        # Constants
        self.MAX_ALLOWED_SINKRATE = 7
        self.PLANE_GROUND_TOUCHDOWN = 660
        #  Variables
        self.screen = screen
        pygame.sprite.Sprite.__init__(self)
        self.plane = ''
        self.flightsim = flightsim
        self.groundobjects = ''
        self.old_feet_value = 0
        self.is_crashed = False
        self.reason = ''
        self.sinkrate_cycle = 0
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

    def __handle_collision(self):
        self.plane.set_speed(0)
        self.flightsim.stop_simulation()
        speed_display = self.font_object.render("Simulation Ended! Reason: {}".format(self.reason), 1, (0, 0, 0))
        self.screen.blit(speed_display, (350, 400))

    def __detect_groundobject_crash(self):
        """
        check if plane has crashed into a ground object
        """
        current_plane_rect = self.plane.get_rect()
        for current_groundobject in self.filtered_groundobjects:
            for current_imagemap in current_groundobject.get_image_maps():
            # Skip objects that are behind the airplane
                if (current_plane_rect.x) > current_imagemap["rect"].x:
                    continue
            # Check if a collision occured
                if current_imagemap["rect"].colliderect(current_plane_rect):
                    # yes, set crash states
                    self.is_crashed = True
                    self.reason = "Crash into a ground object."

    def __detect_ground_crash(self):
        """
        Check if the plane has gone into ground with a very high sinkrate
        """
        # To get a better resolution of the sinkrate at high speeds
        # the ground detection is only done every second frame.
        if self.sinkrate_cycle < 2:
            self.sinkrate_cycle += 1
            return
        self.sinkrate_cycle = 0
        # only check sinkrate, if we are airborne and the plan
        if (self.plane.get_feet() > 1):
            # Does the plane sink?
            if self.old_feet_value > self.plane.get_feet():
                sinkrate = (self.old_feet_value - self.plane.get_feet())
                is_sinkrate_not_in_tolerance = (sinkrate > self.MAX_ALLOWED_SINKRATE)
                is_plane_on_ground = ((self.PLANE_GROUND_TOUCHDOWN - self.plane.get_y_coords()) < 10)
                is_plane_not_leveled = ((self.plane.get_angle() < -6) or (self.plane.get_angle() > 6))
                # Is the plane sinking too fast?
                if (is_plane_on_ground and is_sinkrate_not_in_tolerance):
                     self.is_crashed = True
                     self.reason = "Crashed into ground. Sinkrate out of tolerance."
                # Is the plane leveled when touching the ground
                if (is_plane_on_ground and is_plane_not_leveled):
                    self.is_crashed = True
                    self.reason = "Crashed into ground. Plane was not leveled."
                # Is the plane landing with gear out?
                if (not self.plane.gear_down and is_plane_on_ground):
                    self.is_crashed = True
                    self.reason = "Crashed into ground. Gear was retracted."
            self.old_feet_value = self.plane.get_feet()

    def update(self):
        if self.is_crashed:
            self.__handle_collision()
        else:
            self.__detect_groundobject_crash()
            self.__detect_ground_crash()
