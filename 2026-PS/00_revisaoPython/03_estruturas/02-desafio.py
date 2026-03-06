# ========================================
# SISTEMA DE BIBLIOTECA
# ========================================
# Disciplina  : Programação de Sistemas (PS)
# Aula        : 05 - Revisão: Estruturas de Dados
# Autor       : Nickolas Kinceski Martins
# Data        : 05/03/2026
# Descrição   :
# Sistema de biblioteca que demonstra o uso
# de listas e dicionários para armazenar livros.
# Permite: consultar catálogo, cadastrar novos livros, buscar por autor,
# registrar empréstimos e devoluções e gera relatório final
# ========================================

# -------------------------------------------------------
# CATÁLOGO INICIAL (LISTA DE DICIONÁRIOS)
# ------------------------------------------------------------------

catalogo = [
    {
        "titulo": "O Programador Pragmático",
        "autor": "Andrew Hunt",
        "ano": 1999,
        "disponivel": True
    },
    {
        "titulo": "Código Limpo",
        "autor": "Robert C. Martin",
        "ano": 2008,
        "disponivel": False
    },
    {
        "titulo": "Entendendo Algoritmos",
        "autor": "Aditya Bhargava",
        "ano": 2016,
        "disponivel": True
    }
]


# ----------------------------------------------------------------------------------------------------
# FUNÇÃO PARA EXIBIR CATÁLOGO
# --------------------------------------------------------------------------------------

def mostrar_catalogo():
    print("\n=== CATÁLOGO DA BIBLIOTECA ===")

    for idx, livro in enumerate(catalogo, start=1):

        status = "Disponível" if livro["disponivel"] else "Emprestado"

        print(f"{idx}. {livro['titulo']} ({livro['ano']})")
        print(f"   Autor: {livro['autor']} | Status: {status}")
        print("-" * 40)


# ------------------------------------------------------------------------------------
# FUNÇÃO DE CADASTRAR NOVO LIVRO
# --------------------------------------------------------------------------------

def adicionar_livro():

    print("\n=== CADASTRAR NOVO LIVRO ===")

    titulo = input("Título: ")
    autor = input("Autor: ")
    # verificação de entrada válida.
    while True:
        try:
            ano = int(input("Ano de publicação: "))
            break
        except ValueError:
            print("Digite um ano válido (apenas números).")

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "disponivel": True
    }

    catalogo.append(novo_livro)

    print("\nLivro adicionado com sucesso!")


# ----------------------------------------------------------------------
# FUNÇÃO PARA BUSCA POR AUTOR
# --------------------------------------------------------------------------

def buscar_por_autor():

    print("\n=== BUSCAR POR AUTOR ===")

    busca = input("Digite o nome do autor: ").lower()

    encontrado = False

    for livro in catalogo:

        if busca in livro["autor"].lower():

            status = "Disponível" if livro["disponivel"] else "Emprestado"

            print(f"{livro['titulo']} - {livro['autor']} ({status})")

            encontrado = True

    if not encontrado:
        print("Nenhum livro encontrado para esse autor.")


# -------------------------------------------------------------------------------------------------
# FUNÇÃO DE EMPRÉSTIMO E DEVOLUÇÃO
# ------------------------------------------------------------------------------------------

def emprestimo_devolucao():

    print("\n=== EMPRÉSTIMO / DEVOLUÇÃO ===")

    busca = input("Digite o título do livro: ").lower()

    for livro in catalogo:

        if busca in livro["titulo"].lower():

            livro["disponivel"] = not livro["disponivel"]

            if livro["disponivel"]:
                print("Livro devolvido com sucesso.")
            else:
                print("Livro emprestado com sucesso.")

            return

    print("Livro não encontrado no catálogo.")


# ---------------------------------------------------------------
# RELATÓRIO FINAL
# -------------------------------------------------------------------------------

def relatorio_final():

    print("\n=== RELATÓRIO FINAL ===")

    total = len(catalogo)
    disponiveis = 0
    emprestados = 0

    for livro in catalogo:

        if livro["disponivel"]:
            disponiveis += 1
        else:
            emprestados += 1

    print(f"Total de livros: {total}")
    print(f"Disponíveis: {disponiveis}")
    print(f"Emprestados: {emprestados}")

    print("\nLivros emprestados:")

    for livro in catalogo:
        if not livro["disponivel"]:
            print(f"- {livro['titulo']}")


# ---------------------------------------------------------------------------------
# MENU PRINCIPAL DO SISTEMA
# ---------------------------------------------------------

while True:

    print("\n========= MENU =========")
    print("1 - Ver catálogo")
    print("2 - Cadastrar livro")
    print("3 - Buscar por autor")
    print("4 - Empréstimo / Devolução")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_catalogo()

    elif opcao == "2":
        adicionar_livro()

    elif opcao == "3":
        buscar_por_autor()

    elif opcao == "4":
        emprestimo_devolucao()

    elif opcao == "5":
        relatorio_final()
        print("\nEncerrando o sistema...")
        break

    else:
        print("Opção inválida.")