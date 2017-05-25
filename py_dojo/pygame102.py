# pygame101
import pygame

from pygame.locals import *
from pygame.math import *

from pygame_appentry import *
import py_global as glob
import py_physics.py_physics_simulation as physics


class Box:
    m_pos = (0, 0, 0)
    m_size = 8
    m_color = (255, 255, 255)


class Container:
    m_size = 64


class TreeNode:
    m_pos = (0, 0, 0)
    m_size = 8
    m_children = [None]


class BoxPacker:
    m_root = TreeNode()

    def __init__(self):
        pass


class App(BaseApp):
    def init(self):
        pass

    def update(self):
        self.handle_input()
        # game update

    def render(self):
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
        pygame.a
        pass

if __name__ == "__main__":
    theApp = App()
    theApp.on_execute()