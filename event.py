# # Import pygame, GameObject and initialize pygame
# from move import GameObject
# import pygame
# pygame.init()
#
# # Create screen
# screen = pygame.display.set_mode([500, 500])
#
#
# # ---------------------------------------------
# # Create player class this will extend GameObject, subclass
# class Player(GameObject):
#     def __init__(self):
#         super(Player, self).__init__(0, 0, 'player.png')
#         self.dx = 0
#         self.dy = 0
#         self.reset()
#
#     def left(self):
#         """
#         :desc: move the player when the left key is pressed
#         :return:
#         """
#         self.dx -= 100
#
#     def right(self):
#         """
#         :desc: move the player when the right key is pressed
#         :return:
#         """
#         self.dx += 100
#
#     def up(self):
#         """
#         :desc: move the player when the up key is pressed
#         :return:
#         """
#         self.dy -= 100
#
#     def down(self):
#         """
#         :desc: move the player when the down key is pressed
#         :return:
#         """
#         self.dy += 100
#
#     def move(self):
#         """
#         :desc: Updates the player's position in each frame
#         :return: None
#         """
#         # dx is where to go and x is the start
#         # Calculates the distance to move
#         self.x -= (self.x - self.dx) * 0.25
#         self.y -= (self.y - self.dy) * 0.25
#
#     def reset(self):
#         """
#         :desc: Moves sprite to the center of the screen. This is the player's starting position.
#         :return: None
#         """
#         self.x = 250 - 32
#         self.y = 250 - 32
#
#
# # Make an instance of Player
# player = Player()
#
# # -----------------------
# # Create game loop
# running = True
# while running:
#     # Look at events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         # Check for event types KEYBOARD
#         elif event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 running = False
#             elif event.type == pygame.K_LEFT:
#                 player.left()
#             elif event.type == pygame.K_RIGHT:
#                 player.right()
#             elif event.type == pygame.K_UP:
#                 player.up()
#             elif event.type == pygame.K_DOWN:
#                 player.down()
#
#     # Clear screen
#     screen.fill((255, 255, 255))
#     # --------------------------
#     # Draw player
#     player.move()
#     player.render(screen)
#
#     # Update the window
#     pygame.display.flip()
