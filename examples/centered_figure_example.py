"""
CenteredFigure class example.
"""
import sys
import os
import pygame
from pygame.locals import QUIT

# Add previous folder to path
sys.path.append('../')

# Import CenteredFigure
from centered_figure import CenteredFigure

# Colors
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)

# Init pygame modules
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Create figure
center_square = [400, 300]
center_triangle = [200, 200]

square = CenteredFigure([(-1, -1), (-1, 1), (1, 1), (1, -1)], center_square,
                        color=COLOR_WHITE)
triangle = CenteredFigure([(-1, -0.5), (0, 1.0), (-1, 0.5)], center_triangle,
                          color=COLOR_WHITE)

# Create pygame window
surface = pygame.display.set_mode((640, 480))
pygame.display.set_caption('CenteredFigure example')

# Create pygame timer
clock = pygame.time.Clock()

# Set figure surfaces
square.set_surface(surface)
triangle.set_surface(surface)

# Scale figures
triangle.scale(30)
square.scale(50)

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

    # Rotate figures
    square.rotate(1)
    triangle.rotate(0)

    # Draw figures
    square.draw()
    triangle.draw()

    # Flip display
    pygame.display.flip()
