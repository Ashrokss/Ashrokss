#!/usr/bin/env python3
"""
Generate a small, self-hosted "for-the-badge"-style two-segment SVG badge
(label | message), so critical links don't depend on shields.io's
reliability. Mimics shields.io's for-the-badge look: bold uppercase text,
flat segments, small rounded corners on the outer edges only.

Usage: python make_badge_svg.py <label> <message> <label_bg> <message_bg>
                                 <message_text_color> <out.svg>
"""
import sys

FONT = "Verdana, Geneva, DejaVu Sans, sans-serif"
HEIGHT = 28
FONT_SIZE = 11
PAD = 14
CHAR_W = 8.1  # rough bold-uppercase-at-11px width estimate, per character
RADIUS = 4


def text_width(s):
    return round(len(s) * CHAR_W)


def render(label, message, label_bg, message_bg, message_fg, out_path):
    label = label.upper()
    message = message.upper()

    label_w = text_width(label) + PAD * 2
    message_w = text_width(message) + PAD * 2
    total_w = label_w + message_w
    label_fg = "#ffffff"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{total_w}" height="{HEIGHT}" viewBox="0 0 {total_w} {HEIGHT}">
<clipPath id="round">
  <rect width="{total_w}" height="{HEIGHT}" rx="{RADIUS}" fill="#fff"/>
</clipPath>
<g clip-path="url(#round)">
  <rect width="{label_w}" height="{HEIGHT}" fill="{label_bg}"/>
  <rect x="{label_w}" width="{message_w}" height="{HEIGHT}" fill="{message_bg}"/>
</g>
<g fill="{label_fg}" text-anchor="middle" font-family="{FONT}" font-size="{FONT_SIZE}" font-weight="700" letter-spacing="0.6">
  <text x="{label_w/2}" y="{HEIGHT/2 + 4}">{label}</text>
</g>
<g fill="{message_fg}" text-anchor="middle" font-family="{FONT}" font-size="{FONT_SIZE}" font-weight="700" letter-spacing="0.6">
  <text x="{label_w + message_w/2}" y="{HEIGHT/2 + 4}">{message}</text>
</g>
</svg>'''
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"wrote {out_path} ({total_w}x{HEIGHT})")


if __name__ == "__main__":
    _, label, message, label_bg, message_bg, message_fg, out_path = sys.argv
    render(label, message, label_bg, message_bg, message_fg, out_path)
