import psutil, platform
try:
    import cpuinfo
    modelo = cpuinfo.get_cpu_info()['brand_raw']
except:
    modelo = "Modelo não disponível"

print("Modelo:", modelo)
print("Núcleos físicos:", psutil.cpu_count(logical=False))
print("Núcleos lógicos:", psutil.cpu_count())
print("Frequência:", psutil.cpu_freq().current, "MHz")
print("Número de série: não disponível em sistemas portáveis")
