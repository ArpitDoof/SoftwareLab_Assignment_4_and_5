from pathlib import Path
from collections import Counter

files = Path("..").rglob("*")

filenames = [file.name for file in files if file.is_file()]

counts = Counter(filenames)

for name in filenames:
    if counts[name ] > 1:
        print(name)


