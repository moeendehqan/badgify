"""
Badgify - A Django app for generating dynamic SVG badges

This package provides functionality to generate dynamic SVG badges similar to
shields.io, with support for customization including colors, styles, and RTL/LTR text.
"""

from django.apps import AppConfig


class BadgifyConfig(AppConfig):
    """App configuration for Badgify."""
    name = 'badgify'
    verbose_name = 'Badgify'
    default_auto_field = 'django.db.models.BigAutoField'
