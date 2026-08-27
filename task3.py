from pathlib import Path

path = Path.home()/"Documents"

directories = [item for item in path.iterdir() if item.is_dir()]

sizes = []

for directory in directories:
    total_size = 0

    for item in directory.rglob("*"):
        #searches inside the directories recursively jaise * krta hai shell main
        if item.is_file():
            total_size+=item.stat().st_size

    sizes.append((total_size,directory))
    #just adding a tuple just see the ()

sizes.sort(reverse="True")

for size,directory in sizes[:12]:
    #just picking the top 12 directory sizes
    print(f"{size / 1024**2:.1f} MB {directory}")
