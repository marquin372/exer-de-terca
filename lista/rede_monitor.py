import psutil, time

old = psutil.net_io_counters()
while True:
    time.sleep(1)
    new = psutil.net_io_counters()
    download = (new.bytes_recv - old.bytes_recv) / 1024
    upload = (new.bytes_sent - old.bytes_sent) / 1024
    print(f"Download: {download:.2f} kB/s | Upload: {upload:.2f} kB/s")
    old = new
