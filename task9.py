import subprocess
import sys

process_name = sys.argv[1]

result = subprocess.run(
    ["pgrep","-x",process_name],
    capture_output=True,
    text = True
)

with open("report.txt","a") as report:

    if result.returncode == 0:
        report.write("Process is running")
        pid = result.stdout.strip();
        report.write(f"{pid}\n")
        
        cpu = subprocess.run(
                ["ps","-p",pid,"-o","%cpu"],
                capture_output=True,
                text=True
            )
        report.write(f"{cpu}\n")
        
        mem = subprocess.run(
                ["ps","p",pid,"-o","%mem"],
                capture_output=True,
                text = True
            )
        
        report.write(f"{mem}\n")

    else:
        report.write("Process is not running")





   


        