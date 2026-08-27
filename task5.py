from pathlib import Path
import subprocess

directories = [ 
    "DECS,"
    "FML",
    "Software_lab",
    "Aglo and Complexity CS 601"
]

def calculate():
    for directory in directories:

        path = Path.home()/ "Documents" / "Mtech Courses"

        if(path.is_dir()):
            print("Directory exists")

            result = subprocess.run(
                ["find", str(path),"-type" ,"f"],
                capture_output=True,
                text=True
            )

            linesCount = len(result.stdout.splitlines())
            print(linesCount)

            subprocess.run(["du","-sh",str(path)])

            result = subprocess.run(["du","-sm",str(path)],
                                    capture_output=True,
                                    text = True)
            size = int(result.stdout.split()[0])

            if(size < 100):
                print("Small")

            elif(size < 1000):
                print("Medium")

            else:
                print("Larger than 1 GB")

        else:
            print("Directory doesn't exist")

calculate()