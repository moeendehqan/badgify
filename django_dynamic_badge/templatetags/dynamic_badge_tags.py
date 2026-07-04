"""
Django Template Tags for Dynamic Badge Generation
"""

from django import template
from django.utils.safestring import mark_safe

from ..generator import BadgeGenerator, BadgeStyle

register = template.Library()


@register.simple_tag
def dynamic_badge(label, message, style='flat', color=None, label_color=None, rtl=False):
    """
    Generate a dynamic badge SVG inline in your template.
    
    Usage:
        {% load dynamic_badge_tags %}
        {% dynamic_badge "build" "passing" style="flat" color="brightgreen" %}
        {% dynamic_badge "نسخه" "1.0.0" rtl=True color="blue" %}
    
    Args:
        label: The label text
        message: The message text
        style: Badge style (flat, flat-square, plastic, for-the-badge, social)
        color: Message background color
        label_color: Label background color
        rtl: Right-to-left text direction
    
    Returns:
        SVG markup as safe HTML
    """
    # Map style string to enum
    style_map = {
        'flat': BadgeStyle.FLAT,
        'flat-square': BadgeStyle.FLAT_SQUARE,
        'plastic': BadgeStyle.PLASTIC,
        'for-the-badge': BadgeStyle.FOR_THE_BADGE,
        'social': BadgeStyle.SOCIAL,
    }
    badge_style = style_map.get(style.lower(), BadgeStyle.FLAT)
    
    generator = BadgeGenerator(
        style=badge_style,
        color=color,
        label_color=label_color,
        rtl=rtl,
    )
    
    svg = generator.generate(label, message)
    return mark_safe(svg)


@register.simple_tag
def badge_url(label, message, style='flat', color=None, label_color=None, rtl=False):
    """
    Generate a URL to a badge endpoint.
    
    Usage:
        {% load dynamic_badge_tags %}
        <img src="{% badge_url "build" "passing" %}" alt="Build Status">
    
    Args:
        label: The label text
        message: The message text
        style: Badge style
        color: Message background color
        label_color: Label background color
        rtl: Right-to-left text direction
    
    Returns:
        URL string with query parameters
    """
    from django.urls import reverse
    
    base_url = reverse('django_dynamic_badge:badge')
    
    # Build query string
    params = [f'label={label}', f'message={message}']
    
    if style and style != 'flat':
        params.append(f'style={style}')
    
    if color:
        params.append(f'color={color}')
    
    if label_color:
        params.append(f'label_color={label_color}')
    
    if rtl:
        params.append('rtl=true')
    
    return f"{base_url}?{'&'.join(params)}"
