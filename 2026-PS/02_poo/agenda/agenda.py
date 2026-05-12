"""
agenda.py - Aula 23 (Programação de Sistemas, 2026)
Agenda de Contatos: classe inicial.
"""
import pickle


class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def exibir(self):
        print(f" Nome: {self.nome}")
        print(f" Telefone: {self.telefone}")
        print(f" Email: {self.email}")

    def para_linha_txt(self):
        return f"{self.nome};{self.telefone};{self.email}"


"""========================================================================="""
def salvar_em_txt(contatos, caminho):
    with open(caminho, "w", encoding="utf-8") as arquivo:
        for c in contatos:
            linha = c.para_linha_txt()
            arquivo.write(linha + "\n")
    print(f"{len(contatos)} contato(s) salvo(s) em '{caminho}'.")

def carregar_de_txt(caminho):
    contatos = []
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, telefone, email = linha.strip().split(";")
                contatos.append(Contato(nome, telefone, email))
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. começando vazio.")
    return contatos
"""========================================================================="""
def cadastrar(contatos):
    print("\n--- Novo Contato ---")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append(Contato(nome, telefone, email))
    print("Contato cadastrado com sucesso!")

def listar(contatos):
    if not contatos:
        print("\n(agenda vazia)")
        return
    print(f"\n--- Agenda ({len(contatos)} contatos) ---")
    for i, c in enumerate(contatos, start=1):
        print(f"\n[{i}]:")
        c.exibir()

def remover(contatos):
    listar(contatos)
    if not contatos:
        return
    indice = int(input("\nN° do contato a reover: ")) - 1
    if 0 <= indice < len(contatos):
        removido = contatos.pop(indice)
        print(f"Contato '{removido.nome}' removido.")
    else:
        print("Índice inválido.")


def salvar_em_binario(contatos, caminho):
    with open(caminho, "wb") as arquivo:
        pickle.dump(contatos, arquivo)
        print(f"{len(contatos)} contato(s) salvo(s) em '{caminho}'.")

def carregar_de_binario(caminho):
    try:
        with open(caminho, "rb") as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {caminho} ainda não existe. começando vazio.")
        return []

def menu():
    contatos = carregar_de_binario("agenda.bin")
    while True:
        print("\n====== AGENDA ======")
        print("1 - Cadastrar contato")
        print("2 - Listar contatos")
        print("3 - Remover contato")
        print("4 - Salvar contatos em .txt")
        print("5 - Salvar contatos em .bin")
        print("6 - Sair")
        opcao = input("Opção: ")

        if opcao == "1":
            contatos = []
            cadastrar(contatos)
        elif opcao == "2":
            listar(contatos)
        elif opcao == "3":
            remover(contatos)
        elif opcao == "4":
            salvar_em_txt(contatos, "contatos.txt")
        elif opcao == "5":
            salvar_em_binario(contatos, "contatos.bin")
        elif opcao == "6":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()