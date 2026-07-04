"""
Badgify - Django URL Configuration for Dynamic Badge Generation

Include these URLs in your main urls.py:

    from django.urls import path, include
    
    urlpatterns = [
        # ... your other URLs
        path('badge/', include('badgify.urls')),
    ]
"""

from django.urls import path

from .views import BadgeView, StaticBadgeView, badge_view

app_name = 'badgify'

urlpatterns = [
    # Main badge endpoint (class-based view)
    path('', BadgeView.as_view(), name='badge'),
    
    # Alternative function-based view
    path('simple/', badge_view, name='badge_simple'),
    
    # Static preset badges
    path('static/<str:category>/<str:value>/', StaticBadgeView.as_view(), name='badge_static'),
]
