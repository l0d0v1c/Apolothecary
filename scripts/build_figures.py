#!/usr/bin/env python3
"""Generate the README figures as SVG files in assets/.

Standard library only. Run from the repository root:
    python3 scripts/build_figures.py
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"

FONT = "Georgia, 'Times New Roman', Times, serif"

# Palette: parchment and ink, plus pigments from the dictionary itself.
PARCH = "#F5EEE1"
INK = "#2A2420"
MUTED = "#6E6258"
RULE = "#D9CDB9"
BLUE = "#1F5FA8"     # Egyptian blue (M-03)
PURPLE = "#6B2D5C"   # Tyrian purple (O-04)
TERRA = "#9C4A1A"    # fired clay (P)
RED = "#A8432F"      # miltos (M-04)
OCHRE = "#C08A1E"    # orpiment (M-14)
VERD = "#3D7A5A"     # verdigris (M-13)
GREY = "#8C827A"

CERTAINTY = {"high": VERD, "medium": OCHRE, "low": RED, "unknown": GREY}


def svg(width, height, body, title):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{title}">\n'
        f"<title>{title}</title>\n{body}\n</svg>\n"
    )


def frame(width, height):
    return (
        f'<rect x="1" y="1" width="{width - 2}" height="{height - 2}" rx="18" '
        f'fill="{PARCH}" stroke="{RULE}" stroke-width="2"/>\n'
        f'<rect x="10" y="10" width="{width - 20}" height="{height - 20}" rx="12" '
        f'fill="none" stroke="{RULE}" stroke-width="1"/>\n'
    )


def text(x, y, s, size=16, fill=INK, anchor="start", weight="normal", style="normal",
         spacing=0):
    return (
        f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" fill="{fill}" '
        f'text-anchor="{anchor}" font-weight="{weight}" font-style="{style}" '
        f'letter-spacing="{spacing}">{s}</text>\n'
    )


# ---------------------------------------------------------------- icons

def icon_mineral(x, y, color, s=1.0):
    return (
        f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" '
        f'stroke-width="3" stroke-linejoin="round">'
        f'<polygon points="0,-28 22,-12 15,24 -15,24 -22,-12" fill="{color}" fill-opacity="0.15"/>'
        f'<polyline points="-22,-12 -7,-6 0,-28 7,-6 22,-12"/>'
        f'<polyline points="-7,-6 -15,24"/><polyline points="7,-6 15,24"/>'
        f'<line x1="-7" y1="-6" x2="7" y2="-6"/></g>\n'
    )


def icon_plant(x, y, color, s=1.0):
    return (
        f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" '
        f'stroke-width="3" stroke-linecap="round" stroke-linejoin="round">'
        f'<path d="M0,22 C-26,6 -20,-22 0,-30 C20,-22 26,6 0,22 Z" fill="{color}" fill-opacity="0.15"/>'
        f'<path d="M0,30 L0,-22"/><path d="M0,-4 L-10,-12"/><path d="M0,8 L11,0"/></g>\n'
    )


def icon_process(x, y, color, s=1.0):
    return (
        f'<g transform="translate({x},{y}) scale({s})" fill="none" stroke="{color}" '
        f'stroke-width="3" stroke-linejoin="round" stroke-linecap="round">'
        f'<path d="M-7,-28 L7,-28 M-5,-28 L-5,-8 L-23,24 L23,24 L5,-8 L5,-28" />'
        f'<path d="M-15,10 L15,10 L23,24 L-23,24 Z" fill="{color}" fill-opacity="0.3" stroke="none"/>'
        f'<path d="M-12,-14 q-6,-8 0,-14 M12,-16 q6,-8 0,-14" stroke-width="2.2"/></g>\n'
    )


ICONS = {"mineral": (icon_mineral, BLUE), "plant": (icon_plant, PURPLE),
         "process": (icon_process, TERRA)}


# ---------------------------------------------------------------- banner

def jar(x, y, color, label, lost=False):
    """An albarello (apothecary jar) whose base sits at y + 140."""
    if lost:
        style = f'fill="none" stroke="{INK}" stroke-width="2.5" stroke-dasharray="7 6"'
    else:
        style = f'fill="{color}" stroke="{INK}" stroke-width="2.5"'
    body = (
        f'<g transform="translate({x},{y})">'
        f'<circle cx="0" cy="-30" r="6" {style}/>'
        f'<rect x="-36" y="-24" width="72" height="14" rx="4" {style}/>'
        f'<rect x="-38" y="-10" width="76" height="10" rx="2" {style}/>'
        f'<path d="M-45,0 C-56,42 -38,84 -45,140 L45,140 C38,84 56,42 45,0 Z" {style}/>'
        f'<rect x="-34" y="46" width="68" height="38" rx="3" fill="{PARCH}" '
        f'stroke="{INK}" stroke-width="1.5"/>'
    )
    body += text(0, 70, label, size=14, anchor="middle", style="italic")
    if lost:
        body += text(0, 124, "?", size=30, fill=MUTED, anchor="middle")
    return body + "</g>\n"


def sparkle(x, y, r, color):
    return (
        f'<path transform="translate({x},{y}) scale({r / 10})" '
        f'd="M0,-10 Q0,0 10,0 Q0,0 0,10 Q0,0 -10,0 Q0,0 0,-10 Z" fill="{color}"/>\n'
    )


def banner():
    w, h = 1200, 360
    b = frame(w, h)
    b += text(70, 112, "A DICTIONARY OF LOST MATERIALS OF ANTIQUITY", size=15,
              fill=MUTED, spacing=2.5)
    b += text(66, 190, "The Apolothecary", size=68)
    b += f'<line x1="70" y1="218" x2="560" y2="218" stroke="{RULE}" stroke-width="2"/>\n'
    b += text(70, 256, "Using AI to recover what antiquity lost:", size=21, style="italic")
    b += text(70, 286, "the identity, the source and the recipe.", size=21, style="italic")
    # shelf
    b += f'<line x1="660" y1="292" x2="1140" y2="292" stroke="{INK}" stroke-width="4" stroke-linecap="round"/>\n'
    b += f'<line x1="680" y1="292" x2="680" y2="310" stroke="{INK}" stroke-width="4"/>\n'
    b += f'<line x1="1120" y1="292" x2="1120" y2="310" stroke="{INK}" stroke-width="4"/>\n'
    b += jar(725, 150, BLUE, "caeruleum")
    b += jar(840, 150, None, "σίλφιον", lost=True)
    b += jar(955, 150, RED, "μίλτος")
    b += jar(1070, 150, PURPLE, "purpura")
    # magnifying lens over the lost jar
    b += (f'<line x1="899" y1="133" x2="928" y2="162" stroke="{INK}" stroke-width="8" '
          f'stroke-linecap="round"/>\n'
          f'<circle cx="878" cy="112" r="30" fill="{PARCH}" fill-opacity="0.55" '
          f'stroke="{INK}" stroke-width="5"/>\n')
    b += sparkle(878, 112, 11, BLUE)
    b += sparkle(912, 76, 6, OCHRE)
    b += sparkle(846, 70, 4, OCHRE)
    return svg(w, h, b, "The Apolothecary: a dictionary of lost materials of antiquity")


# ---------------------------------------------------------------- what is lost

def venn():
    w, h = 1200, 740
    r = 200
    a, bb, c = (510, 320), (690, 320), (600, 476)
    b = frame(w, h)
    b += text(600, 58, "What is lost?", size=30, anchor="middle")
    b += text(600, 88, "A material is lost when at least one of three things is missing.",
              size=17, fill=MUTED, anchor="middle", style="italic")
    for (cx, cy), col in ((a, BLUE), (bb, OCHRE), (c, TERRA)):
        b += (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{col}" fill-opacity="0.10" '
              f'stroke="{col}" stroke-width="2.5"/>\n')
    b += text(300, 180, "Identity", size=26, fill=BLUE, anchor="end")
    b += text(300, 204, "what it was", size=16, fill=MUTED, anchor="end", style="italic")
    b += text(900, 180, "Source", size=26, fill=OCHRE)
    b += text(900, 204, "which deposit or workshop", size=16, fill=MUTED, style="italic")
    b += text(470, 650, "Recipe", size=26, fill=TERRA, anchor="end")
    b += text(470, 674, "how it was made or processed", size=16, fill=MUTED,
              anchor="end", style="italic")

    def region(x, y, items, size=15, step=6):
        out = ""
        for i, s in enumerate(items):
            code, _, name = s.partition(" ") if s[:2] in ("M-", "O-", "P-") else ("", "", s)
            out += (f'<text x="{x}" y="{y + i * (size + step)}" font-family="{FONT}" '
                    f'font-size="{size}" fill="{INK}" text-anchor="middle">'
                    f'<tspan font-weight="bold">{code}</tspan> {name}</text>\n')
        return out

    # Regions follow the "What is lost" field of each M and O entry.
    b += text(400, 300, "none", size=15, fill=MUTED, anchor="middle", style="italic")
    b += region(820, 300, ["M-10 natron"])
    b += region(600, 584, ["M-02 pozzolana", "M-03 Egyptian blue", "O-04 purple"])
    b += region(600, 186, ["M-04 miltos", "M-06 Samian", "M-11 cadmia", "M-14 sandaraca"],
                size=14, step=5)
    b += region(472, 418, ["M-05 Lemnian", "M-07 alum", "M-09 chrysocolla", "M-13 verdigris"],
                size=14, step=5)
    b += region(728, 430, ["M-12 electrum", "O-02 date"], size=14, step=5)
    b += region(600, 318, ["M-01 Cimolian", "M-08 misy", "M-15 asbestos", "M-16 Chian",
                           "O-01 silphium", "O-03 balsam"], size=14, step=5)
    b += text(1160, 716, "M and O entries placed by their “What is lost” field. Processes (P) "
              "are lost by their steps and parameters and are not shown.", size=13, fill=MUTED,
              anchor="end", style="italic")
    return svg(w, h, b, "What is lost: identity, source, recipe")


# ---------------------------------------------------------------- sections

def sections():
    w, h = 1200, 300
    cards = [
        ("mineral", "M", "Mineral materials", "16 entries",
         ["Earths, pigments, salts,", "alloys, binders."]),
        ("plant", "O", "Plant and animal materials", "4 entries",
         ["Plants, resins, dyes, foods,", "and their cultivated varieties."]),
        ("process", "P", "Methods and processes", "8 entries",
         ["Recipes, workshop operations,", "firing and transformation."]),
    ]
    b = ""
    for i, (kind, letter, title, count, desc) in enumerate(cards):
        fn, col = ICONS[kind]
        x = 15 + i * 395
        b += (f'<rect x="{x}" y="15" width="375" height="270" rx="16" fill="{PARCH}" '
              f'stroke="{RULE}" stroke-width="2"/>\n'
              f'<path d="M{x},31 a16,16 0 0 1 16,-16 h343 a16,16 0 0 1 16,16 v9 h-375 Z" '
              f'fill="{col}"/>\n')
        b += fn(x + 62, 112, col, 1.25)
        b += text(x + 330, 132, letter, size=64, fill=col, anchor="end")
        b += text(x + 30, 192, title, size=21)
        b += text(x + 30, 218, count, size=15, fill=col, weight="bold")
        for j, line in enumerate(desc):
            b += text(x + 30, 246 + j * 21, line, size=15, fill=MUTED, style="italic")
    return svg(w, h, b, "Three sections: M mineral, O plant and animal, P processes")


# ---------------------------------------------------------------- method

def method():
    w, h = 1200, 340
    steps = [
        ("Extract", ["every occurrence of a", "term in the digitised", "corpora"],
         "TLG · PHI · Perseus · ToposText", BLUE),
        ("Verify", ["each passage against", "the critical edition"],
         "to be confirmed → ✔", INK),
        ("Synthesise", ["the state of the art", "on identifications,", "quoting the authors"],
         None, INK),
        ("Test", ["low- and medium-", "certainty entries a", "laboratory can settle"],
         None, INK),
        ("Publish", ["the revised entries", "with their history"],
         "versioning", INK),
    ]
    b = frame(w, h)
    b += text(600, 54, "Method of work", size=28, anchor="middle")
    bw, gap, x0, y0, bh = 200, 32, 44, 84, 176
    for i, (title, lines, foot, col) in enumerate(steps):
        x = x0 + i * (bw + gap)
        stroke = BLUE if i == 0 else RULE
        b += (f'<rect x="{x}" y="{y0}" width="{bw}" height="{bh}" rx="12" fill="#FBF7EF" '
              f'stroke="{stroke}" stroke-width="{2.5 if i == 0 else 2}"/>\n')
        b += (f'<circle cx="{x + 30}" cy="{y0 + 32}" r="16" fill="{BLUE if i == 0 else INK}"/>\n')
        b += text(x + 30, y0 + 38, str(i + 1), size=17, fill=PARCH, anchor="middle",
                  weight="bold")
        b += text(x + 56, y0 + 39, title, size=21)
        if i == 0:
            b += (f'<rect x="{x + bw - 52}" y="{y0 + 18}" width="38" height="24" rx="12" '
                  f'fill="{BLUE}"/>\n')
            b += text(x + bw - 33, y0 + 35, "AI", size=14, fill=PARCH, anchor="middle",
                      weight="bold")
            b += sparkle(x + bw - 58, y0 + 16, 6, OCHRE)
        for j, line in enumerate(lines):
            b += text(x + 18, y0 + 76 + j * 21, line, size=15, fill=MUTED)
        if foot:
            b += (f'<line x1="{x + 18}" y1="{y0 + bh - 38}" x2="{x + bw - 18}" '
                  f'y2="{y0 + bh - 38}" stroke="{RULE}"/>\n')
            b += text(x + bw / 2, y0 + bh - 15, foot, size=13,
                      fill=BLUE if i == 0 else MUTED, anchor="middle", style="italic")
        if i < len(steps) - 1:
            ax = x + bw + 5
            b += (f'<path d="M{ax},{y0 + bh / 2} h{gap - 12} m-7,-6 l7,6 l-7,6" fill="none" '
                  f'stroke="{INK}" stroke-width="2.2" stroke-linecap="round" '
                  f'stroke-linejoin="round"/>\n')
    # feedback loop from step 5 back to step 1
    ly = y0 + bh + 34
    xs, xe = x0 + bw / 2, x0 + 4 * (bw + gap) + bw / 2
    b += (f'<path d="M{xe},{y0 + bh + 4} V{ly} H{xs} V{y0 + bh + 10}" fill="none" '
          f'stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 5"/>\n'
          f'<path d="M{xs - 6},{y0 + bh + 16} l6,-8 l6,8" fill="none" stroke="{MUTED}" '
          f'stroke-width="2" stroke-linejoin="round"/>\n')
    b += (f'<rect x="{600 - 205}" y="{ly - 13}" width="410" height="26" fill="{PARCH}"/>\n')
    b += text(600, ly + 5, "a living work: each project adds or corrects entries", size=15,
              fill=MUTED, anchor="middle", style="italic")
    return svg(w, h, b, "Method of work: extract, verify, synthesise, test, publish")


# ---------------------------------------------------------------- badges

def badge(level):
    label = level.capitalize()
    col = CERTAINTY[level]
    w = 16 + int(len(label) * 7.6)
    h = 20
    b = (f'<rect x="0.5" y="0.5" width="{w - 1}" height="{h - 1}" rx="9.5" fill="{col}"/>\n')
    b += text(w / 2, 14.5, label, size=12, fill="#FFFFFF", anchor="middle", weight="bold")
    return svg(w, h, b, f"Certainty: {label}")


def doi_badge(doi):
    left, right = "DOI", doi
    lw = 14 + int(len(left) * 8)
    rw = 14 + int(len(right) * 7.0)
    w, h = lw + rw, 20
    b = (f'<rect x="0" y="0" width="{w}" height="{h}" rx="4" fill="{BLUE}"/>\n'
         f'<rect x="0" y="0" width="{lw}" height="{h}" rx="4" fill="{INK}"/>\n'
         f'<rect x="{lw - 4}" y="0" width="4" height="{h}" fill="{INK}"/>\n')
    b += text(lw / 2, 14.5, left, size=12, fill="#FFFFFF", anchor="middle", weight="bold")
    b += text(lw + rw / 2, 14.5, right, size=12, fill="#FFFFFF", anchor="middle")
    return svg(w, h, b, f"DOI {doi}")


def icon_file(kind):
    fn, col = ICONS[kind]
    return svg(64, 64, fn(32, 32, col, 0.95), f"{kind} icon")


def main():
    (ASSETS / "badges").mkdir(parents=True, exist_ok=True)
    (ASSETS / "icons").mkdir(parents=True, exist_ok=True)
    files = {
        "banner.svg": banner(),
        "what-is-lost.svg": venn(),
        "sections.svg": sections(),
        "method.svg": method(),
    }
    for level in CERTAINTY:
        files[f"badges/{level}.svg"] = badge(level)
    files["badges/doi.svg"] = doi_badge("10.5281/zenodo.24422717")
    for kind in ICONS:
        files[f"icons/{kind}.svg"] = icon_file(kind)
    for name, content in files.items():
        (ASSETS / name).write_text(content, encoding="utf-8")
        print(f"wrote assets/{name} ({len(content)} bytes)")


if __name__ == "__main__":
    main()
