import pygame

# Object class
class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, height, width):
        super().__init__()

        #load in image
        self.image = pygame.image.load("grass.png")
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = pygame.Rect(x ,y ,height, width)
  