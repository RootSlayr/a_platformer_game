import os
import random
import math
import pygame
from os import listdir
from os.path import isfile, join

pygame.init()

pygame.display.set_caption("Platformer")

# BG_COLOR = (255, 255, 255)
WIDTH, HEIGHT = 1000, 800
FPS = 60
PLAYER_VEL = 5

window = pygame.display.set_mode((WIDTH, HEIGHT))

class Player(pygame.sprite.Sprite):
    COLOR = (255, 0, 0)

    def __init__(self, x,y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.x_vel = 0
        self.y_vel = 0
        self.mask = None
        self.direction = "left"
        self.animation_count = 0
    
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
    
    def move_left(self, vel_left):
        self.x_vel = -vel_left
        if self.direction != "left":
            self.direction = "left"
            self.animation_count = 0

    def move_right(self, vel_right):
        self.x_vel = vel_right
        if self.direction != "right":
            self.direction = "right"
            self.animation_count = 0

    def loop(self, fps):
        self.move(self.x_vel, self.y_vel)

    def draw(self, window):
        pygame.draw.rect(window, self.COLOR, self.rect)

def get_bg(name):
    image = pygame.image.load(join('assets','Background',name))
    _, _, width, height = image.get_rect()
    tiles = []

    for i in range(WIDTH//width + 1):
        for j in range( HEIGHT // height +1):
            pos = (i* width, j*height)
            tiles.append(pos)

    return tiles, image

def draw(window, background, bg_image, player):
    for tile in background:
        window.blit(bg_image, tile)
    
    player.draw(window)

    pygame.display.update()


def main(window):
    clock  = pygame.time.Clock()
    background, bg_img = get_bg("Blue.png")
    run = True

    player = Player(100, 100, 50, 50)
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw(window, background, bg_img, player)
    pass


if __name__ == "__main__":
    main(window)