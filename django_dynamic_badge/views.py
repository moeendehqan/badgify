"""
Django Views for Dynamic Badge Generation

This module provides Django views that can be integrated into your Django project
to serve dynamic SVG badges.
"""

from django.http import HttpResponse, JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from .generator import BadgeGenerator, BadgeStyle, ColorPalette


@method_decorator(cache_page(60 * 5), name='dispatch')  # Cache for 5 minutes
class BadgeView(View):
    """
    Django view for generating dynamic badges.
    
    Query Parameters:
        - label: The label text (required)
        - message: The message text (required)
        - style: Badge style (flat, flat-square, plastic, for-the-badge, social)
        - color: Message background color (hex or preset name)
        - label_color: Label background color (hex or preset name)
        - rtl: Right-to-left text direction (true/false)
        - logo: Optional logo URL
        - format: Response format (svg, json) - default: svg
    
    Example Usage:
        /badge/?label=build&message=passing&style=flat&color=brightgreen
        /badge/?label=نسخه&message=1.0.0&rtl=true&color=blue
    """
    
    def get(self, request, *args, **kwargs):
        # Get parameters from request
        label = request.GET.get('label', 'label')
        message = request.GET.get('message', 'message')
        style_str = request.GET.get('style', 'flat').lower()
        color = request.GET.get('color', None)
        label_color = request.GET.get('label_color', None)
        rtl = request.GET.get('rtl', 'false').lower() == 'true'
        logo = request.GET.get('logo', None)
        output_format = request.GET.get('format', 'svg').lower()
        
        # Map style string to enum
        style_map = {
            'flat': BadgeStyle.FLAT,
            'flat-square': BadgeStyle.FLAT_SQUARE,
            'plastic': BadgeStyle.PLASTIC,
            'for-the-badge': BadgeStyle.FOR_THE_BADGE,
            'social': BadgeStyle.SOCIAL,
        }
        style = style_map.get(style_str, BadgeStyle.FLAT)
        
        # Create generator and generate badge
        generator = BadgeGenerator(
            style=style,
            color=color,
            label_color=label_color,
            rtl=rtl,
        )
        
        if output_format == 'json':
            # Return JSON with badge data
            svg_content = generator.generate(label, message, logo=logo)
            return JsonResponse({
                'label': label,
                'message': message,
                'style': style.value,
                'svg': svg_content,
                'color': color,
                'label_color': label_color,
                'rtl': rtl,
            })
        else:
            # Return SVG
            svg_content = generator.generate(label, message, logo=logo)
            response = HttpResponse(svg_content, content_type='image/svg+xml')
            response['Cache-Control'] = 'public, max-age=300'
            return response


@method_decorator(cache_page(60 * 15), name='dispatch')  # Cache for 15 minutes
class StaticBadgeView(View):
    """
    Simplified view for static badges with preset configurations.
    
    This is useful for common use cases like:
    - Version badges
    - License badges
    - Build status badges
    - Coverage badges
    
    URL Pattern: /badge/static/<category>/<value>/
    
    Example Usage:
        /badge/static/version/1.0.0/
        /badge/static/license/MIT/
        /badge/static/build/passing/
    """
    
    PRESETS = {
        'version': {'label': 'version', 'color': ColorPalette.BLUE},
        'license': {'label': 'license', 'color': ColorPalette.GREEN},
        'build': {'label': 'build', 'color': ColorPalette.BRIGHTGREEN},
        'coverage': {'label': 'coverage', 'color': ColorPalette.YELLOWGREEN},
        'status': {'label': 'status', 'color': ColorPalette.GRAY},
    }
    
    def get(self, request, category, value, *args, **kwargs):
        # Get preset configuration
        preset = self.PRESETS.get(category.lower(), self.PRESETS['status'])
        
        # Get optional parameters
        style_str = request.GET.get('style', 'flat').lower()
        rtl = request.GET.get('rtl', 'false').lower() == 'true'
        logo = request.GET.get('logo', None)
        
        # Map style string to enum
        style_map = {
            'flat': BadgeStyle.FLAT,
            'flat-square': BadgeStyle.FLAT_SQUARE,
            'plastic': BadgeStyle.PLASTIC,
            'for-the-badge': BadgeStyle.FOR_THE_BADGE,
            'social': BadgeStyle.SOCIAL,
        }
        style = style_map.get(style_str, BadgeStyle.FLAT)
        
        # Create generator and generate badge
        generator = BadgeGenerator(
            style=style,
            color=preset['color'],
            rtl=rtl,
        )
        
        svg_content = generator.generate(preset['label'], value, logo=logo)
        response = HttpResponse(svg_content, content_type='image/svg+xml')
        response['Cache-Control'] = 'public, max-age=900'
        return response


# Function-based view alternative
@cache_page(60 * 5)
def badge_view(request):
    """
    Function-based view for generating dynamic badges.
    
    This is an alternative to the class-based BadgeView.
    """
    from django.http import HttpResponse
    
    # Get parameters from request
    label = request.GET.get('label', 'label')
    message = request.GET.get('message', 'message')
    style_str = request.GET.get('style', 'flat').lower()
    color = request.GET.get('color', None)
    label_color = request.GET.get('label_color', None)
    rtl = request.GET.get('rtl', 'false').lower() == 'true'
    logo = request.GET.get('logo', None)
    
    # Map style string to enum
    style_map = {
        'flat': BadgeStyle.FLAT,
        'flat-square': BadgeStyle.FLAT_SQUARE,
        'plastic': BadgeStyle.PLASTIC,
        'for-the-badge': BadgeStyle.FOR_THE_BADGE,
        'social': BadgeStyle.SOCIAL,
    }
    style = style_map.get(style_str, BadgeStyle.FLAT)
    
    # Create generator and generate badge
    generator = BadgeGenerator(
        style=style,
        color=color,
        label_color=label_color,
        rtl=rtl,
    )
    
    svg_content = generator.generate(label, message, logo=logo)
    response = HttpResponse(svg_content, content_type='image/svg+xml')
    response['Cache-Control'] = 'public, max-age=300'
    return response
