'''
==================================================
# Diciplina : Programação de Sistemas
# Autor     : Nickolas Kinceski Martins
# Data      : 2026-05-07
==================================================
'''
import os

class Pet:
    def __init__(self, nome, especie, idade, peso=0.0):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.check_in = False

def menu(pets):
    carregar_de_txt(pets)
    carregar_de_binario(pets)

    while True:
        print("\n============= Hotel Pet =============")
        print("1  - Cadastrar um Pet.")
        print("2  - Listar os Pets.")
        print("3  - salvar em .txt.")
        print("4  - Salvar em binário.")
        print("5  - Atualizar peso do pet.")
        print("6  - Check-in.")
        print("7  - Check-out.")
        print("8  - Buscar por pet.")
        print("9  - Relatório de pets hospedados.")
        print("10 - Resumo individual do pet.")
        print("11 - Sair.")
        print("====================================")
        opcao = input("Escolha uma opção: ")
        """Funcionalidades Menu"""

        if opcao == "1":
            cadastrar(pets)
        elif opcao == "2":
            listar_pet(pets)
        elif opcao == "3":
            salvarecarregar_em_txt(pets)
        elif opcao == "4":
            salvarecarregar_em_binario(pets)
        elif opcao == "5":
            atualizar_peso(pets)
        elif opcao == "6":
            registrar_entrada(pets)
        elif opcao == "7":
            registrar_saida(pets)
        elif opcao == "8":
            buscar_pet(pets)
        elif opcao == "9":
            relatorio_pets(pets)
        elif opcao == "10":
            resumo_individual(pets)
        elif opcao == "11":
            salvarecarregar_em_txt(pets)
            salvarecarregar_em_binario(pets)
            print("Saindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")

"""======================================= Funções ===================================================================="""

def cadastrar(pets):
    nome = input("Digite o nome do pet: ")
    especie = input("Digite a espécie do pet: ")
    idade = int(input("Digite a idade do pet (anos): "))
    peso = float(input("Digite o peso do pet (kg): "))
    pet = Pet(nome, especie, idade, peso)
    pets.append(pet)
    print(f"Pet '{nome}' cadastrado com sucesso!")

def listar_pet(pets):
    if not pets:
        print("Nenhum pet cadastrado.")
        return
    print("\nLista de Pets Cadastrados:")
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. Nome: {pet.nome}, Espécie: {pet.especie}, Idade: {pet.idade} anos")

def atualizar_peso(pets):
    nome = input("Digite o nome do pet para atualizar o peso: ")
    for pet in pets:
        if pet.nome == nome:
            novo_peso = float(input(f"Digite o novo peso para {pet.nome}: "))
            pet.peso = novo_peso
            print(f"Peso do pet '{pet.nome}' atualizado para {novo_peso} kg.")
            return
    print(f"Pet '{nome}' não encontrado.")

def registrar_entrada(pets):
    nome = input("Digite o nome do pet para check-in: ")
    for pet in pets:
        if pet.nome == nome:
            pet.check_in = True
            print(f"Pet '{pet.nome}' fez check-in com sucesso!")
            return
    print(f"Pet '{nome}' não encontrado.")

def registrar_saida(pets):
    nome = input("Digite o nome do pet para check-out: ")
    for pet in pets:
        if pet.nome == nome:
            pet.check_in = False
            print(f"Pet '{pet.nome}' fez check-out com sucesso!")
            return
    print(f"Pet '{nome}' não encontrado.")

def buscar_pet(pets):
    termo = input("Digite o nome (ou parte do nome) do pet: ").lower()
    encontrados = False

    print(f"\nResultados para '{termo}':")
    for pet in pets:
        if termo in pet.nome.lower():
            status = "Presente" if pet.check_in else "Saiu"
            print(f"- Nome: {pet.nome} | Espécie: {pet.especie} | Idade: {pet.idade} anos [{status}]")
            encontrados = True
    
    if not encontrados:
        print(f"Nenhum pet encontrado com o nome '{termo}'.")


def relatorio_pets(pets):
    hospedados = [pet for pet in pets if pet.check_in]
    if not hospedados:
        print("\nNenhum pet hospedado no momento.")
        return
    print("\nRelatório de Pets Hospedados:")
    for pet in hospedados:
        print(f"Nome: {pet.nome}, Espécie: {pet.especie}, Idade: {pet.idade} anos, Peso: {pet.peso} kg")
        
def resumo_individual(pets):
    nome = input("Digite o nome do pet para resumo individual: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            print(f"\n{'='*40}")
            print(f"Resumo do Pet '{pet.nome}'")
            print(f"{'='*40}")
            print(f"Espécie: {pet.especie}")
            print(f"Idade: {pet.idade} anos")
            print(f"Peso: {pet.peso} kg")
            status = "Hospedado" if pet.check_in else "Não hospedado"
            print(f"Status: {status}")
            print(f"{'='*40}\n")
            return
    print(f"Pet '{nome}' não encontrado.")

"""=======================Salvar em .txt e .binário==============================="""
def salvarecarregar_em_txt(pets):
    with open(os.path.join(os.path.dirname(__file__), "pets.txt"), "w") as file:
        for pet in pets:
            file.write(f"{pet.nome},{pet.especie},{pet.idade},{pet.peso},{pet.check_in}\n")
    print("Pets salvos em 'pets.txt' com sucesso!")

def carregar_de_txt(pets):
    filepath = os.path.join(os.path.dirname(__file__), "pets.txt")
    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for linha in file.readlines():
                    if linha.strip():
                        dados = linha.strip().split(",")
                        if len(dados) >= 3:
                            pet = Pet(dados[0], dados[1], int(dados[2]), float(dados[3]) if len(dados) > 3 else 0.0)
                            if len(dados) > 4:
                                pet.check_in = dados[4].lower() == "true"
                            pets.append(pet)
        except Exception as e:
            print(f"Erro ao carregar pets.txt: {e}")

def salvarecarregar_em_binario(pets):
    with open(os.path.join(os.path.dirname(__file__), "pets.bin"), "wb") as file:
        for pet in pets:
            file.write(f"{pet.nome},{pet.especie},{pet.idade},{pet.peso},{pet.check_in}\n".encode())
    print("Pets salvos em 'pets.bin' com sucesso!")

def carregar_de_binario(pets):
    filepath = os.path.join(os.path.dirname(__file__), "pets.bin")
    if os.path.exists(filepath):
        try:
            with open(filepath, "rb") as file:
                for linha in file.readlines():
                    if linha.strip():
                        dados = linha.decode().strip().split(",")
                        if len(dados) >= 3:
                            pet = Pet(dados[0], dados[1], int(dados[2]), float(dados[3]) if len(dados) > 3 else 0.0)
                            if len(dados) > 4:
                                pet.check_in = dados[4].lower() == "true"
                            if pet.nome not in [p.nome for p in pets]:
                                pets.append(pet)
        except Exception as e:
            print(f"Erro ao carregar pets.bin: {e}")

if __name__ == "__main__":
    pets = []
    menu(pets)