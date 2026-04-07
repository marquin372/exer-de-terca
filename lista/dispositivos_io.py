import psutil

print("Dispositivos de armazenamento:")
for part in psutil.disk_partitions():
    print(f"{part.device} - {part.mountpoint}")

# Comentário didático:
# Outros dispositivos de E/S incluem teclado, mouse, monitor, impressora etc.
