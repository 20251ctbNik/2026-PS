# ===============================================================
# CABEÇALHO
# ===============================================================
# Autor    : Nickolas Kinceski Martins
# Data     : 05/06/2026
# Projeto  : Calculadora de Notas
# Repositório: https://github.com/20251ctbNik/2026-PS
# Descrição: Desenvolver uma calculadora que calcula as notas
# e a situação dos alunos, além de ser reutilizável
# ==============================================================

# Lista de outros 3 alunos
alunos = [
    {"aluno": "Cassandra", "nota1": "10", "nota2": "10"},
    {"aluno": "Julieta", "nota1": "6.5", "nota2": "8.2"},
    {"aluno": "Zeca Gado", "nota1": "0.1", "nota2": "0.9"},
]

print("\nSistema de cálculo das notas dos alunos IFPR.")

nome = input("Digite o nome do(a) aluno(a): ")

# Função para solicitar e validar notas
def solicitar_notas(nome_aluno):
    while True:
        try:
            nota1 = float(input("Primeira nota do(a) aluno(a): "))
            nota2 = float(input("Segunda nota do(a) aluno(a): "))

            if (nota1 < 0 or nota1 > 10) or (nota2 < 0 or nota2 > 10):
                print("Entrada inválida. Digite valores entre 0 e 10.")
                continue

            return nota1, nota2

        except ValueError:
            print("Entrada inválida, digite um número válido.")

nota1, nota2 = solicitar_notas(nome)

# Função para calcular a média
def calcular_media(n1, n2):
    return (n1 + n2) / 2

md = calcular_media(nota1, nota2)
print(f"A média do aluno(a) é: {md:.2f}")

# Função para verificar a situação
def verificar_situacao(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    else:
        return "Reprovado"

situacao = verificar_situacao(md)
print(f"Situação do(a) aluno(a) {nome}: {situacao}")

# Função de gerar relatório
def gerar_relatorio(nome, media, situacao):
    print("==== RELATÓRIO DO ALUNO ====")
    print(f"Nome do aluno(a)        : {nome}")
    print(f"Média do aluno(a)       : {media:.2f}")
    print(f"Situação do aluno(a)    : {situacao}")

print("\n==== RELATÓRIO GERAL DOS ALUNOS(AS) ====\n")

# Processa alunos da lista
for aluno in alunos:
    nome_aluno = aluno["aluno"]
    nota1 = float(aluno["nota1"])
    nota2 = float(aluno["nota2"])

    media = calcular_media(nota1, nota2)
    situacao_aluno = verificar_situacao(media)

    gerar_relatorio(nome_aluno, media, situacao_aluno)
    print()

# Função recursiva para média da turma
def calcular_media_turma(medias, tamanho=None):

    if tamanho is None:
        tamanho = len(medias)

    if len(medias) == 0:
        return 0

    if len(medias) == 1:
        return medias[0] / tamanho

    return medias[0] / tamanho + calcular_media_turma(medias[1:], tamanho)

medias_turma = []

for aluno in alunos:
    nota1 = float(aluno["nota1"])
    nota2 = float(aluno["nota2"])

    media = calcular_media(nota1, nota2)
    medias_turma.append(media)

media_geral = calcular_media_turma(medias_turma)

print(f"Média geral da turma: {media_geral:.2f}")

# Função resumo da turma
def resumo_turma(alunos):

    total_aprovados = 0
    total_recuperacao = 0
    total_reprovados = 0

    for aluno in alunos:

        nota1 = float(aluno["nota1"])
        nota2 = float(aluno["nota2"])

        media = calcular_media(nota1, nota2)
        situacao = verificar_situacao(media)

        if situacao == "Aprovado":
            total_aprovados += 1

        elif situacao == "Recuperação":
            total_recuperacao += 1

        else:
            total_reprovados += 1

    return total_aprovados, total_recuperacao, total_reprovados

# Chamando a função resumo
aprovados, recuperacao, reprovados = resumo_turma(alunos)

print("\n==== RELATÓRIO FINAL DA TURMA ====")
print(f"Média geral da turma : {media_geral:.2f}")
print(f"Total de aprovados   : {aprovados}")
print(f"Total em recuperação : {recuperacao}")
print(f"Total de reprovados  : {reprovados}")