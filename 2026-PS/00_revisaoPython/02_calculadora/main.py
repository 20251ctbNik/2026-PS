# Projeto: Calculadora Simples em Python
# Autor: Nickolas Kinceski Martins
# Data: 26/02/2026

import time
# importa as bibliotecas necessárias

def limpar_tela():
    #Limpa a tela
    print("\n" * 50)
    print("=" * 80)

def mostrar_menu(): 
    #lista as operaçoes disponiveis
    print("\n[Pressione o número correspondente à operação desejada]")
    print("1) Soma")
    print("2) Subtração")
    print("3) Multiplicação")
    print("4) Divisão")
    print("0) Sair")

def obter_numero(prompt):
    #Função que confere se a entrada é compativel
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Digite um número válido.")

def executar_operacao(op):
    #Pede os números e executa a operação escolhida
    a = obter_numero("Informe o primeiro número: ")
    b = obter_numero("Informe o segundo número: ")
    
    if op == "1":
        resultado = a + b
        simbolo = "+"
        nome = "Soma"
    elif op == "2":
        resultado = a - b
        simbolo = "-"
        nome = "Subtração"
    elif op == "3":
        resultado = a * b
        simbolo = "*"
        nome = "Multiplicação"
    elif op == "4":
        #Tratamente para a divisão por 0
        if b == 0:
            print("Erro: divisão por zero.")
            return
        resultado = a / b
        simbolo = "/"
        nome = "Divisão"
    else:
        print("Operação desconhecida.")
        return
        
    print(f"{nome}: {a} {simbolo} {b} = {resultado}")

def main():
    #fica nesse loop até o usuario escolher sair
    while True:
        limpar_tela()
        mostrar_menu()
        
        escolha = input("Escolha: ").strip()
        
        if escolha == "0":
            print("Encerrando...")
            time.sleep(0.5)
            break
            
        executar_operacao(escolha)
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()