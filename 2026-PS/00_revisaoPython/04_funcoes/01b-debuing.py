# Arquivo: 01b-debuing.py
# ATENÇÃO: 4 erros propositais. Encontre e corrija todos!

def saudacao(nome, turno="manhã"):
    mensagem = f"Bom {turno}, {nome}!"

saudacao("Ana")
print(saudacao("Bruno", "tarde"))

def dobrar(x):
    resultado = x * 2

print("Dobro de 5:", dobrar(5))

total = 0
def incrementar():
    total = total + 1
    
    
incrementar()
print("Total:", total)

def contagem(n):
    print(n)
    contagem(n - 1)

contagem(3)