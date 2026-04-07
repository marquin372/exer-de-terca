import psutil, time

limite = float(input("Digite o limite de uso da RAM (%): "))

while True:
    mem = psutil.virtual_memory()
    print(f"Uso atual: {mem.percent}%")
    if mem.percent > limite:
        print("⚠ ALERTA: Uso de RAM acima do limite!")
    time.sleep(2)
