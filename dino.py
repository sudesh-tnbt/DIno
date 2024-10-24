import pygame as py
import os

py.init()

width = 1100
height = 600
screen = py.display.set_mode((width, height))

variables = [py.image.load(os.path.join("Assets/Bird", "Bird1.png")),
             py.image.load(os.path.join("Assets/Bird", "Bird2.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")),
             py.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")),
             py.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoDead.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoDuck2.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoJump.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoRun1.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoRun2.png")),
             py.image.load(os.path.join("Assets/Dino", "DinoStart.png")),
             py.image.load(os.path.join("Assets/Other", "Cloud.png")),
             py.image.load(os.path.join("Assets/Other", "GameOver.png")),
             py.image.load(os.path.join("Assets/Other", "Reset.png")),
             py.image.load(os.path.join("Assets/Other", "Track.png"))]

class Dinosaur:
    pass

def main():
    run = True
    clock = py.time.Clock()
    player = Dinosaur()

    while run:
        for event in py.event.get():
            if event.type == py.quit():
                run = False

        screen.fill((255, 255, 255))
        prompt = py.key.get_pressed()

        player.draw(screen)
        player.update(prompt)