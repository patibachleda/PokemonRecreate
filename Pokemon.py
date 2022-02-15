import pygame

names = ["Zubat", "Ponyta", "Jigglypuff"]
images = ["zubat.gif", "ponyta.png", "jigglypuff.gif"]

# Object class
class Pokemon:
    def __init__(self, number):
        self.name = names[number]
        self.image = images[number]
        self.health = 100
        self.lvl = 3
        self.damage = 20

    def attack(self, target):
        target.health = target.health - self.damage
            