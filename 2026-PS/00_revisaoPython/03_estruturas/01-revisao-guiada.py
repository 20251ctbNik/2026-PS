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

# ---- METODOS DE LISTA ----

print("\n--- Operações na lista ---")

# Adicionar um im=tem ao final
titulos.append("Python Fluente")
print("Após append:", titulos)

# Verificar se um item existe
busca = "Código Limpo"
if busca in titulos:
    print(f'"{busca}" está no catálogo.')
else:
    print(f'!{busca}" não encontrado.')

# Ordenar a lista
titulos.sort()
print("Lista ordenada:", titulos)

# Remover um item
titulos.remove("Entendendo Algoritmos")
print("Após remove:", titulos)
