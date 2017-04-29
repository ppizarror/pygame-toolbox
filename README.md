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

    triangle.collide(square) # true
    triangle.rotate(15) # Rotate 15 grads Counterclockwise
    triangle.scale(10)  # Multiply 10 to all vertices position
    ```
    
## Requirements
<ul>
    <li><a href="https://pypi.python.org/pypi/Shapely">Shapely</a>
    <ul>
    <li>Windows users: Download <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs/#shapely">Shapely whl</a> and install it through pip.
    </li>
    <li>Linux users: <b>pip install shapely</b>
    <li>OSX users:</li>
    </ul>
    </li>
    <li>
    <a href="http://www.pygame.org/download.shtml">Pygame</a>
    </li>
</ul>

## Licence
This project is licenced under GPLv3 (GNU General Public License, version 3) [https://www.gnu.org/licenses/gpl-3.0.html].

## Author
Author: Pablo Pizarro, 2017<br>
