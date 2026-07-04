"""
Badge Generator Module

This module provides the core functionality for generating dynamic SVG badges
with customizable styles, colors, and RTL/LTR support.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional, Tuple


class BadgeStyle(Enum):
    """Predefined badge styles similar to shields.io"""
    FLAT = "flat"
    FLAT_SQUARE = "flat-square"
    PLASTIC = "plastic"
    FOR_THE_BADGE = "for-the-badge"
    SOCIAL = "social"


@dataclass
class ColorPalette:
    """Color palette for badges"""
    # Common colors
    BRIGHTGREEN = "#4c1"
    GREEN = "#97ca00"
    YELLOW = "#dfb317"
    YELLOWGREEN = "#a4a61d"
    ORANGE = "#fe7d37"
    RED = "#e05d44"
    BLUE = "#007ec6"
    GRAY = "#9f9f9f"
    LIGHTGRAY = "#9f9f9f"
    BLACK = "#000000"
    
    # Additional colors
    SUCCESS = "#4c1"
    IMPORTANT = "#c03829"
    CRITICAL = "#e05d44"
    INFORMATIONAL = "#007ec6"


class BadgeGenerator:
    """
    Generate dynamic SVG badges with customizable options.
    
    Features:
    - Custom label and message
    - Custom colors
    - Multiple predefined styles
    - RTL/LTR support
    - Django view integration ready
    """
    
    DEFAULT_WIDTH = 100
    DEFAULT_HEIGHT = 20
    FONT_SIZE = 11
    FONT_FAMILY = "DejaVu Sans,Verdana,Geneva,sans-serif"
    
    def __init__(
        self,
        style: BadgeStyle = BadgeStyle.FLAT,
        color: Optional[str] = None,
        label_color: Optional[str] = None,
        rtl: bool = False,
    ):
        """
        Initialize the badge generator.
        
        Args:
            style: The badge style (default: FLAT)
            color: Background color for the message part (hex code or preset name)
            label_color: Background color for the label part (hex code or preset name)
            rtl: Right-to-left text direction (default: False)
        """
        self.style = style
        self.color = self._resolve_color(color or ColorPalette.BLUE)
        self.label_color = self._resolve_color(label_color or ColorPalette.GRAY)
        self.rtl = rtl
    
    def _resolve_color(self, color: str) -> str:
        """Resolve color name to hex code if needed."""
        color_upper = color.upper()
        for attr_name in dir(ColorPalette):
            if attr_name.isupper():
                attr_value = getattr(ColorPalette, attr_name)
                if attr_name == color_upper or attr_value == color:
                    return attr_value
        # If it's already a hex code, return as is
        if color.startswith("#"):
            return color
        return color
    
    def _get_text_width(self, text: str) -> int:
        """Estimate text width in pixels (simplified calculation)."""
        # Approximate: average character width ~7px for 11px font
        return max(10, len(text) * 7 + 10)
    
    def _escape_xml(self, text: str) -> str:
        """Escape special XML characters."""
        replacements = {
            "&": "&amp;",
            "<": "&lt;",
            ">": "&gt;",
            '"': "&quot;",
            "'": "&apos;",
        }
        for char, escaped in replacements.items():
            text = text.replace(char, escaped)
        return text
    
    def generate(
        self,
        label: str,
        message: str,
        label_color: Optional[str] = None,
        color: Optional[str] = None,
        rtl: Optional[bool] = None,
        logo: Optional[str] = None,
        logo_width: int = 14,
    ) -> str:
        """
        Generate an SVG badge.
        
        Args:
            label: The label text (left side)
            message: The message text (right side)
            label_color: Override default label color
            color: Override default message color
            rtl: Override default RTL setting
            logo: Optional logo URL (not fully implemented in this version)
            logo_width: Width of the logo if present
            
        Returns:
            SVG string representation of the badge
        """
        # Resolve overrides
        msg_color = self._resolve_color(color) if color else self.color
        lbl_color = self._resolve_color(label_color) if label_color else self.label_color
        is_rtl = rtl if rtl is not None else self.rtl
        
        # Escape text
        label_escaped = self._escape_xml(label)
        message_escaped = self._escape_xml(message)
        
        # Calculate dimensions
        label_width = self._get_text_width(label)
        message_width = self._get_text_width(message)
        
        # Add logo space if present
        if logo:
            label_width += logo_width + 4
        
        total_width = label_width + message_width
        
        # Adjust height based on style
        if self.style == BadgeStyle.FOR_THE_BADGE:
            height = 28
            font_size = 10
            y_offset = 14
        else:
            height = 20
            font_size = 11
            y_offset = 10
        
        # Generate SVG based on style
        if self.style == BadgeStyle.FLAT:
            svg = self._generate_flat(
                label_escaped, message_escaped, label_width, message_width,
                total_width, height, font_size, y_offset, lbl_color, msg_color,
                is_rtl, logo, logo_width
            )
        elif self.style == BadgeStyle.FLAT_SQUARE:
            svg = self._generate_flat_square(
                label_escaped, message_escaped, label_width, message_width,
                total_width, height, font_size, y_offset, lbl_color, msg_color,
                is_rtl, logo, logo_width
            )
        elif self.style == BadgeStyle.PLASTIC:
            svg = self._generate_plastic(
                label_escaped, message_escaped, label_width, message_width,
                total_width, height, font_size, y_offset, lbl_color, msg_color,
                is_rtl, logo, logo_width
            )
        elif self.style == BadgeStyle.FOR_THE_BADGE:
            svg = self._generate_for_the_badge(
                label_escaped, message_escaped, label_width, message_width,
                total_width, height, font_size, y_offset, lbl_color, msg_color,
                is_rtl, logo, logo_width
            )
        else:  # SOCIAL
            svg = self._generate_social(
                label_escaped, message_escaped, label_width, message_width,
                total_width, height, font_size, y_offset, lbl_color, msg_color,
                is_rtl, logo, logo_width
            )
        
        return svg
    
    def _generate_flat(
        self, label: str, message: str, label_width: int, message_width: int,
        total_width: int, height: int, font_size: int, y_offset: int,
        label_color: str, message_color: str, rtl: bool, logo: Optional[str],
        logo_width: int
    ) -> str:
        """Generate flat style badge."""
        label_x = 6 if not rtl else total_width - label_width - 6
        message_x = label_width + 6 if not rtl else total_width - message_width - 6
        
        if rtl:
            label_x, message_x = message_x, label_x
        
        logo_svg = f'<image x="4" y="3" width="{logo_width}" height="{logo_width}" xlink:href="{logo}"/>' if logo else ""
        
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <linearGradient id="smooth" x2="0" y2="100%">
    <stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
    <stop offset="1" stop-opacity=".1"/>
  </linearGradient>
  <mask id="round"><rect width="{total_width}" height="{height}" rx="4" fill="#fff"/></mask>
  <g mask="url(#round)">
    <rect width="{label_width}" height="{height}" fill="{label_color}"/>
    <rect x="{label_width}" width="{message_width}" height="{height}" fill="{message_color}"/>
    <rect width="{total_width}" height="{height}" fill="url(#smooth)"/>
  </g>
  {logo_svg}
  <g fill="#fff" text-anchor="middle" font-family="{self.FONT_FAMILY}" font-size="{font_size}">
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{label}</text>
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset - 1}">{label}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{message}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset - 1}">{message}</text>
  </g>
</svg>'''
    
    def _generate_flat_square(
        self, label: str, message: str, label_width: int, message_width: int,
        total_width: int, height: int, font_size: int, y_offset: int,
        label_color: str, message_color: str, rtl: bool, logo: Optional[str],
        logo_width: int
    ) -> str:
        """Generate flat-square style badge."""
        label_x = 6 if not rtl else total_width - label_width - 6
        message_x = label_width + 6 if not rtl else total_width - message_width - 6
        
        if rtl:
            label_x, message_x = message_x, label_x
        
        logo_svg = f'<image x="4" y="3" width="{logo_width}" height="{logo_width}" xlink:href="{logo}"/>' if logo else ""
        
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <rect width="{total_width}" height="{height}" rx="0" fill="{label_color}"/>
  <rect x="{label_width}" width="{message_width}" height="{height}" fill="{message_color}"/>
  {logo_svg}
  <g fill="#fff" text-anchor="middle" font-family="{self.FONT_FAMILY}" font-size="{font_size}">
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset}">{label}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset}">{message}</text>
  </g>
</svg>'''
    
    def _generate_plastic(
        self, label: str, message: str, label_width: int, message_width: int,
        total_width: int, height: int, font_size: int, y_offset: int,
        label_color: str, message_color: str, rtl: bool, logo: Optional[str],
        logo_width: int
    ) -> str:
        """Generate plastic style badge."""
        label_x = 6 if not rtl else total_width - label_width - 6
        message_x = label_width + 6 if not rtl else total_width - message_width - 6
        
        if rtl:
            label_x, message_x = message_x, label_x
        
        logo_svg = f'<image x="4" y="3" width="{logo_width}" height="{logo_width}" xlink:href="{logo}"/>' if logo else ""
        
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <linearGradient id="linear" x2="0" y2="100%">
    <stop offset="0" stop-color="#fff" stop-opacity=".7"/>
    <stop offset=".1" stop-color="#fff" stop-opacity=".2"/>
    <stop offset=".3" stop-color="#fff" stop-opacity=".2"/>
    <stop offset=".9" stop-color="#fff" stop-opacity=".2"/>
    <stop offset="1" stop-color="#fff" stop-opacity=".5"/>
  </linearGradient>
  <mask id="round"><rect width="{total_width}" height="{height}" rx="4" fill="#fff"/></mask>
  <g mask="url(#round)">
    <rect width="{label_width}" height="{height}" fill="{label_color}"/>
    <rect x="{label_width}" width="{message_width}" height="{height}" fill="{message_color}"/>
    <rect width="{total_width}" height="{height}" fill="url(#linear)"/>
  </g>
  {logo_svg}
  <g fill="#fff" text-anchor="middle" font-family="{self.FONT_FAMILY}" font-size="{font_size}">
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{label}</text>
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset - 1}">{label}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{message}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset - 1}">{message}</text>
  </g>
</svg>'''
    
    def _generate_for_the_badge(
        self, label: str, message: str, label_width: int, message_width: int,
        total_width: int, height: int, font_size: int, y_offset: int,
        label_color: str, message_color: str, rtl: bool, logo: Optional[str],
        logo_width: int
    ) -> str:
        """Generate for-the-badge style badge."""
        label_x = 6 if not rtl else total_width - label_width - 6
        message_x = label_width + 6 if not rtl else total_width - message_width - 6
        
        if rtl:
            label_x, message_x = message_x, label_x
        
        logo_svg = f'<image x="4" y="7" width="{logo_width}" height="{logo_width}" xlink:href="{logo}"/>' if logo else ""
        
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <rect width="{label_width}" height="{height}" rx="0" fill="{label_color}"/>
  <rect x="{label_width}" width="{message_width}" height="{height}" fill="{message_color}"/>
  {logo_svg}
  <g fill="#fff" text-anchor="middle" font-family="{self.FONT_FAMILY}" font-size="{font_size}" font-weight="bold">
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{label.upper()}</text>
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset - 1}">{label.upper()}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset}" fill="#010101" fill-opacity=".3">{message.upper()}</text>
    <text x="{message_x + message_width // 2}" y="{y_offset - 1}">{message.upper()}</text>
  </g>
</svg>'''
    
    def _generate_social(
        self, label: str, message: str, label_width: int, message_width: int,
        total_width: int, height: int, font_size: int, y_offset: int,
        label_color: str, message_color: str, rtl: bool, logo: Optional[str],
        logo_width: int
    ) -> str:
        """Generate social style badge."""
        # Social style has rounded corners and different layout
        label_x = 6 if not rtl else total_width - label_width - 6
        message_x = label_width + 6 if not rtl else total_width - message_width - 6
        
        if rtl:
            label_x, message_x = message_x, label_x
        
        logo_svg = f'<image x="4" y="3" width="{logo_width}" height="{logo_width}" xlink:href="{logo}"/>' if logo else ""
        
        return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_width}" height="{height}" viewBox="0 0 {total_width} {height}">
  <rect width="{total_width}" height="{height}" rx="4" fill="{label_color}"/>
  <g fill="#fff" text-anchor="middle" font-family="{self.FONT_FAMILY}" font-size="{font_size}">
    <text x="{label_x + label_width // 2 if not rtl else label_x - label_width // 2}" y="{y_offset}">{label}</text>
  </g>
  {logo_svg}
</svg>'''
    
    def generate_html_img_tag(
        self,
        label: str,
        message: str,
        alt: Optional[str] = None,
        **kwargs
    ) -> str:
        """
        Generate an HTML img tag that references a Django view URL.
        
        This is useful for Django templates where you want to reference
        a view that generates the badge dynamically.
        
        Args:
            label: The label text
            message: The message text
            alt: Alt text for the image (default: f"{label}: {message}")
            **kwargs: Additional query parameters
            
        Returns:
            HTML img tag string
        """
        if alt is None:
            alt = f"{label}: {message}"
        
        # Build query string
        params = "&".join(f"{k}={v}" for k, v in kwargs.items())
        url = f"/badge/?label={label}&message={message}"
        if params:
            url += f"&{params}"
        
        return f'<img src="{url}" alt="{alt}" />'
