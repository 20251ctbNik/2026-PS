# ========================================
# SISTEMA DE BIBLIOTECA
# ========================================
# Diciplina  : Programação de Sistemas (PS)
# Aula       : 05 - Revisão: Estruturas de Dados
# Autor      : Nickolas Kinceski Martins
# Data       : 03/03/2026
# Repositório: https://github.com/20251ctbNik/2026-PS
# ========================================
#
# DESCRIÇÃO:
# Catálogo de livros que demonstra o uso de listas
# e dicionários para armazenar, consultar e filtrar
# dados estruturados.

# ---- LISTAS: CONCEITO BÁSICO ----

# criando uma lista de títulos
titulos= [
    "O ProgrmadorPrágmatico",
    "Código limpo",
    "Entendendo Algoritmos",
]

# Acesso por indice (começa do 0, não em 1!)
print("Primeiro livro:", titulos[0])
print("ÚLTIMO livro:", titulos[-1]) # indice -1 = último elemento
print("Total de livros:", len(titulos))
