import subprocess
import sys

subprocess.run(["who"])

count = subprocess.run(
 ["who"],
 capture_output="True",
 text = True
)
result = len(count.stdout.splitlines())

with open("report.txt","a") as report:
    report.write(f"Number of currently logged in users {count}")

    username = sys.argv[1]

    logged_in  = any(
        line.startswith(username + " ")
        for line in count.stdout.splitlines()
    )

    if logged_in:
        report.write(f"{username} is currently logged in")
    else:
        report.write(f"{username} is not logged in")

with open("report.txt","a") as report:
    result = subprocess.run(
        ["last","-n","10"],
        capture_output=True,
        text = True
    )
    report.write(result.stdout)

with open("report.txt","a") as report:
    result = subprocess.run(
        ["last","-n","1"],
        capture_output=True,
        text = True
    )
    report.write(result.stdout)


