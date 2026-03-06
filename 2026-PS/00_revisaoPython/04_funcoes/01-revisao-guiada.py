# =================================================
# SISTEMA DE CÁLCULO DE IMC
# =================================================
# Diciplina  : Programação de Sistemas (PS)
# Aula       : 06 - Revisão: Funções
# Autor      : Nickolas Kinceski Martins
# Data       : 03/03/2026
# Repositório: https:/github.com/20251ctbNik/2026-PS
# =================================================
#
# DESCRIÇÇAO:
# Calcula e classifica o IMC de uma pessoa.
# Demonstra definição de funções, poarâmetros,
# retorno, escopo e recursão.
# =================================================

# ---- FUNÇÃO SEM PARÂMETROS E SEM RETORNO ----

def exibir_cabecalho():
    print("=" * 40)
    print(" SISTEMA DE CÁLCULO DE IMC")
    print("=" * 40)

# Chamando a função
exibir_cabecalho()

# ---- FUNÇÃO COM PARÂMETROS E COM RETORNO ----

def calcular_imc(peso, altura):
    """Calcula e retorna o IMC. Fórmula: peso / altura^2"""
    imc = peso / (altura ** 2)      # ** é o operador de potência
    return imc                      # devolve o resultado para quem chamou

# Coletando dados do usuário
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

# Chamando a função e armazenando o retorno
resultado = calcular_imc(peso, altura)
print(f"Seu IMC é: {resultado:.2f}")

# ---- ESCOPO LOCAL vs. GLOBAL ----

versão = "1.0"      # Variável GLOBAL - existe fora de qualquer função

def demonstrar_escopo():
    mensagem = "Olá do interipr da função"   # variável LOCAL
    print("Dentro da função:")
    print(f"    mensagem: {mensagem}")          # OK: local existe aqui
    print(f"    versão global: {versão}")       # OK: global é visível dentro

demonstrar_escopo()

print("\nFora da função:")
print(f"    versão global = {versão}")       # OK: global existe aqui
# print(mensagem)                           # ERRO: variável local não existe aqui!

def mostrar_versao():
    print(f"Sistema IMC---versão 1.0: {versão}")

mostrar_versao()

# ==== VALOR PADRÃO E MÚLTIPLOS RETORNOS ====

def classificar_imc(imc, unidade="ka/m²"):
    """Classifica o IMC e retorna a classificação e a unidade usada."""
    if imc < 18.5:
        classificacao = "Abaixo do peso"
        emoji = "⚠️"
    elif imc < 25:
        classificacao = "Peso normal"
        emoji = "✅"
    elif imc < 30:
        classificacao = "Sobrepeso"
        emoji = "⚠️"
    else:
        classificacao = "Obesidade"
        emoji = "🚨"
    
    return classificacao, emoji         # retorna dois valores - Python empacota como tupla

# Chama sem o parâmetro opcional (usa o padrão "kg/m²")
imc_teste = 22.5
classificacao, emoji = classificar_imc(imc_teste)
print(f"IMC: {imc_teste} - Classificação: {classificacao} {emoji}")

# ==== RECURSÃO BÁSICA ====

def contagem_regressiva(n):
    """Exibe contagem regressiva de n até o usando recursão."""
    if n < 0:         # CASOP BASE: para a recursão
        return
    print(n)
    contagem_regressiva(n - 1)   # CHAMADA RECURSIVA: resolve problema menor

print("\n==== Contagem regressiva ====")
contagem_regressiva(5)

# Fatorial: exemplo9 clássico de recursão com retorno
def fatorial(n):
    """Calcula n! recursivamente. Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120"""
    if n == 0 or n == 1:        # caso base
        return 1
    return n * fatorial(n - 1)  # chamada recursivo

print("\n---- fatorial ----")
for i in range(1, 7):
    print(f"{i}! = {fatorial(i)}")

def soma_regressiva(n):
    """Calcula a soma de n até 1 usando recursão.

    Caso base: quando n <= 1, a soma é simplesmente n (1 + 0 ou 0).
    Caso recursivo: para n > 1, retorna n + soma_regressiva(n-1).
    """
    # caso base: parar a recursão quando n for 0 ou 1
    if n <= 1:
        return n
    # caso recursivo: soma o valor atual e delega o restante
    return n + soma_regressiva(n - 1)


# exemplo de uso da função corrigida
definir = None
print("\n---- soma regressiva ----")
for i in range(1, 6):
    print(f"soma_regressiva({i}) = {soma_regressiva(i)}")


# ==== FUNÇÃOP PRINCIPAL ====

def processar_pessoas():
    """Coleta dados, calcula IMC e exibe resultado completo."""
    nome = input("\nNome: ")
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))

    imc = calcular_imc(peso, altura)                # reutiliza funções já definidas
    classificacao, emoji = classificar_imc(imc)

    print("\n---- resultado ----")
    print(f"Nome         : {nome}")
    print(f"IMC          : {imc:.2f}")
    print(f"Classificação: {classificacao} {emoji}")

# ---- EXECUSÃO PRINCIPAL ----

exibir_cabecalho()

continuar = "s"
while continuar == "s":
    processar_pessoas()
    continuar = input("\nProcessar outra pessoa? (s/n): ").lower()
exibir_cabecalho()