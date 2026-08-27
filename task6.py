import subprocess
from datetime import datetime

today = datetime.now().strftime("%d-%m-%Y")
print(today)

time = datetime.now().strftime("%H:%M:%S")
print(time)

subprocess.run(["whoami"])
subprocess.run(["hostname"])
subprocess.run(["pwd"])
subprocess.run(["df","-h"])
subprocess.run(["uptime"])
