"""Program to draw Mandelbrot fractals: the main entry point.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: M.J. Moshiri
* TU/e ID number 1: 1524003
* Contributor 2: M.G.A. Fatah
* TU/e ID number 2: 1297546
* Date: ...
"""
import Image
from gui import GUI
import tkinter

# Don't execute this if file is imported
if __name__ == '__main__':
    gui = GUI()
    gui.show()
    # make_image(gui, color_mandel)
    tkinter.mainloop()
