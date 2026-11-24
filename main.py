import os
# One-liner entry: the line below is the whole submission.
LINE = "One star. He fills my bowl, then sits on MY chair and stares at a glowing box all day. I would give zero stars if the form allowed it."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
