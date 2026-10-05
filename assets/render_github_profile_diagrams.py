#!/usr/bin/env python3
"""Render GitHub org profile diagram PNGs. Icons from website/public/brand/png/."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ASSETS = Path(__file__).resolve().parent
ICON_DIR = ASSETS.parents[2] / "website" / "public" / "brand" / "png"


def rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return tuple(int(h[i : i + 2], 16) for i in (0, 2, 4))


BG = rgb("#04070f")
SURFACE = rgb("#0b1122")
LINE = rgb("#2a3a63")
INK = rgb("#e8eefb")
MUTED = rgb("#94a0ba")
ACCENT = rgb("#3ce3ff")


def font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    for path in ("/System/Library/Fonts/Menlo.ttc", "/Library/Fonts/Menlo.ttf"):
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def load_icon(slug: str, size: int = 32) -> Image.Image:
    path = ICON_DIR / f"{slug}.png"
    if not path.exists():
        img = Image.new("RGBA", (size, size), (60, 227, 255, 80))
        return img
    icon = Image.open(path).convert("RGBA")
    icon.thumbnail((size, size), Image.Resampling.LANCZOS)
    out = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    ox = (size - icon.width) // 2
    oy = (size - icon.height) // 2
    out.paste(icon, (ox, oy), icon)
    return out


def paste_icon(base: Image.Image, slug: str, x: int, y: int, size: int = 28) -> None:
    icon = load_icon(slug, size)
    base.paste(icon, (x, y), icon)


def icon_box(
    draw: ImageDraw.ImageDraw,
    img: Image.Image,
    rect: tuple[int, int, int, int],
    title: str,
    lines: list[str],
    icon: str | None,
    ft,
    fb,
    accent: bool = False,
) -> None:
    x, y, w, h = rect
    draw.rounded_rectangle(
        (x, y, x + w, y + h),
        fill=SURFACE,
        outline=ACCENT if accent else LINE,
        width=1,
    )
    tx = x + 12
    if icon:
        paste_icon(img, icon, x + 8, y + 8, 30)
        tx = x + 46
    draw.text((tx, y + 10), title, fill=ACCENT, font=ft)
    for i, line in enumerate(lines):
        draw.text((tx, y + 28 + i * 14), line, fill=INK if i == 0 else MUTED, font=fb)


def render_platform() -> None:
    ft, fb = font(11), font(10)
    img = Image.new("RGB", (960, 460), BG)
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle((258, 28, 702, 340), radius=10, outline=LINE, width=1)
    draw.text((284, 44), "KUBERNETES CLUSTER", fill=INK, font=ft)
    for i, slug in enumerate(["kubernetes", "digitalocean", "aws", "googlecloud"]):
        paste_icon(img, slug, 284 + i * 34, 60, 26)

    icon_box(draw, img, (284, 90, 188, 66), "ARGO CD", ["gitops engine"], "argo", ft, fb)
    icon_box(draw, img, (488, 90, 188, 66), "TRAEFIK", ["ingress + TLS"], "traefikproxy", ft, fb)
    icon_box(draw, img, (284, 166, 188, 66), "EXT-SECRETS", ["Infisical sync"], "vault", ft, fb)
    icon_box(
        draw,
        img,
        (488, 166, 188, 66),
        "YOUR APPS",
        ["via app-starter"],
        "helm",
        ft,
        fb,
        accent=True,
    )
    icon_box(
        draw,
        img,
        (8, 128, 188, 108),
        "PIPELINES",
        ["GitHub Actions", "build · scan · sign"],
        "github",
        ft,
        fb,
    )
    icon_box(
        draw,
        img,
        (764, 58, 188, 108),
        "MONITORING",
        ["Grafana Cloud", "metrics · traces"],
        "grafana",
        ft,
        fb,
    )

    draw.rounded_rectangle((764, 228, 954, 338), radius=8, fill=SURFACE, outline=LINE)
    paste_icon(img, "trivy", 776, 240, 26)
    paste_icon(img, "falco", 808, 240, 26)
    draw.text((842, 252), "SECURITY", fill=ACCENT, font=ft)
    draw.text((776, 278), "Trivy · Falco · Cosign", fill=MUTED, font=fb)

    draw.rounded_rectangle((258, 366, 702, 438), radius=8, fill=SURFACE, outline=LINE)
    draw.text((272, 386), "INFRASTRUCTURE", fill=ACCENT, font=ft)
    draw.text((272, 404), "Terraform Cloud · multi-cloud", fill=MUTED, font=fb)
    for i, slug in enumerate(["terraform", "aws", "googlecloud", "cloudflare", "digitalocean"]):
        paste_icon(img, slug, 288 + i * 38, 410, 30)

    out = ASSETS / "github-profile-platform.png"
    img.save(out, optimize=True)
    print(f"wrote {out}")


def render_agents() -> None:
    ft, fb = font(11), font(10)
    img = Image.new("RGB", (920, 280), BG)
    draw = ImageDraw.Draw(img)
    draw.rounded_rectangle((168, 28, 688, 252), radius=10, outline=LINE, width=1)
    draw.text((184, 42), "KUBERNETES", fill=MUTED, font=fb)
    icon_box(draw, img, (20, 98, 142, 64), "SLACK", ["channel in"], None, ft, fb)
    icon_box(
        draw,
        img,
        (188, 68, 168, 144),
        "AGENT POD",
        ["Hermes gateway", "Agent worker"],
        "kubernetes",
        ft,
        fb,
        accent=True,
    )
    icon_box(draw, img, (388, 88, 198, 52), "GITHUB BROKER", ["repo credentials"], "github", ft, fb)
    icon_box(draw, img, (388, 154, 198, 52), "AGENT IDENTITY", ["OIDC · cloud"], "aws", ft, fb)
    icon_box(draw, img, (708, 88, 152, 52), "GITHUB", ["git · API"], "github", ft, fb)
    icon_box(draw, img, (708, 154, 152, 52), "CLOUD IAM", ["AWS · GCP"], "googlecloud", ft, fb)
    img.save(ASSETS / "github-profile-agents.png", optimize=True)
    print(f"wrote {ASSETS / 'github-profile-agents.png'}")


if __name__ == "__main__":
    render_platform()
    render_agents()
