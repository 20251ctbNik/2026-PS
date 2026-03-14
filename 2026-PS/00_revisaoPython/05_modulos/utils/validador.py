# função de validar o número
def validar_numero(valor_str, minimo=None,  maximo=None):
    # Validação e tratamento de erros
    try:
        valor = float(valor_str)
    except ValueError:
        return False, "Valor inválido: não é um número."
    
    if minimo is not None and valor < minimo:
        return False, f"Valor deve ser maior ou igual a {minimo}."
    
    if maximo is not None and valor > maximo:
        return False, f"Valor deve ser menor ou igual a {maximo}."
    
    return True, valor