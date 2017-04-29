"""
Centered polygon figure, needs shapely and pygame.

Create figure with an (x,y) center, set color, thickness and surface to plot
(optional).

Usage:
    triangle = CenteredFigure([(0, 0), (0, 1), (0, 3)], [10, 10])
    square = CenteredFigure([(0, 0), (0, 1), (1, 1), (1, 0)], [10, 10])

    triangle.collide(square) -> true
    triangle.rotate(15) -> Rotate 15 grads Counterclockwise
    triangle.scale(10) -> Multiply 10 to all vertices position

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
from math import cos, sin, pi
from shapely.geometry import Polygon
import pygame


class CenteredFigure(object):
    def __init__(self, points, center, color=(255, 255, 255), width=0,
                 pygame_surface=None):
        """
        Create centered figure from point list with center (x,y).

        :param points: Clockwise vertices tuple list (ex. [(10,10),(10,5), ...])
        :type points: list
        :param center: Center list (ex [10, 10])
        :type center: list
        :param color: Tuple color
        :type color: tuple
        :param width: Border width (px)
        :param pygame_surface: Pygame surface object
        :type pygame_surface: pygame.display
        """
        assert self._assert_center(center), 'Center must be a list'
        assert isinstance(color, tuple), 'Color must be a tuple'
        assert self._assert_vertices(
            points), 'Vertices must be a list of tuples'
        self._points = points
        self._center = center
        self._color = color
        self._width = width
        self._surface = pygame_surface

    @staticmethod
    def _assert_center(center):
        """
        Check if center variable is correct.
        
        :param center: Center list
        :return: Boolean
        """
        if isinstance(center, list):
            if len(center) == 2:
                return True
        return False

    @staticmethod
    def _assert_vertices(vertices):
        """
        Check if vertices list only contain tuples
        
        :param vertices: Vertices list
        :return: 
        """
        if isinstance(vertices, list):
            for v in vertices:
                if not isinstance(v, tuple):
                    return False
            return True
        return False

    def collide(self, figure):
        """
        Check if figure collides with another figure.

        :param figure: Figure to check collision
        :type figure: CenteredFigure
        :return:
        """
        assert isinstance(figure, CenteredFigure), \
            'Figure must be CenteredFigure'

        p1 = Polygon(self.get_vertices())
        p2 = Polygon(figure.get_vertices())
        return p1.intersects(p2)

    def draw(self):
        """
        Draw polygon figure to pygame surface.

        :return: None
        """
        if self._surface is not None:
            pygame.draw.polygon(self._surface, self._color, self.get_vertices(),
                                self._width)

    def get_center(self):
        """
        Return center list (reference).
        
        :return: Center list
        :rtype: list
        """
        return self._center

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

    def rotate(self, angle):
        """
        Rotate vertices list (around center, which is mathematically [0,0])
        
        :param angle: Rotation angle, Counterclockwise (grad)
        :return: 
        """
        angle = - angle * pi / 180.0
        rotated_vertices = []
        for u, v in self._points:
            nu = u * cos(angle) - v * sin(angle)
            nv = v * cos(angle) + u * sin(angle)
            rotated_vertices.append((nu, nv))
        self._points = rotated_vertices

    def scale(self, factor):
        """
        Scale the figure.

        :param factor: 
        :return: 
        """
        self._points = [(x * factor, y * factor) for x, y in self._points]

    def set_center(self, center):
        """
        Set figure center.

        :param center: Center list
        :type center: list
        :return:
        """
        self._center = center

    def set_color(self, color):
        """
        Set figure color.

        :param color: Pygame color
        :return:
        """
        assert isinstance(color, tuple), 'Color must be a tuple'
        self._color = color

    def set_surface(self, surface):
        """
        Set pygame surface object.

        :param surface: Pygame display surface.
        :type surface: pygame.display
        :return:
        """
        self._surface = surface

    def set_vertices_points(self, points):
        """
        Set vertices points of figure.
        
        :param points: Clockwise vertices tuple list (ex. [(10,10),(10,5), ...])
        :type points: list
        :return: 
        """
        assert self._assert_vertices(
            points), 'Vertices must be a list of tuples'
        self._points = points
