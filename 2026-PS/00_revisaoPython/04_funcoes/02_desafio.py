# ===============================================================
# CABEÇALHO
# Autor    : Nickolas Kinceski Martins
# Data     : 05/06/2026
# Projeto  : Calculadora de Notas
# Descrição: Dsenvolver uma calculadora que calcula as notas
# e a situação dos alunos. além de ser reutilizavel
# ==============================================================

print("\nSistema de calculo de notas dos alunos IFPR.")

nome = int(input("Digite o nome do(a) aluno(a): "))
nota1 = float(input("Primeira nota do(a) aluno(a): "))
nota2 = float(input("Segunda nota do(a) aluno(a) : "))

# Função: Calcular a média
def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media

md = calcular_media(nota1, nota2)
print(f"A média do aluno(a) é: {md}")

def verificar_situacao(media):
    if media >= 6.0:
        resultado = "Aprovado"
    elif media >= 4.0 and media <= 5.9:
        resultado = "Recuperação"
    else:
        resultado = "Reprovado"
    return resultado