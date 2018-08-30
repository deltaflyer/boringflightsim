import pygame
import os

class Plane(pygame.sprite.Sprite):
    def __init__(self, screen, scenery):

        # static
        self.TAKEOFFSPEED = 100

        pygame.sprite.Sprite.__init__(self)

        self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small_gear.png'))
        self.plane_rect = self.plane_img.get_rect()
        self.plane_rect.centerx = 400
        self.plane_rect.centery = 660
        # Distance travelled in x-direction
        self.travelled_x_distance = 0

        self.screen = screen
        self.scenery = scenery

        self.gear_down = True
        self.air_brake_out = False
        self.engine_running = True

        self.angle = 0
        self.angle_old = 0
        self.set_angle = 0

        self.thrust = 1
        self.thrust_old = 0
        self.set_thrust = 0

        # 485 Knots = 900 km/h
        self.knots = 0

        self.feet = 0

        self.images_computes = self.__precompute_rotated_plane(self.plane_img, self.plane_rect)
        self.explosion_images = self.__load_explosion_images()
        self.explosion_counter = 0

    def __precompute_rotated_plane(self, image, rect):
        images_computes = {}
        for degree in xrange(-180, 180):
            images_computes[degree] = self.__rot_center(image, rect, degree)
        return images_computes

    def __rot_center(self, image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return (rot_image, rot_rect)

    def __load_explosion_images(self):
        retval = []
        for i in range(1, 25):
            image = pygame.image.load(
                        os.path.join(
                        'graphics',
                        "explosion_{}.png".format(i)
                        )
                    )
            rect = image.get_rect()
            retval.append((image, rect))
        return retval

    def increase_speed(self):
        if self.set_thrust < 100 and self.engine_running:
            self.set_thrust = self.set_thrust + 10

    def decrease_speed(self):
        if self.set_thrust > 0:
            self.set_thrust = self.set_thrust - 10

    def turn_engines_off(self):
        self.engine_running = False

    def get_angle(self):
        return self.angle

    def get_speed(self):
        return self.knots

    def set_speed(self, knots):
        self.knots = knots

    def get_y_coords(self):
        return self.plane_rect.centery

    def push_down(self):
        if self.set_angle > -20 and self.feet > 0:
            self.set_angle = self.set_angle - 5

    def pull_up(self):
        if self.set_angle < 20 and self.knots > self.TAKEOFFSPEED:
            self.set_angle = self.set_angle + 5

    def get_feet(self):
        return self.feet

    def get_thrust(self):
        return self.thrust

    def get_travelled_x_distance(self):
        return self.travelled_x_distance

    def get_rect(self):
        return self.plane_rect

    def update(self):
        # Bring real angle to set_angle
        self.__update_angles()

        # Bring real thrust to set thrust
        self.__update_thrust()

        # Compute the speed
        self.__update_knots()

        # Update travelled x direction
        self.__update_x_travelled_instance()

        # Compute the height
        if self.feet >= 0:
            self.feet = self.feet + self.__calculate_climbrate(self.angle, self.knots)
        if self.feet < 0:
            self.feet = 0

        # Incrementally rotate the plane sprite
        if int(self.angle) is not int(self.angle_old):
            result = self.__compute_single_plane(self.feet, self.angle)
            self.plane_img = result[0]
            self.plane_rect = result[1]

        # Render the plane
        self.screen.blit(self.plane_img, self.plane_rect)

        # Shutdown thrust if engines are shutdown
        if not self.engine_running and self.thrust > 0:
            self.decrease_speed()

        # Render the explosion frame by frame if the engines are out
        if not self.engine_running and self.explosion_counter < 24:
            explosion_rect = self.explosion_images[self.explosion_counter][1]
            # center the explosion rect on the plane engines position
            explosion_rect.centerx = self.plane_rect.centerx + 20
            explosion_rect.centery = self.plane_rect.centery + 20
            self.screen.blit(
                self.explosion_images[self.explosion_counter][0],
                explosion_rect
                )
            # Slow down the explosion effect
            if self.travelled_x_distance % 4 == 0:
                self.explosion_counter += 1

    def __update_thrust(self):
        # Incrementally change the thrust
        if self.thrust is self.set_thrust:
            return
        self.thrust_old = self.thrust
        if self.thrust < self.set_thrust:
            self.thrust = self.thrust + 1
        if self.thrust > self.set_thrust:
            self.thrust = self.thrust - 1

    def __update_angles(self):
        if int(self.angle) is not int(self.set_angle):
            self.angle_old = self.angle
            # Pull nose up
            if self.angle < self.set_angle:
                self.angle = self.angle + 0.5
            # Push nose down
            if self.angle > self.set_angle:
                self.angle = self.angle - 0.5

    def __calculate_climbrate(self, angle, speed):
        if int(self.angle) is 0 and int(self.set_angle) is 0:
            return 0
        value = 3  # default
        if speed < 100:
            return 0
        if speed < 200:
            value = 1
        if speed < 400:
            value = 2
        if angle < 0:
            return value * -1
        return value

    def toggle_landing_gear(self):
        # Below 50 feet the landing gear cannot be retracted
        if self.feet < 50:
            return
        # Toggle the gear state
        plane_temp_x = self.plane_rect.centerx
        plane_temp_y = self.plane_rect.centery
        if self.gear_down:
            self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small.png'))
            self.gear_down = False
        else:
            self.plane_img = pygame.image.load(os.path.join('graphics', 'plane_small_gear.png'))
            self.gear_down = True
        # Calculate the new images
        self.plane_rect = self.plane_img.get_rect()
        self.plane_rect.centerx = plane_temp_x
        self.plane_rect.centery = plane_temp_y
        self.images_computes = self.__precompute_rotated_plane(self.plane_img, self.plane_rect)

    def toggle_airbrake(self):
        self.air_brake_out = not self.air_brake_out

    def __compute_single_plane(self, feet, angle):
        smoothed_angle = int(angle + 0.5)
        plane_img = self.images_computes[smoothed_angle][0]
        plane_rect = self.images_computes[smoothed_angle][1]
        x_delta = int((feet * 1.6) + 0.5)
        plane_rect.centery = 745 - x_delta

        # Limit sliding space of the plane to the upper and lower barrier
        if plane_rect.centery > 660:
            plane_rect.centery = 660
        if plane_rect.centery < 280:
            plane_rect.centery = 280

        return (plane_img, plane_rect)

    def __update_knots(self):
        # Bring real knots to set_knots
        self.knots = self.knots + self.__calculate_acceleration(self.angle, self.thrust)

    def __update_x_travelled_instance(self):
        if self.knots <= 0:
            return
        if self.knots > 40:
            self.travelled_x_distance += int(round(self.knots // 40))
            return
        if self.knots > 30:
            self.travelled_x_distance += int(round(self.knots // 30))
            return
        if self.knots > 20:
            self.travelled_x_distance += int(round(self.knots // 20))
            return
        if self.knots > 10:
            self.travelled_x_distance += int(round(self.knots // 10))
            return
        if self.knots > 5:
            self.travelled_x_distance += int(round(self.knots // 5))
            return
        if self.knots > 2:
            self.travelled_x_distance += int(round(self.knots // 2))
            return
        self.travelled_x_distance += int(round(self.knots))


    def __calculate_acceleration(self, angle, thrust):
        thrust_coeff = 0.002
        air_drag = 0.08
        temp_val = 0

        # If the gear is down the air drag increases
        if self.gear_down and self.feet > 50:
            air_drag = air_drag * 2

        # If the airbreak is out increase the airdrag
        if self.air_brake_out and self.knots > 0:
            air_drag = air_drag * 2

        # in case of climb decrease acceleration based on angle
        if int(angle + 0.5) > 0:
            return (thrust * thrust_coeff) - (angle * (thrust_coeff * 6))

        # in case of decent increas acceleration based on angle
        if int(angle + 0.5) < 0:
            return (thrust * thrust_coeff) - (angle * (thrust_coeff * 6)) - air_drag

        # in horizontal and moving
        if int(angle + 0.5) == 0:
            temp_val = (thrust * thrust_coeff)
            if self.knots > 0:
                temp_val = temp_val - air_drag
            return temp_val
