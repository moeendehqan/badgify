"""
Dynamic Badge Generator for Django/GitLab/GitHub
A Python package that generates dynamic SVG badges with customizable styles, colors, and RTL/LTR support.
"""

__version__ = "0.1.0"
__author__ = "Your Name"

from .generator import BadgeGenerator, BadgeStyle, ColorPalette

__all__ = ["BadgeGenerator", "BadgeStyle", "ColorPalette"]
