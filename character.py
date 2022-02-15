import pygame

# Object class
class Character(pygame.sprite.Sprite):
    def __init__(self, height, width):
        super().__init__()

        #set up coordinates and movement
        self.x = 220
        self.y = 0

        #load in image
        self.image = pygame.image.load("person.png")
        self.image = pygame.transform.scale(self.image, (height, width))
        self.rect = pygame.Rect(self.x, self.y ,height, width)

        self.pokemon = "person.png"
        self.health = 100
        self.damage = 30

        self.last_grass = None

    #attack function
    def attack(self, target):
        target.health = target.health - self.damage

    #movement functions
    def moveRight(self, pixels):
        if self.rect.x <= 435:
            self.rect.x += pixels
  
    def moveLeft(self, pixels):
        if self.rect.x >= 0:
            self.rect.x -= pixels
  
    def moveUp(self, speed):
        if self.rect.y >= 0:
            self.rect.y -= speed * speed/10
  
    def moveDown(self, speed):
        if self.rect.y <= 430:
            self.rect.y += speed * speed/10
    