import psutil, time
from datetime import datetime

with open("cpu_log.txt", "a") as log:
    while True:
        uso = psutil.cpu_percent()
        log.write(f"{datetime.now()} - CPU: {uso}%\n")
        log.flush()
        time.sleep(5)
