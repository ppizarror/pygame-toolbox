"""
CenteredFigure class example.
"""
import sys
import os
import pygame
from pygame.locals import QUIT
import random

# Add previous folder to path
sys.path.append('../')

# Import CenteredFigure
from centered_figure import CenteredFigure

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Screen size
S_WIDTH = 640
S_HEIGHT = 480

# Total figures on screen
TOTAL_FIGURES = 50

# Init pygame modules
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create pygame window
surface = pygame.display.set_mode((S_WIDTH, S_HEIGHT))
pygame.display.set_caption('CenteredFigure example 2')

# Create pygame timer
clock = pygame.time.Clock()

# Create figures
figure_list = []  # Stores CenteredFigure objects
figure_angvel = []  # Store angular velocity to each figure
for i in range(TOTAL_FIGURES):
    # Create center of figure
    center_square = [random.randrange(0, S_WIDTH),
                     random.randrange(0, S_HEIGHT)]

    # Create random color
    color = (random.randrange(0, 255), random.randrange(0, 255),
             random.randrange(0, 255))

    # Create object
    square = CenteredFigure([(-1, -1), (-1, 1), (1, 1), (1, -1)], center_square,
                            color=color)

    # Set figure surface
    square.set_surface(surface)

    # Create figure scale
    scale = random.randrange(1, 50)
    square.scale(scale)

    # Create angular velocity between -2 and 2
    angvel = random.random() * random.choice([-2, 2])

    # Append figure to list
    figure_list.append(square)
    figure_angvel.append(angvel)

# Main loop
while True:

    # Set clock (60FPS)
    clock.tick(60)

    # Check events
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()

    # Fill surface
    surface.fill(COLOR_BLACK)

    # Rotate figures, Scale and draw
    for f in range(TOTAL_FIGURES):
        figure = figure_list[f]
        angle = figure_angvel[f]

        # Rotate figure
        figure.rotate(angle)

        # Draw figure
        figure.draw()

    # Flip display
    pygame.display.flip()
