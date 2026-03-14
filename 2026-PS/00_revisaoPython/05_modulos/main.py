# ====================================================
# SISTEMA DE CONVERSÃO DE UNIDADES
# ====================================================
# Diciplina  : Programação de Sistemas (PS)
# Aula       : 07 - Revisão: Módulos
# Autor      : Nickolas Kinceski Martins
# Data       : 12/03/2026
# Repositório: https://github.com/20251ctbNik/2026-PS
# ===================================================

# Importa funções da arquivo conversores
from conversores import (
    celsius_para_fahrenheit, celsius_para_kelvin, fahrenheit_para_celsius,
    km_para_milhas, milhas_para_km, metros_para_pes, kg_para_gramas, kg_para_libras, libras_para_kg
)
# Importa funções do arquive utils
from utils import cabecalho_secao, formatar_resultado, linha_separadora, validar_numero
# Função do menu de temperatura
def menu_temperatura():
    print(cabecalho_secao("Conversão de Temperatura"))

    # Para validar se a entrada  é valida
    entra = input("   Valor em °C: ")
    ok, valor = validar_numero(entra)
    if not ok:
        print(valor)
        return
    
    print(formatar_resultado("°C -> °F", valor, "°C", celsius_para_fahrenheit(valor), "°F"))
    print(formatar_resultado("°C -> K", valor, "°C", celsius_para_kelvin(valor), "K"))
    print(formatar_resultado("°F -> °C", valor, "°F", fahrenheit_para_celsius(valor), "°C"))

# Função do menu de distância
def menu_distancia():
    print(cabecalho_secao("Conversão de Distância"))
    entra = input("   Valor em km: ")

    # Para validar se a entrada  é valida
    ok, valor = validar_numero(entra)
    if not ok:
        print(valor)
        return
    
    print(formatar_resultado ("km -> mi", valor, "km", km_para_milhas(valor), "mi"))
    print(formatar_resultado("km -> pés", valor * 1000, "m", metros_para_pes(valor * 1000), "pés"))
    print(formatar_resultado("mi -> km", valor, "mi",  milhas_para_km(valor), "km"))

# Função do menu da maszsa
def menu_massa():
    print(cabecalho_secao("Conversão de Massa"))
    # Para validar se a entrada  é valida
    entra = input("   Valor em kg: ")
    ok, valor = validar_numero(entra)
    if not ok:
        print(valor)
        return          
        
    print(formatar_resultado("kg -> lb", valor, "kg", kg_para_libras(valor), "lb"))
    print(formatar_resultado("kg -> g", valor, "kg", kg_para_gramas(valor), "g"))
    print(formatar_resultado("lb -> kg", valor, "lb", libras_para_kg(valor), "kg"))

    
# Função principal(main)
def main():
    print(linha_separadora())
    print(" SISTEMA DE CONVERSÃO DE UNIDADES")
    print(linha_separadora())
# opções de escolha. Para o usúario calcular, temperatura, massa ou distância
    opcoes = {"1": menu_temperatura, "2": menu_distancia, "3": menu_massa}

    # De acordo com a entrada do usúario, ou encerra o programa ou continua com determinada função
    while True:
        print("\n [1] Temperatura  [2] Distância [3] Massa [0] Sair")
        escolha = input("   Opção: ").strip()
        if escolha == "0":
            print("\nSistema encerrado.")
            break
        elif escolha in opcoes:
            opcoes[escolha] ()
        else:
            print("     Opção inválida.")

#W Executa o main
if __name__ == "__main__":
    main()