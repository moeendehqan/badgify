"""
Badgify - Dynamic Badge Generator for Django/GitLab/GitHub
A Python package that generates dynamic SVG badges with customizable styles, colors, and RTL/LTR support.

Author: Moeen Dehqan
Email: moeen.dehqan@gmail.com
"""

__version__ = "0.1.0"
__author__ = "Moeen Dehqan"
__email__ = "moeen.dehqan@gmail.com"

from .generator import BadgeGenerator, BadgeStyle, ColorPalette

__all__ = ["BadgeGenerator", "BadgeStyle", "ColorPalette"]
