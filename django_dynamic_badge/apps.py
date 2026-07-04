"""
Django Dynamic Badge - A Django app for generating dynamic SVG badges

This package provides functionality to generate dynamic SVG badges similar to
shields.io, with support for customization including colors, styles, and RTL/LTR text.
"""

from django.apps import AppConfig


class DjangoDynamicBadgeConfig(AppConfig):
    """App configuration for Django Dynamic Badge."""
    name = 'django_dynamic_badge'
    verbose_name = 'Django Dynamic Badge'
    default_auto_field = 'django.db.models.BigAutoField'
