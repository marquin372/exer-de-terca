import psutil

print(f"{'Partição':<20}{'Total (GB)':<15}{'Usado (GB)':<15}{'Livre (GB)':<15}{'% Usado':<10}")
for part in psutil.disk_partitions():
    uso = psutil.disk_usage(part.mountpoint)
    print(f"{part.mountpoint:<20}{uso.total/(1024**3):<15.2f}{uso.used/(1024**3):<15.2f}{uso.free/(1024**3):<15.2f}{uso.percent:<10.2f}")
