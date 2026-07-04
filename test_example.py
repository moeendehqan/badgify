#!/usr/bin/env python3
"""
مثال عملی برای تست پکیج Badgify
این اسکریپت نحوه استفاده از پکیج را نشان می‌دهد
"""

from badgify.generator import BadgeGenerator, BadgeStyle

def main():
    print("=" * 60)
    print("تست پکیج Badgify")
    print("=" * 60)
    print()
    
    # مثال ۱: badge ساده انگلیسی
    print("۱. Badge ساده انگلیسی:")
    gen1 = BadgeGenerator(style=BadgeStyle.FLAT)
    svg1 = gen1.generate("Build", "Passing")
    print(f"   ✓ SVG تولید شد ({len(svg1)} کاراکتر)")
    print()
    
    # مثال ۲: badge فارسی با RTL
    print("۲. Badge فارسی (RTL):")
    gen2 = BadgeGenerator(style=BadgeStyle.FLAT, rtl=True)
    svg2 = gen2.generate("وضعیت", "موفق", label_color="#4CAF50", color="#2196F3")
    print(f"   ✓ SVG تولید شد ({len(svg2)} کاراکتر)")
    print()
    
    # مثال ۳: تمام استایل‌ها
    print("۳. تست تمام استایل‌ها:")
    styles = [
        (BadgeStyle.FLAT, "flat"),
        (BadgeStyle.FLAT_SQUARE, "flat-square"),
        (BadgeStyle.PLASTIC, "plastic"),
        (BadgeStyle.FOR_THE_BADGE, "for-the-badge"),
        (BadgeStyle.SOCIAL, "social"),
    ]
    for style, name in styles:
        gen = BadgeGenerator(style=style)
        svg = gen.generate("Test", "OK")
        print(f"   ✓ {name}: {len(svg)} کاراکتر")
    print()
    
    # مثال ۴: رنگ‌های preset
    print("۴. تست رنگ‌های preset:")
    colors = ["SUCCESS", "GREEN", "YELLOW", "ORANGE", "RED", "BLUE", "GRAY"]
    for color_name in colors:
        gen = BadgeGenerator()
        svg = gen.generate("Status", color_name, color=color_name)
        print(f"   ✓ {color_name}: {len(svg)} کاراکتر")
    print()
    
    # مثال ۵: HTML img tag
    print("۵. تولید HTML img tag:")
    gen_html = BadgeGenerator()
    img_tag = gen_html.generate_html_img_tag("Version", "1.0.0", style="flat-square")
    print(f"   {img_tag}")
    print()
    
    # مثال ۶: badge با رنگ سفارشی
    print("۶. Badge با رنگ سفارشی:")
    gen_custom = BadgeGenerator()
    svg_custom = gen_custom.generate(
        "Coverage", 
        "85%", 
        label_color="#e05d44", 
        color="#4c1"
    )
    print(f"   ✓ SVG تولید شد ({len(svg_custom)} کاراکتر)")
    print()
    
    print("=" * 60)
    print("✓ تمام تست‌ها با موفقیت انجام شدند!")
    print("=" * 60)

if __name__ == "__main__":
    main()
