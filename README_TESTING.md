# راهنمای تست پکیج Badgify

## روش‌های مختلف تست

### ۱. اجرای تست‌های واحد (Unit Tests)

```bash
# با استفاده از unittest (پیش‌فرض پایتون)
python -m unittest discover tests -v

# یا مستقیم
python -m unittest tests.test_generator -v
```

**خروجی مورد انتظار:**
```
Ran 17 tests in 0.002s
OK
```

### ۲. اجرای اسکریپت نمونه

```bash
python test_example.py
```

این اسکریپت تمام قابلیت‌های پکیج را نشان می‌دهد:
- ساخت badge انگلیسی
- ساخت badge فارسی با RTL
- تمام ۵ استایل مختلف
- رنگ‌های preset
- تولید HTML img tag
- رنگ‌های سفارشی

### ۳. تست تعاملی در پایتون

```bash
python3
```

```python
from badgify.generator import BadgeGenerator, BadgeStyle

# مثال ساده
gen = BadgeGenerator(style=BadgeStyle.FLAT)
svg = gen.generate("Build", "Passing")
print(svg)

# مثال فارسی با RTL
gen_rtl = BadgeGenerator(rtl=True)
svg_rtl = gen_rtl.generate("وضعیت", "موفق")
print(svg_rtl)

# ذخیره SVG در فایل
with open("badge.svg", "w", encoding="utf-8") as f:
    f.write(svg_rtl)
```

### ۴. تست در پروژه جنگو

#### نصب در پروژه جنگو:

```bash
pip install -e .
```

#### اضافه کردن به settings.py:

```python
INSTALLED_APPS = [
    # ...
    'badgify',
]
```

#### اضافه کردن به urls.py:

```python
from django.urls import path, include

urlpatterns = [
    # ...
    path('badges/', include('badgify.urls')),
]
```

#### استفاده در تمپلت:

```html+django
{% load dynamic_badge_tags %}

<!-- روش ۱: استفاده از template tag -->
{% dynamic_badge "Version" "1.0.0" %}

<!-- روش ۲: استفاده از view -->
<img src="{% url 'badgify:badge' %}?label=Build&message=Passing&style=flat-square">
```

#### دسترسی مستقیم از طریق URL:

```
http://localhost:8000/badges/?label=Coverage&message=85%&color=brightgreen
http://localhost:8000/badges/?label=وضعیت&message=موفق&rtl=true&style=flat
```

## پارامترهای قابل تنظیم

### استایل‌ها:
- `flat` (پیش‌فرض)
- `flat-square`
- `plastic`
- `for-the-badge`
- `social`

### رنگ‌های preset:
- `BRIGHTGREEN`, `GREEN`, `YELLOW`, `YELLOWGREEN`
- `ORANGE`, `RED`, `BLUE`, `GRAY`
- `SUCCESS`, `IMPORTANT`, `CRITICAL`, `INFORMATIONAL`

### سایر پارامترها:
- `rtl=true/false` - برای پشتیبانی از زبان‌های راست‌چین
- `label_color` - رنگ بخش برچسب
- `color` - رنگ بخش پیام
- `logo` - URL لوگو (اختیاری)

## مثال‌های کاربردی

### Badge برای نسخه پروژه:
```
/badge/?label=Version&message=1.0.0&style=flat-square&color=blue
```

### Badge برای وضعیت بیلد:
```
/badge/?label=Build&message=Passing&color=brightgreen
```

### Badge فارسی برای Coverage:
```
/badge/?label=پوشش&message=85%&rtl=true&color=yellowgreen
```

### Badge برای لایسنس:
```
/badge/?label=License&message=MIT&color=blue
```
