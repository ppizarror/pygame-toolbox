"""
Centered polygon figure, needs shapely and pygame.

Create figure with an (x,y) center, set color, thickness and surface to plot
(optional).

Usage:
    triangle = CenteredFigure([(0, 0), (0, 1), (0, 3)], [10, 10])
    square = CenteredFigure([(0, 0), (0, 1), (1, 1), (1, 0)], [10, 10])

    triangle.intersect(square) -> true

Copyright (C) 2017 Pablo Pizarro @ppizarror

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
"""

# Imports
from shapely.geometry import Polygon
import pygame


class CenteredFigure(object):
    def __init__(self, points, center, color=None, width=0,
                 pygame_surface=None):
        """
        Create centered figure from point list with center (x,y).

        :param points: Vertices tuple list (ex. [(10,10), (10,5)...])
        :type points: list
        :param center: Center list (ex [10, 10])
        :type center: list
        :param color: Pygame color
        :type color: pygame.Color
        :param width: Border width (px)
        :param pygame_surface: Pygame surface object
        :type pygame_surface: pygame.display
        """
        self._points = points
        self._center = center
        self._color = color
        self._width = width
        self._surface = pygame_surface

    def set_color(self, color):
        """
        Set figure color.

        :param color: Pygame color
        :return:
        """
        self._color = color

    def set_surface(self, surface):
        """
        Set pygame surface object.

        :param surface: Pygame display surface.
        :type surface: pygame.display
        :return:
        """
        self._surface = surface

    def set_center(self, center):
        """
        Set figure center.

        :param center: Center list
        :type center: list
        :return:
        """
        self._center = center

    def intersect(self, figure):
        """
        Intersect figure with another figure.

        :param figure: Figure to intersect
        :type figure: CenteredFigure
        :return:
        """
        assert isinstance(figure, CenteredFigure), \
            'Figure must be CenteredFigure'

        p1 = Polygon(self.get_vertices())
        p2 = Polygon(figure.get_vertices())
        return p1.intersects(p2)

    def get_vertices(self):
        """
        Return tuple list of centered points.

        :return: List of tuples
        :rtype: list
        """

        # Get center
        cx = self._center[0]
        cy = self._center[1]

        # Return vertex list
        return [(u + cx, v + cy) for u, v in self._points]

    def draw(self):
        """
        Draw polygon figure to pygame surface.

        :return: None
        """
        if self._surface is not None:
            pygame.draw.polygon(self._surface, self._color, self.get_vertices(),
                                self._width)

    def scale(self, factor):
        """
        Scale the figure.
        
        :param factor: 
        :return: 
        """
        self._points = [(x * factor, y * factor) for x, y in self._points]
