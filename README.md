# Pygame toolbox
Toolbox for pygame, contains functions and classes to manipulate figures, points, sounds, etc.

| File | Description |
| :-: | :-- |
| **centered_figure.py** | Create figure with a (x,y) center. Detects collision, and prints into pygame surface. |

## Usage

- **centered_figure**

    ```python
    triangle = CenteredFigure([(0, 0), (0, 1), (0, 3)], [10, 10])
    square = CenteredFigure([(0, 0), (0, 1), (1, 1), (1, 0)], [10, 10])
    
    triangle.intersect(square) # True
    ```

## Licence
This project is licenced under GPLv3 (GNU General Public License, version 3) [https://www.gnu.org/licenses/gpl-3.0.html].

## Author
Author: Pablo Pizarro, 2017.<br>
