# Example Django Project Integration

This example shows how to integrate `django-dynamic-badge` into your Django project.

## 1. Install the package

```bash
pip install django-dynamic-badge
```

Or if developing locally:

```bash
cd /path/to/django-dynamic-badge
pip install -e .
```

## 2. Add to INSTALLED_APPS

In your `settings.py`:

```python
INSTALLED_APPS = [
    # ... your other apps
    'django_dynamic_badge',
]
```

## 3. Add URL configuration

In your main `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ... your other URLs
    path('badge/', include('django_dynamic_badge.urls')),
]
```

## 4. Usage Examples

### In Templates

```django
{% load dynamic_badge_tags %}

<!-- Inline SVG badge -->
<div class="badge-container">
    {% dynamic_badge "build" "passing" style="flat" color="brightgreen" %}
</div>

<!-- Badge as image source -->
<img src="{% badge_url "version" "1.0.0" style="flat-square" color="blue" %}" 
     alt="Version Badge">

<!-- RTL support for Persian/Arabic -->
{% dynamic_badge "نسخه" "1.0.0" rtl=True color="blue" %}

<!-- Custom colors -->
{% dynamic_badge "coverage" "95%" color="#4c1" label_color="#555" %}
```

### In Views

```python
from django.shortcuts import render
from django_dynamic_badge import BadgeGenerator, BadgeStyle, ColorPalette

def project_status(request):
    # Generate badges programmatically
    generator = BadgeGenerator(
        style=BadgeStyle.FLAT_SQUARE,
        color=ColorPalette.GREEN,
    )
    
    build_badge = generator.generate("build", "passing")
    coverage_badge = generator.generate("coverage", "95%", color="#4c1")
    
    return render(request, 'project.html', {
        'build_badge': build_badge,
        'coverage_badge': coverage_badge,
    })
```

### Direct URL Access

Once configured, you can access badges directly via URL:

```
# Basic badge
GET /badge/?label=build&message=passing

# With style and color
GET /badge/?label=tests&message=100%25&style=flat-square&color=brightgreen

# RTL (Persian)
GET /badge/?label=نسخه&message=1.0.0&rtl=true&color=blue

# JSON response
GET /badge/?label=build&message=passing&format=json

# Static preset endpoints
GET /badge/static/version/1.0.0/
GET /badge/static/license/MIT/
GET /badge/static/build/passing/
```

### In README files (GitLab/GitHub)

You can use the badge URLs in your README files:

```markdown
![Build Status](https://yourdomain.com/badge/?label=build&message=passing&color=brightgreen)
![Version](https://yourdomain.com/badge/?label=version&message=1.0.0&color=blue)
![License](https://yourdomain.com/badge/static/license/MIT/)
```

For RTL languages:

```markdown
![نسخه](https://yourdomain.com/badge/?label=نسخه&message=1.0.0&rtl=true&color=blue)
```

## 5. Advanced Configuration

### Custom Cache Settings

The badge views come with built-in caching. You can override the cache settings in your `settings.py`:

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```

### Custom Styling

You can create custom badge styles by extending the `BadgeGenerator` class:

```python
from django_dynamic_badge.generator import BadgeGenerator

class CustomBadgeGenerator(BadgeGenerator):
    def _generate_custom_style(self, label, message, *args, **kwargs):
        # Your custom SVG generation logic
        pass
```

## 6. Complete Example Project Structure

```
myproject/
├── manage.py
├── myproject/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── templates/
    └── project.html
```

**settings.py:**
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_dynamic_badge',
]
```

**urls.py:**
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('badge/', include('django_dynamic_badge.urls')),
]
```

**templates/project.html:**
```django
<!DOCTYPE html>
<html>
<head>
    <title>Project Status</title>
</head>
<body>
    <h1>Project Badges</h1>
    
    {% load dynamic_badge_tags %}
    
    <div class="badges">
        {% dynamic_badge "build" "passing" style="flat" color="brightgreen" %}
        {% dynamic_badge "tests" "100%" style="flat" color="brightgreen" %}
        {% dynamic_badge "coverage" "95%" style="flat" color="yellowgreen" %}
        {% dynamic_badge "license" "MIT" style="flat" color="blue" %}
    </div>
</body>
</html>
```

## 7. Running the Development Server

```bash
python manage.py runserver
```

Then visit:
- http://localhost:8000/badge/?label=build&message=passing
- http://localhost:8000/badge/static/version/1.0.0/
