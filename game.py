import sys, pygame
import random
from character import Character 
from grass import Grass 
from Pokemon import Pokemon 

pygame.init()
pygame.font.init()

#character attributes
SPEED = 7

#background attributes
size = width, height = 500, 499
black = 0, 0, 0
white = 255, 255, 255
background = pygame.image.load("grass_bg.png")

#window start
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon')

#grass start
picture = pygame.image.load("grass.png")
grass = pygame.transform.scale(picture, (50, 50))
# grass_rect = pygame.Rect(0,0, 50,50)

#fighting background
back = pygame.image.load("fight_bg.png")
pic = pygame.transform.scale(back, (500, 399))
back_rect = picture.get_rect()

#sprite lists for character and grass
all_sprites_list = pygame.sprite.Group()
enemies_list = pygame.sprite.Group()

#create character object
person = Character(70,70) 
all_sprites_list.add(person)

#text box attributes
font = pygame.font.SysFont(None, 32)
img = font.render('Pokemon Attacked!', True, (0,0,0), (255,255,255))
text_rect = img.get_rect(width=3000, height=150)

title = font.render("Pokemon", True, white)
caption = font.render("Pick your starting Pokemon!", True, white)


#starting pokemon
x = pygame.image.load("piplup.png")
one = pygame.transform.scale(x, (100, 100))

y = pygame.image.load("turtwig.png")
two = pygame.transform.scale(y, (100, 100))

z = pygame.image.load("charmander.png")
three = pygame.transform.scale(z, (100, 100))

turn = 2
scene = 0

#loads in the grass
for i in range(0, 4, 1):
    for j in range(0,11,1):
        grass = Grass(width-(45.45*(j+1)), height-(45.45*(i+1)), 50,50)
        all_sprites_list.add(grass)
        enemies_list.add(grass)

#starting scene
def main_scene():
    global scene

    #clicking within boundaries
    images = ["piplup.png", "turtwig.png", "charmander.png"]
    mouse = pygame.mouse.get_pos()

    #waits to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        #checks if a mouse is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if 50 <= mouse[0] <= 150 and height/2 <= mouse[1] <= height/2+100:
                person.pokemon = images[0]
                scene = 1
            elif 200 <= mouse[0] <= 300 and height/2 <= mouse[1] <= height/2+100:
                person.pokemon = images[1]
                scene = 1
            elif 350 <= mouse[0] <= 450 and height/2 <= mouse[1] <= height/2+100:
                person.pokemon = images[2]
                scene = 1
             
    screen.fill(black)

    #Title text box
    screen.blit(title , [width/2-50, 50])
    screen.blit(caption , [width/2-150, 100])

    #displaying the choices
    screen.blit(one, [50,height/2])
    screen.blit(two, [200,height/2])
    screen.blit(three, [350,height/2])

    #screen loading
    if scene == 1:
        screen.fill(black)
        pygame.time.wait(50)

    pygame.time.wait(10)
    pygame.display.flip()

#game scene
def game_scene():
    global scene
    key = pygame.key.get_pressed()

    #waits to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()

        
    #character movement
    if key[pygame.K_LEFT]:
        person.moveLeft(SPEED)
    elif key[pygame.K_RIGHT]:
        person.moveRight(SPEED)
    elif key[pygame.K_UP]:
        person.moveUp(SPEED)
    elif key[pygame.K_DOWN]:
        person.moveDown(SPEED)

    #creates the background
    screen.fill(black)
    screen.blit(background, [0,0])

    #collision detection
    if pygame.sprite.spritecollide(person, enemies_list, False) :
        if random.randint(1,100) == 1:
            #Change to fight screen
            screen.blit(img, (150,50), text_rect)
            scene = 2
        
    
    #end stuff
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.time.wait(10)
    pygame.display.flip()

    #if pokemon attacked cause delay before switching
    if scene == 2:
        pygame.time.wait(1100)

        #picks a pokemon
        pokemon = Pokemon(random.randint(0,2))
        return pokemon
    return None

#fight scene
def fight_scene(pokemon):   
    #texts
    wild = font.render('A wild ' + pokemon.name  + ' appeared!', True, black)
    wild_rect = img.get_rect(width=270, height=150)

    pAttack = font.render(pokemon.name + ' used Attack!', True, black)
    pAttack_rect = img.get_rect(width=270, height=150)

    uAttack = font.render('You used Attack!', True, black)
    uAttack_rect = img.get_rect(width=270, height=150)

    health1 = font.render('HEALTH: ' + str(person.health), True, black)
    health1_rect = img.get_rect(width=270, height=150)

    health2 = font.render('HEALTH: ' + str(pokemon.health), True, black)
    health2_rect = img.get_rect(width=270, height=150)

    win = font.render('You win!', True, black)
    win_rect = img.get_rect(width=270, height=150)

    lose = font.render('You fainted...', True, black)
    lose_rect = img.get_rect(width=270, height=150)

    global scene
    global turn

    #waits to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)

    #update text box depending on winner (doesn't work idk why)
    if pokemon.health < 0 or person.health < 0:
        scene = 1
        if pokemon.health < 0:
            screen.blit(win, (width/2-100,425), win_rect)
        elif person.health < 0:
            screen.blit(lose, (width/2-100,425), lose_rect)
        pokemon.health = 100
        person.health = 100

        pygame.display.flip()
        pygame.time.wait(1100)
        screen.fill(black)

        return

    #adjusts the image to fit screen
    rect = back_rect.move((0, 0))
    screen.blit(pic, rect)

    #load in character and pokemon
    screen.blit(pygame.transform.scale(pygame.image.load(person.pokemon), (100, 100)), [50,300])
    screen.blit(pygame.transform.scale(pygame.image.load(pokemon.image), (150, 150)), [300,110])
    #set up text box
    textbox = pygame.draw.rect(screen, (white), pygame.Rect(0, height-100, 500, 100))
    border = pygame.draw.rect(screen, (black), pygame.Rect(0, height-100, 500, 100), width =  5)
    pygame.display.update()

    screen.blit(health1, (50,270), health1_rect)
    screen.blit(health2, (310,270), health2_rect)

    if turn == 0:
        #text box
        screen.blit(pAttack, (width/2-120,425), pAttack_rect)
        #attack
        pokemon.attack(person) 
        turn = 1

    elif turn == 1:
        #text box
        screen.blit(uAttack, (width/2-100,425), uAttack_rect)
        #attack
        person.attack(pokemon)
        turn = 0
    else:
        screen.blit(wild, (width/2-100,425), wild_rect)
        turn = 0


    #screen loading
    pygame.display.flip()
    pygame.time.wait(2000)
    


while True:
    if scene == 0:
        main_scene()
    elif scene == 1:
        pokemon = game_scene()
    elif scene == 2:
        fight_scene(pokemon)