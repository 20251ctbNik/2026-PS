#================================================
# SISTEMA DE APROVAÇÃO DE ALUNOS
#===============================================
# Diciplina  : Programação de Sistemas (PS)
# Aula       : 04 - Revisão: Variaveis, Tipos e Controle de Fluxo
# Autor      : Nickolas Kinceski Martins
# Data       : 24/02/2026
# Repositório: https://github.com/20251ctbNik/2026-PS
#================================================
#
# DESCRIÇÃO:
# Este progrema processa as notas de uma turma e determina
# a situação de cada aluno (Aprovado, Recuperação ou Reprovado).
# Conceitos utilizados: variáveis, tipos de dados, operadores
# estruturas de seleção e estruturas de repetição.
#================================================

# ---- ENTRADA DE DADOS ----

turma = [
    {"nome": "Ana", "nota1": 8.0, "nota2": 7.5},
    {"nome": "Bruno", "nota1": 4.5, "nota2": 5.0},
    {"nome": "Carla", "nota1": 2.0, "nota2": 3.5},  
]

print("=== Resultado da Turma ===")
print() # Linha em branco para melhor visualização
    
# O "for" percorre cada aluno da lista automaticamente.
for aluno in turma:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    media = (nota1 + nota2) / 2 

    # Determina a situação do aluno
    if media >= 6.0:                            # condição principal
        situacao = "Aprovado"     
    elif media >= 4.0:                          # condição alternativa (so verificada se a anterior for falsa)
        situacao = "Recuperação"
    else:                                       # caso nenhuma seja verdadeira
        situacao = "Reprovado"
        if media < 2.0:                          # condição aninhada (verificada somente se a condição anterior for verdadeira)
            situacao += " - Atenção: nota muito baixa em uma das avaliações." # concatenando string para adicionar mais informação à situação

    # Exibe o resultado do aluno
    print(f"Aluno    : {nome}")
    print(f"Média    : {media:.2f}")
    print(f"Situação : {situacao}")
    print("-" * 30)

# Pergunta se deseja processar outro aluno
continuar = "s"
while continuar == "s":
    print("\nDeseja processar outro aluno? (s/n): ", end="")
    continuar = input().lower()
    if continuar == "s":
        nome = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        media = (nota1 + nota2) / 2

        # Determina a situação do aluno
        if media >= 6.0:
            situacao = "Aprovado"
        elif media >= 4.0:
            situacao = "Recuperação"
        else:
            situacao = "Reprovado"
            if media < 2.0:
                situacao += " - Atenção: nota muito baixa em uma das avaliações."

        # Exibe o resultado do aluno
        print(f"\nAluno    : {nome}")
        print(f"Média    : {media:.2f}")
        print(f"Situação : {situacao}")
        print("-" * 30)
pass