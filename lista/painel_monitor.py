import psutil, time, os

while True:
    os.system("cls" if os.name == "nt" else "clear")
    mem = psutil.virtual_memory()
    cpu = psutil.cpu_percent()
    disco = psutil.disk_usage(psutil.disk_partitions()[0].mountpoint)
    net1 = psutil.net_io_counters()
    time.sleep(2)
    net2 = psutil.net_io_counters()
    download = (net2.bytes_recv - net1.bytes_recv) / 1024
    upload = (net2.bytes_sent - net1.bytes_sent) / 1024

    print(f"RAM: {mem.percent}% ({mem.used/(1024**2):.2f} MB usados)")
    print(f"CPU Total: {cpu}%")
    print(f"Disco Livre: {disco.free/(1024**3):.2f} GB ({100-disco.percent:.2f}%)")
    print(f"Rede: Download {download:.2f} kB/s | Upload {upload:.2f} kB/s")
