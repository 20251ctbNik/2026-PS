# Autor: Nickolas Kinceski Martins
# Arquivo: 01b-debuing.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"
    return mensagem  # Erro: a função não retornava para mensagem. A saudacao("Ana") não produzia saída

saudacao("Ana")
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2
    return resultado  # Erro: a função não retornava o resultado, então dobrar(5) retornava None

print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    global total  # Erro: a Variável global não estava declarada, causando um UnboundLocalError
    total = total + 1
    
    
incrementar()
print("Total:", total)

def contagem(n):
    if n > 0:  # Ero: Sem condição de parada, causando recursão infinita (RecursionError)
        print(n)
        contagem(n - 1)

contagem(3)