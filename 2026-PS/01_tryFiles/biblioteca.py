# ===================================================================
# Autor: Nickolas Kinceski Martins
# Data : 24/03/2026
# ===================================================================

from datetime import datetime

ARQUIVO = "biblioteca.txt"
SEPARADOR = "|"

def carregar_catalogo():
    catalogo = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(SEPARADOR)
                if len(partes) != 3:
                    continue
                titulo, autor, disponivel_str = partes
                catalogo.append({
                    "titulo": titulo,
                    "autor": autor,
                    "disponivel": disponivel_str == "True"
                })
    except FileNotFoundError:
        pass

    return catalogo


def salvar_catalogo(catalogo):
    try:
        with open(ARQUIVO, "w", encoding="utf-8") as f:
            for livro in catalogo:
                linha = f"{livro['titulo']}{SEPARADOR}{livro['autor']}{SEPARADOR}{livro['disponivel']}\n"
                f.write(linha)
        print(f"Catálogo salvo em '{ARQUIVO}'.")
    except IOError as e:
        print(f"Erro ao salvar: {e}")


def registrar_historico(acao, livro):
    try:
        with open("historico.txt", "a", encoding="utf-8") as f:
            data_hora = datetime.now().strftime("%d/%m/%Y %H:%M")
            linha = f"{data_hora} - {acao}: {livro['titulo']} ({livro['autor']})\n"
            f.write(linha)
    except IOError as e:
        print(f"Erro ao salvar histórico: {e}")


def listar_livros(catalogo):
    print("\n" + "=" * 50)
    print(" CATÁLOGO DA BIBLIOTECA")
    print("=" * 50)

    if not catalogo:
        print("   Nenhum livro cadastrado.")
        return
    
    for i, livro in enumerate(catalogo, 1):
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"    {i}. {livro['titulo']} - {livro['autor']} [{status}]")

    print("=" * 50)


def adicionar_livro(catalogo):
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()

    if not titulo or not autor:
        print("Título e autor são obrigatórios.")
        return

    # valida duplicata
    if any(l["titulo"].lower() == titulo.lower() for l in catalogo):
        print(" Livro já cadastrado.")
        return
    
    catalogo.append({
        "titulo": titulo,
        "autor": autor,
        "disponivel": True
    })

    print(f" '{titulo}' adicionado com sucesso!")
    salvar_catalogo(catalogo)


def buscar_livro(catalogo):
    print("\n=== Buscar Livro ===")
    termo = input("Digite parte do título: ").strip().lower()

    resultados = [l for l in catalogo if termo in l["titulo"].lower()]

    if not resultados:
        print("     Nenhum livro encontrado.")
        return
    
    print(f"\n {len(resultados)} resultado(s):")
    for livro in resultados:
        status = "Disponível" if livro["disponivel"] else "Emprestado"
        print(f"   {livro['titulo']} - {livro['autor']} [{status}]")


def registrar_emprestimo(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return

    print("\n=== Registrar Empréstimo ===")

    try:
        numero = int(input("Número do livro: "))

        if numero < 1 or numero > len(catalogo):
            print("Número fora do intervalo.")
            return

        livro = catalogo[numero - 1]

        if not livro["disponivel"]:
            print(f" '{livro['titulo']}' já está emprestado")
        else:
            livro["disponivel"] = False
            print(f" Empréstimo de '{livro['titulo']}' registrado.")

            registrar_historico("Empréstimo", livro)
            salvar_catalogo(catalogo)

    except ValueError:
        print(" Entrada inválida. Digite apenas o número.")


def devolver_livro(catalogo):
    listar_livros(catalogo)
    if not catalogo:
        return

    print("\n--- Registrar Devolução ---")

    try:
        numero = int(input("Número do livro a devolver: "))
        livro = catalogo[numero - 1]

        if livro["disponivel"]:
            print(f" '{livro['titulo']}' já está disponível.")
        else:
            livro["disponivel"] = True
            print(f" Devolução de '{livro['titulo']}' registrada")

            registrar_historico("Devolução", livro)
            salvar_catalogo(catalogo)

    except ValueError:
        print(" Digite apenas o número do livro.")
    except IndexError:
        print(" Número fora da lista.")


def ver_historico():
    print("\n=== HISTÓRICO ===")

    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            conteudo = f.read()

            if not conteudo.strip():
                print(" Nenhuma operação registrada.")
            else:
                print(conteudo)

    except FileNotFoundError:
        print(" Nenhum histórico encontrado.")


def relatorio_acervo(catalogo):
    print("\n=== RELATÓRIO DO ACERVO ===")

    total = len(catalogo)
    disponiveis = sum(1 for l in catalogo if l["disponivel"])
    emprestados = total - disponiveis

    print(f" Total de livros: {total}")
    print(f" Disponíveis: {disponiveis}")
    print(f" Emprestados: {emprestados}")

    try:
        with open("historico.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()

        emprestimos = {}

        for linha in linhas:
            if "Empréstimo" in linha:
                parte = linha.split("Empréstimo: ")[1]
                titulo = parte.split(" (")[0]
                emprestimos[titulo] = emprestimos.get(titulo, 0) + 1

        if emprestimos:
            mais_emprestado = max(emprestimos, key=emprestimos.get)
            qtd = emprestimos[mais_emprestado]
            print(f" Livro mais emprestado: {mais_emprestado} ({qtd} vezes)")
        else:
            print(" Nenhum empréstimo registrado ainda.")

    except FileNotFoundError:
        print(" Nenhum histórico encontrado.")


def menu():
    catalogo = carregar_catalogo()

    print("\nSISTEMA DE BIBLIOTECA -v3 (com persistência + histórico)")
    print(f" {len(catalogo)} livro(s) carregado(s) de '{ARQUIVO}'.")

    while True:
        print("\n Opções:")
        print("    [1] Listar livros")
        print("    [2] Adicionar livro")
        print("    [3] Buscar livro")
        print("    [4] Registrar empréstimo")
        print("    [5] Devolver livro")
        print("    [6] Ver histórico")
        print("    [7] Relatório do acervo")
        print("    [0] Sair")

        escolha = input("\n Sua escolha: ").strip()

        if escolha == "1":
            listar_livros(catalogo)
        elif escolha == "2":
            adicionar_livro(catalogo)
        elif escolha == "3":
            buscar_livro(catalogo)
        elif escolha == "4":
            registrar_emprestimo(catalogo)
        elif escolha == "5":
            devolver_livro(catalogo)
        elif escolha == "6":
            ver_historico()
        elif escolha == "7":
            relatorio_acervo(catalogo)
        elif escolha == "0":
            print("\n Até logo!")
            break
        else:
            print(" Opção inválida.")


if __name__ == "__main__":
    menu()