#!/usr/bin/env python3
"""
Generate a small, self-hosted "for-the-badge"-style single-segment SVG
badge (icon + label on one flat colored rectangle), matching the look of
the shields.io Tech Stack badges elsewhere in the README, but hosted
locally so it doesn't depend on shields.io's reliability.

Usage: python make_solid_badge_svg.py <icon> <label> <bg_color> <fg_color> <out.svg>
"""
import sys

FONT = "Verdana, Geneva, DejaVu Sans, sans-serif"
HEIGHT = 28
FONT_SIZE = 11
PAD = 14
ICON_GAP = 8
CHAR_W = 8.1
ICON_W = 16
RADIUS = 4


def text_width(s):
    return round(len(s) * CHAR_W)


def render(icon, label, bg, fg, out_path):
    label = label.upper()
    label_w = text_width(label)
    total_w = PAD + ICON_W + ICON_GAP + label_w + PAD

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{HEIGHT}" viewBox="0 0 {total_w} {HEIGHT}">
<rect width="{total_w}" height="{HEIGHT}" rx="{RADIUS}" fill="{bg}"/>
<text x="{PAD}" y="{HEIGHT/2 + 5}" font-size="14" fill="{fg}">{icon}</text>
<text x="{PAD + ICON_W + ICON_GAP}" y="{HEIGHT/2 + 4}" font-family="{FONT}" font-size="{FONT_SIZE}"
      font-weight="700" letter-spacing="0.6" fill="{fg}">{label}</text>
</svg>'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({total_w}x{HEIGHT})")


if __name__ == "__main__":
    _, icon, label, bg, fg, out_path = sys.argv
    render(icon, label, bg, fg, out_path)
