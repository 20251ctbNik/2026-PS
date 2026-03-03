# Arquivi> 01b-debug.py
# ATENÇÃO: Este ódigo contém 4 erros propositais. Encontre e corrija todos!

nome = input("Digite o nome do alunos: ") # O erro é: o "input" estava com "m" no lugar do "n"
nota1 = float(input("Digite a nota1: ")) 
nota2 = float(input("Digite a nota2: "))

media = (nota1 + nota2) / 2 # O erro é: a media não tinha parenteses antes de "nota1" e depois de "nota2"

if media >= 6.0:
    situacao = "Aprovado"
elif media >= 4.0:
    situacao = "Recuperação"
else:                           # O erro é: o "else" estava com "tab" que não precisava
    situacao = "Reprovado"

print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}") # O erro é: o "print" estava como "pront"