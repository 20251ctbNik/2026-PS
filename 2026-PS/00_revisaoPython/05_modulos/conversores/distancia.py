# Conversores/distancia.py

def km_para_milhas(km):
    return km * 0.621371

# milhas para km
def milhas_para_km(milhas):
    return milhas * 1.60934

# metros para pés
def metros_para_pes(metros):
    return metros * 3.28084

if __name__== "__main__":
    print("Testando distância.py...")
    print(f"100km = {km_para_milhas(100)} mi (esperado: 62.1371)")
    print(f"15m  = {metros_para_pes(15)} pés (esperado: 49.2126)")
    print("OK")