def kg_para_libras(kg):
    """Converte Kg para Libras"""
    return kg * 2.2046

def kg_para_gramas(kg):
    """Comnverte Kg para Gramas"""
    return kg * 1000

def libras_para_kg(libras):
    """Converte Libras para Kg"""
    return libras * 0.45359237


if __name__== "__main__":
    print("Testando distância.py...")
    print(f"10kg = {kg_para_libras(10)} lb (esperado:  22.046)")
    print(f"15kg  = {kg_para_gramas(15)} g (esperado: 15.000)")
    print(f"20 lb = {libras_para_kg(20)} kg (esperado: 9.0718)")
    print("OK")