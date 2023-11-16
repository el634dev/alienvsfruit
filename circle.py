# Import and initialize pygame
import pygame
pygame.init()

# Configure the screen
screen = pygame.display.set_mode([500, 500])

# --------------------------------------
# Create the game loop
running = True
while running:
    # Look at events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))
    # -----------------------------
    # Draw a circle - Center
    color = (255, 200, 105)
    position = (250, 250)
    pygame.draw.circle(screen, color, position, 75)
    # -----------------------------
    # Circle 2 - Top left
    color = (245, 39, 39)
    position = (80, 80)
    pygame.draw.circle(screen, color, position, 75)
    # -----------------------------
    # Circle 3 - Top right
    color = (255, 115, 15)
    position = (420, 80)
    pygame.draw.circle(screen, color, position, 75)
    # Circle 4 - Lower Left
    color = (13, 222, 131)
    position = (80, 410)
    pygame.draw.circle(screen, color, position, 75)
    # -----------------------------
    # Circle 4 - Lower Right
    color = (13, 222, 131)
    position = (420, 410)
    pygame.draw.circle(screen, color, position, 75)
    # Update the display
    pygame.display.flip()
