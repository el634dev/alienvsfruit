# Import class Apple, apple object
from Apple import Apple
# Import class Strawberry, strawberry object
from Strawberry import Strawberry
# Import class Bomb, bomb object
from Bomb import Bomb
# Import class ship, ship that appears in the background
from Ship import Ship
# Import class Player, player object
from Player import Player
# Import class ScoreBoard
from ScoreBoard import ScoreBoard

import pygame
pygame.init()
pygame.font.init()

# Get the clock
clock = pygame.time.Clock()
# Trigger the clock
clock.tick(60)
# Configure the screen
screen = pygame.display.set_mode([375, 667])
screen.fill(color="orange")


# Make two apples
apple = Apple()
apple_2 = Apple()

# Make two strawberries
strawberry = Strawberry()
strawberry_2 = Strawberry()

# Make an instance of Player
player = Player()

# Make two bombs
bomb = Bomb()
# bomb_2 = Bomb()

# Make a spaceship
spaceship = Ship()

# Create a score instance
score = ScoreBoard(30, 30, 0)

# Make two groups
all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()

# Add sprites to group
all_sprites.add(player)
all_sprites.add(bomb)
# all_sprites.add(bomb_2)
all_sprites.add(spaceship)
all_sprites.add(score)

# Fruit sprites to populate
fruit_sprites.add(apple)
fruit_sprites.add(apple_2)
fruit_sprites.add(strawberry)
fruit_sprites.add(strawberry_2)

# -------------------------------------
# Create the game loop
running = True
while running:
    # Looks at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            score.reset()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_UP:
                player.up()
            elif event.key == pygame.K_DOWN:
                player.down()

        fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
        # collision = pygame.sprite.spritecollideany(player, bomb)
        if fruit:
            score.update(100)
            fruit.reset()
        elif pygame.sprite.collide_circle(player, bomb):
            score.reset()
            player.reset()
            bomb.reset()
            running = False

    # Clear screen
    screen.fill((255, 165, 0))
    # Move and render sprites
    for entity in all_sprites:
        entity.move()
        entity.render(screen)

    for fruit in fruit_sprites:
        fruit.move()
        fruit.render(screen)

    # -----------------------------
    # Update the window
    pygame.display.flip()
    # Trigger the clock
    clock.tick(60)
