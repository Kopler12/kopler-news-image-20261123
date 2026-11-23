#!/usr/bin/env python3
"""Draw 'The World Today' front page for Monday 23 November 2026.

Renders a 1024x1024 newspaper front page with PIL, using only fonts
shipped with the system. All stories are real events reported on
23 November 2026 (see the README for sources).
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (18, 18, 18)
NAVY = (20, 33, 61)
RED = (178, 34, 34)
GOLD = (212, 175, 55)
GREY = (90, 88, 82)
RULE = (160, 155, 145)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines."""
    words = text.split()
    lines, cur = [], ""
    for word in words:
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_story(draw, x, y, w, kicker, headline, body, h_size, b_size,
               max_body_lines=3):
    """Draw one story block; returns the y just below it."""
    kf = font(SANS_B, 17)
    hf = font(SERIF_B, h_size)
    bf = font(SANS, b_size)
    draw.text((x, y), kicker, font=kf, fill=RED)
    y += 26
    for line in wrap(draw, headline, hf, w):
        draw.text((x, y), line, font=hf, fill=INK)
        y += h_size + 6
    y += 2
    for line in wrap(draw, body, bf, w)[:max_body_lines]:
        draw.text((x, y), line, font=bf, fill=(52, 52, 52))
        y += b_size + 5
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 44  # side margin

    # ---- Masthead -------------------------------------------------
    d.rectangle([0, 0, W, 148], fill=NAVY)
    title = "THE WORLD TODAY"
    tf = font(SERIF_B, 66)
    tw = d.textlength(title, font=tf)
    d.text(((W - tw) / 2, 18), title, font=tf, fill=(250, 248, 240))
    date = "MONDAY, 23 NOVEMBER 2026"
    df = font(SANS_B, 28)
    dw = d.textlength(date, font=df)
    d.text(((W - dw) / 2, 98), date, font=df, fill=GOLD)
    d.line([(mx, 164), (W - mx, 164)], fill=RULE, width=2)

    # ---- Lead story: COP31 ---------------------------------------
    y = 182
    y = draw_story(
        d, mx, y, W - 2 * mx,
        "CLIMATE  |  ANTALYA, TURKEY",
        "Climate talks collapse as deal drops fossil fuels",
        "COP31 ends with no agreement \u2014 the longest climate summit ever \u2014 "
        "after the final text omitted any mention of fossil fuels.",
        42, 22, max_body_lines=3)
    d.line([(mx, y + 8), (W - mx, y + 8)], fill=RULE, width=2)

    # ---- Six more stories in two columns -------------------------
    stories = [
        ("MIDDLE EAST  |  THE GULF",
         "Missiles hit US base in Bahrain as Gulf war widens",
         "Iran\u2019s Revolutionary Guard says it struck a US base in Bahrain; "
         "a Houthi missile aimed at Saudi Arabia was intercepted."),
        ("UKRAINE  |  KYIV REGION",
         "Drone strike leaves 14 missing in Kyiv region",
         "A Russian drone hit a residential building outside Kyiv, leaving at "
         "least 14 people missing, President Zelenskyy said."),
        ("ASIA  |  INDONESIA",
         "Factory fire in Banten leaves dozens missing",
         "At least three workers are dead and dozens unaccounted for after a "
         "candy factory blaze near Jakarta; the search resumes today."),
        ("UNITED NATIONS",
         "Nations agree to keep talking on lethal AI weapons",
         "Countries at the UN conference agree to continue negotiations on "
         "lethal autonomous weapons systems."),
        ("SOUTH KOREA  |  SEOUL",
         "Education minister quits over AI exam-cheating scandal",
         "South Korea\u2019s education minister resigns after AI-driven cheating "
         "in exams shook the country\u2019s schools."),
        ("SPORT  |  WELLINGTON",
         "India pile up a record 720 in Wellington Test",
         "India declare on 720 for 9 against New Zealand at the Basin Reserve "
         "\u2014 a record Test total."),
    ]
    col_w = (W - 2 * mx - 36) // 2
    row_y = y + 26
    row_h = 178
    for i, (kicker, headline, body) in enumerate(stories):
        cx = mx + (i % 2) * (col_w + 36)
        cy = row_y + (i // 2) * row_h
        draw_story(d, cx, cy, col_w, kicker, headline, body, 25, 18,
                   max_body_lines=3)
        if i % 2 == 0:
            d.line([(mx + col_w + 18, cy + 4),
                    (mx + col_w + 18, cy + row_h - 18)],
                   fill=RULE, width=1)

    # ---- Footer ---------------------------------------------------
    fy = H - 44
    d.line([(mx, fy - 10), (W - mx, fy - 10)], fill=RULE, width=2)
    foot = ("Sources: CNN, Reuters, Wall Street Journal, Associated Press, "
            "Le Monde  |  Events reported Monday 23 November 2026")
    ff = font(SANS, 15)
    fw = d.textlength(foot, font=ff)
    d.text(((W - fw) / 2, fy), foot, font=ff, fill=GREY)

    img.save("entry.png", "PNG", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
