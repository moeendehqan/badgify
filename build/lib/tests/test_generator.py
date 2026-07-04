"""
Tests for Badgify - Dynamic Badge Generator
"""

import unittest
from badgify.generator import BadgeGenerator, BadgeStyle, ColorPalette


class TestBadgeGenerator(unittest.TestCase):
    """Test cases for BadgeGenerator class."""

    def test_init_default(self):
        """Test default initialization."""
        generator = BadgeGenerator()
        self.assertEqual(generator.style, BadgeStyle.FLAT)
        self.assertEqual(generator.color, ColorPalette.BLUE)
        self.assertEqual(generator.label_color, ColorPalette.GRAY)
        self.assertFalse(generator.rtl)

    def test_init_custom(self):
        """Test custom initialization."""
        generator = BadgeGenerator(
            style=BadgeStyle.FLAT_SQUARE,
            color=ColorPalette.GREEN,
            label_color=ColorPalette.BLACK,
            rtl=True,
        )
        self.assertEqual(generator.style, BadgeStyle.FLAT_SQUARE)
        self.assertEqual(generator.color, ColorPalette.GREEN)
        self.assertEqual(generator.label_color, ColorPalette.BLACK)
        self.assertTrue(generator.rtl)

    def test_generate_flat(self):
        """Test generating flat style badge."""
        generator = BadgeGenerator(style=BadgeStyle.FLAT)
        svg = generator.generate("build", "passing")
        
        self.assertIn("<svg", svg)
        self.assertIn("</svg>", svg)
        self.assertIn("build", svg)
        self.assertIn("passing", svg)
        self.assertIn('xmlns="http://www.w3.org/2000/svg"', svg)

    def test_generate_flat_square(self):
        """Test generating flat-square style badge."""
        generator = BadgeGenerator(style=BadgeStyle.FLAT_SQUARE)
        svg = generator.generate("license", "MIT")
        
        self.assertIn("<svg", svg)
        self.assertIn("license", svg)
        self.assertIn("MIT", svg)

    def test_generate_plastic(self):
        """Test generating plastic style badge."""
        generator = BadgeGenerator(style=BadgeStyle.PLASTIC)
        svg = generator.generate("coverage", "95%")
        
        self.assertIn("<svg", svg)
        self.assertIn("coverage", svg)
        self.assertIn("95%", svg)

    def test_generate_for_the_badge(self):
        """Test generating for-the-badge style badge."""
        generator = BadgeGenerator(style=BadgeStyle.FOR_THE_BADGE)
        svg = generator.generate("BUILD", "PASSING")
        
        self.assertIn("<svg", svg)
        # For the badge should uppercase text
        self.assertIn("BUILD", svg)
        self.assertIn("PASSING", svg)

    def test_generate_social(self):
        """Test generating social style badge."""
        generator = BadgeGenerator(style=BadgeStyle.SOCIAL)
        svg = generator.generate("github", "link")
        
        self.assertIn("<svg", svg)
        self.assertIn("github", svg)

    def test_generate_rtl(self):
        """Test generating RTL badge."""
        generator = BadgeGenerator(rtl=True)
        svg = generator.generate("نسخه", "1.0.0")
        
        self.assertIn("<svg", svg)
        self.assertIn("نسخه", svg)
        self.assertIn("1.0.0", svg)

    def test_generate_custom_colors(self):
        """Test generating badge with custom colors."""
        generator = BadgeGenerator()
        svg = generator.generate(
            "custom", 
            "badge",
            color="#ff0000",
            label_color="#00ff00"
        )
        
        self.assertIn("#ff0000", svg)
        self.assertIn("#00ff00", svg)

    def test_generate_with_preset_colors(self):
        """Test generating badge with preset color names."""
        generator = BadgeGenerator()
        svg = generator.generate(
            "status",
            "ok",
            color="brightgreen",
            label_color="gray"
        )
        
        self.assertIn(ColorPalette.BRIGHTGREEN, svg)
        self.assertIn(ColorPalette.GRAY, svg)

    def test_escape_xml(self):
        """Test XML escaping."""
        generator = BadgeGenerator()
        svg = generator.generate("test", "<>&\"'")
        
        self.assertIn("&lt;", svg)
        self.assertIn("&gt;", svg)
        self.assertIn("&amp;", svg)
        self.assertIn("&quot;", svg)
        self.assertIn("&apos;", svg)

    def test_color_resolution(self):
        """Test color name to hex resolution."""
        generator = BadgeGenerator()
        
        # Test preset color names
        self.assertEqual(generator._resolve_color("brightgreen"), "#4c1")
        self.assertEqual(generator._resolve_color("GREEN"), "#97ca00")
        self.assertEqual(generator._resolve_color("blue"), "#007ec6")
        
        # Test hex codes (should return as-is)
        self.assertEqual(generator._resolve_color("#ff0000"), "#ff0000")
        self.assertEqual(generator._resolve_color("#ABC123"), "#ABC123")

    def test_text_width_calculation(self):
        """Test text width calculation."""
        generator = BadgeGenerator()
        
        # Empty or short text should have minimum width
        self.assertGreaterEqual(generator._get_text_width(""), 10)
        self.assertGreaterEqual(generator._get_text_width("a"), 10)
        
        # Longer text should have proportional width
        width_short = generator._get_text_width("test")
        width_long = generator._get_text_width("this is a longer text")
        self.assertLess(width_short, width_long)

    def test_generate_html_img_tag(self):
        """Test HTML img tag generation."""
        generator = BadgeGenerator()
        img_tag = generator.generate_html_img_tag("build", "passing")
        
        self.assertIn("<img", img_tag)
        self.assertIn('src="/badge/?label=build&message=passing"', img_tag)
        self.assertIn('alt="build: passing"', img_tag)

    def test_generate_html_img_tag_with_params(self):
        """Test HTML img tag generation with additional parameters."""
        generator = BadgeGenerator()
        img_tag = generator.generate_html_img_tag(
            "build", 
            "passing",
            alt="Build Status",
            style="flat-square",
            color="green"
        )
        
        self.assertIn("<img", img_tag)
        self.assertIn('alt="Build Status"', img_tag)
        self.assertIn("style=flat-square", img_tag)
        self.assertIn("color=green", img_tag)


class TestBadgeStyle(unittest.TestCase):
    """Test cases for BadgeStyle enum."""

    def test_styles_exist(self):
        """Test that all expected styles exist."""
        self.assertEqual(BadgeStyle.FLAT.value, "flat")
        self.assertEqual(BadgeStyle.FLAT_SQUARE.value, "flat-square")
        self.assertEqual(BadgeStyle.PLASTIC.value, "plastic")
        self.assertEqual(BadgeStyle.FOR_THE_BADGE.value, "for-the-badge")
        self.assertEqual(BadgeStyle.SOCIAL.value, "social")


class TestColorPalette(unittest.TestCase):
    """Test cases for ColorPalette."""

    def test_common_colors(self):
        """Test that common colors are defined."""
        self.assertEqual(ColorPalette.BRIGHTGREEN, "#4c1")
        self.assertEqual(ColorPalette.GREEN, "#97ca00")
        self.assertEqual(ColorPalette.YELLOW, "#dfb317")
        self.assertEqual(ColorPalette.RED, "#e05d44")
        self.assertEqual(ColorPalette.BLUE, "#007ec6")
        self.assertEqual(ColorPalette.GRAY, "#9f9f9f")


if __name__ == "__main__":
    unittest.main()
