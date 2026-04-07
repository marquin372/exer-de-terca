import psutil

limite = 10  # porcentagem mínima de espaço livre
for part in psutil.disk_partitions():
    uso = psutil.disk_usage(part.mountpoint)
    livre_percent = 100 - uso.percent
    if livre_percent < limite:
        print(f"⚠ ALERTA: Pouco espaço em {part.mountpoint} - Livre: {livre_percent:.2f}%")
