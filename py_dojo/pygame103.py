# pygame101
import os.path
import math

import pygame

from pygame.locals import *
from pygame.math import *

from pygame_appentry import *
import py_global as glob
import py_physics.py_physics_simulation as physics

class Triangle:
    pass

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()


class Actor(pygame.sprite.Sprite):
    speed = 100
    images = []

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def initialize(self):
        self.image = self.images[0]
        self.image = pygame.transform.scale(self.image, [200, 200])
        self.rect = self.image.get_rect()

    def update(self):
        #self.rect.move_ip(0, self.speed * glob.GAME_CLOCK.get_time() * 0.001)
        self.rect.x = 200 + math.cos(glob.GAME_TIME * 0.005) * 100
        self.rect.y = 200 + math.sin(glob.GAME_TIME * 0.05) * 100
        pass

    def set_position(self, x, y):
        self.rect.x = x
        self.rect.y = y

class App(BaseApp):
    draw_group = pygame.sprite.RenderUpdates()

    actor0 = Actor()

    def init(self):
        #Load images, assign to sprite classes
        # #(do this before the classes are used, after screen setup
        img = load_image('asprite.bmp')
        Actor.images = [img]

        self.actor0.initialize()
        self.actor0.set_position(200,200)

        self.draw_group.add(self.actor0)

    def update(self):
        self.handle_input()

        self.actor0.update()
        # game update

    def render(self):
        dirty = self.draw_group.draw(glob.MAIN_SURFACE)
        pass

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.m_active = False
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    pass

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            print("Key pressed")

    def initPolygon(self):
        pass

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()
