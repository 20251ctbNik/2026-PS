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
    "O Progrmador Prágmatico",
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

# Percorrer lista com número de posição
print("\n--- Catálogo completo ---")
for idx, titulo in enumerate(titulos, start=1):
    print(f"{idx}. {titulo}")

# ---- DICIONÁRIOS: CONCEITO BÁSICO ----

# Um dicionário representa um livro com seus atributos
livro = {
    "titulo":       "O Programador Pragmático",
    "autor":        "Andrew Hunt",
    "ano":          1999,               # int, não string
    "disponivel": True,                 # bool
}

# Acessando valoes pelas chaves
print("titulo :", livro["titulo"])
print("autor  :", livro["autor"])
print("ano    :", livro["ano"])
print("status :", "disponivel" if livro["disponivel"] else "Emprestado")

# ---- MODIFICANDO E CONSULTANDO ----

# Atualizando um valor existente
livro["paginas"] = 352
print("Páginas:", livro["paginas"])

# .get() - acesso seguro: retorna None (ou padrão) se a chave não existir
editora = livro.get("editora", "Não informada")
print("Editora:", editora)      # não ança KeyError, retorna padrão
# ---- Cátalogo da Biblioteca ----

catalogo = [
    {"titulo": "O Programador Pragmático", "autor": "Andrew Hunt", "ano": 1999,
     "disponivel": True},
    {"titulo": "Código Limpo", "autor": "Robert C. Martin", "ano": 2008,
     "disponivel": False},
    {"titulo": "Entendendo Algoritmos", "autor": "Aditya Bhargava", "ano": 2016,
     "disponivel": True},
    {"titulo": "Manga Jujutsu kaisen Cap. 23", "autor": "Gege Akutami",  "ano": 2018,
     "disponivel": True}
]

print ("=== Catálogo da Biblioteca ===")
print ()

# Percorrendo cada livro com for (incluindo número)
for idx, livro in enumerate(catalogo, start=1):
    status = "Disponível" if livro["disponivel"] else "Emprestado"
    print (f'{idx}. {livro["titulo"]} ({livro["ano"]})')
    print (f'   Autor: {livro["autor"]} | {status}')
    print (" " + "-" * 40)

# ---- CONSULTAS E FILTROS ----

# Contadores de disponibilidade
print("\n=== Contagem de disponibilidade ===")
disponiveis = 0
emprestados = 0
for livro in catalogo:
    # incrementa o contador apropriado
    if livro["disponivel"]:
        disponiveis += 1
    else:
        emprestados += 1
print(f"Disponíveis: {disponiveis} | Emprestados: {emprestados}")

print("\n=== Livros disponíveis ===")
for livro in catalogo:
    if livro["disponivel"]:             # filtra apenas os disponíveis
        print(f' {livro["titulo"]}')

print("\n=== Busca por títulos ===")
busca = input("Digite o título (ou parte): ").lower()
encontrado = False
for livro in catalogo:
        if busca in livro["titulo"].lower():    # .lower() ignora maiúsculas/minúsculas
            print(f' Encontrado: {livro["titulo"]} - {livro["autor"]}')
            encontrado = True
if not encontrado:
     print(" Nenhum livro encontrado com esse termo.")

print("\n=== Atributos do primeiro livro ===")
for chave, valor in catalogo[0].items():    # .iems() retorna partes (chavem valor)
     print(f" {chave}: {valor}")
