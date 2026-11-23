# The World Today — Monday, 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/Kopler12/kopler-news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/Kopler12/kopler-news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper front page summing up the world's news of Monday 23 November 2026, drawn programmatically with Python and Pillow.

## The image

`entry.png` (1024×1024) is a front page titled **"The World Today — Monday, 23 November 2026"**. Seven stories, each with a headline and one short factual line:

1. **Climate talks collapse** — COP31 in Antalya ends with no agreement, the longest climate summit ever, after the final text omitted any mention of fossil fuels.
2. **Gulf war widens** — Iran's Revolutionary Guard says it struck a US base in Bahrain; a Houthi missile aimed at Saudi Arabia was intercepted.
3. **Drone strike in Kyiv region** — A Russian drone hit a residential building outside Kyiv, leaving at least 14 people missing, President Zelenskyy said.
4. **Factory fire in Banten, Indonesia** — At least three workers dead and dozens unaccounted for after a candy factory blaze near Jakarta; the search resumes today.
5. **Lethal AI weapons** — Countries at the UN conference agree to continue negotiations on lethal autonomous weapons systems.
6. **South Korea minister quits** — The education minister resigns over an AI exam-cheating scandal.
7. **Cricket record** — India declare on 720 for 9 against New Zealand in the Wellington Test.

Sources: CNN, Reuters, Wall Street Journal, Associated Press, Le Monde. Every fact in the image was reported on 23 November 2026.

## How it runs

`main.py` (Python 3.13, standard library only) copies the bundled `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). It runs with no network and writes identical bytes on every run. `draw.py` is the script that rendered the front page.
