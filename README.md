# Badgify

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/badge/python-3.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12-blue)](https://www.python.org/)
[![Django Versions](https://img.shields.io/badge/django-3.2%20|%204.0%20|%204.1%20|%204.2-green)](https://www.djangoproject.com/)

A Django app for generating dynamic SVG badges with customizable styles, colors, and RTL/LTR support. Similar to shields.io but self-hosted in your Django project.

## 🌟 Features

- **Multiple Styles**: Support for flat, flat-square, plastic, for-the-badge, and social styles
- **Custom Colors**: Choose from preset colors or use custom hex codes
- **RTL/LTR Support**: Full support for right-to-left languages like Persian, Arabic, Hebrew
- **Django Integration**: Easy integration with Django projects via views, URLs, and template tags
- **Cache Friendly**: Built-in caching for better performance
- **Logo Support**: Add logos to your badges
- **JSON Output**: Option to get badge data as JSON
- **Template Tags**: Ready-to-use Django template tags for easy integration

## 📦 Installation

### From PyPI (coming soon)

```bash
pip install badgify
```

### From Source

```bash
git clone https://github.com/moeendehqan/badgify.git
cd badgify
pip install -e .
```

## ⚙️ Configuration

Add the app to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    # ...
    'badgify',
]
```

Add the URL configuration to your main `urls.py`:

```python
from django.urls import path, include

urlpatterns = [
    # ...
    path('badge/', include('badgify.urls')),
]
```

## 🚀 Usage

### 1. As a Django View

Access badges via HTTP requests:

```
GET /badge/?label=build&message=passing&style=flat&color=brightgreen
GET /badge/?label=نسخه&message=1.0.0&rtl=true&color=blue
GET /badge/?label=license&message=MIT&style=flat-square&color=green
```

**Query Parameters:**
- `label` (required): The label text
- `message` (required): The message text
- `style`: Badge style (flat, flat-square, plastic, for-the-badge, social)
- `color`: Message background color (hex code or preset name)
- `label_color`: Label background color (hex code or preset name)
- `rtl`: Right-to-left text direction (true/false)
- `logo`: Optional logo URL
- `format`: Response format (svg, json)

### 2. In Django Templates

Load the template tags and use them in your templates:

```django
{% load dynamic_badge_tags %}

<!-- Inline SVG badge -->
{% dynamic_badge "build" "passing" style="flat" color="brightgreen" %}

<!-- Badge URL for img tag -->
<img src="{% badge_url "version" "1.0.0" style="flat-square" color="blue" %}" alt="Version">

<!-- RTL support for Persian/Arabic -->
{% dynamic_badge "نسخه" "1.0.0" rtl=True color="blue" %}
```

### 3. In Python Code

```python
from badgify import BadgeGenerator, BadgeStyle, ColorPalette

# Create a generator
generator = BadgeGenerator(
    style=BadgeStyle.FLAT,
    color=ColorPalette.GREEN,
    rtl=False,
)

# Generate SVG
svg = generator.generate("build", "passing")

# Or with custom colors
svg = generator.generate(
    "coverage", 
    "95%", 
    color="#4c1", 
    label_color="#555"
)

# Different styles
generator_flat_square = BadgeGenerator(style=BadgeStyle.FLAT_SQUARE)
svg = generator_flat_square.generate("license", "MIT", color="#97ca00")
```

## 🎨 Preset Colors

The following preset colors are available:

| Color Name | Hex Code | Alias |
|------------|----------|-------|
| `brightgreen` | #4c1 | `success` |
| `green` | #97ca00 | - |
| `yellow` | #dfb317 | - |
| `yellowgreen` | #a4a61d | - |
| `orange` | #fe7d37 | - |
| `red` | #e05d44 | `critical` |
| `blue` | #007ec6 | `informational` |
| `gray` | #9f9f9f | `lightgray` |
| `black` | #000000 | - |
| `important` | #c03829 | - |

You can also use any valid hex color code (e.g., `#ff0000`).

## 🎭 Badge Styles

1. **flat**: Default style with rounded corners and gradient overlay
2. **flat-square**: Square corners, no gradient
3. **plastic**: Rounded with glossy effect
4. **for-the-badge**: Larger, bold text for prominent display
5. **social**: Simplified style for social links

## 📝 Examples

### Basic Badge
```
/badge/?label=build&message=passing
```

### Colored Badge
```
/badge/?label=tests&message=100%25&color=brightgreen
```

### RTL Badge (Persian)
```
/badge/?label=نسخه&message=1.0.0&rtl=true&color=blue
```

### Custom Colors
```
/badge/?label=custom&message=badge&color=%23ff0000&label_color=%2300ff00
```

### For The Badge Style
```
/badge/?label=build&message=passing&style=for-the-badge&color=success
```

### JSON Response
```
/badge/?label=build&message=passing&format=json
```

## 🔗 Static Badge Endpoints

For common use cases, you can use the static badge endpoints:

```
GET /badge/static/version/1.0.0/
GET /badge/static/license/MIT/
GET /badge/static/build/passing/
GET /badge/static/coverage/95/
```

With optional query parameters:
```
GET /badge/static/version/1.0.0/?style=flat-square&rtl=true
```

## 🧪 Development

### Running Tests

```bash
python -m pytest tests/
```

### Building Package

```bash
python setup.py sdist bdist_wheel
```

### Publishing to PyPI

```bash
# Install twine if you haven't already
pip install twine

# Build the package
python setup.py sdist bdist_wheel

# Upload to TestPyPI (for testing)
twine upload --repository testpypi dist/*

# Upload to PyPI
twine upload dist/*
```

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details

## 👨‍💻 Author

**Moeen Dehqan**
- Email: moeen.dehqan@gmail.com
- GitHub: [@moeendehqan](https://github.com/moeendehqan)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- Inspired by [shields.io](https://shields.io/)
- Built for Django community
- Special thanks to all contributors

## 📞 Support

If you have any questions or need help, please open an issue on GitHub or contact me at moeen.dehqan@gmail.com
