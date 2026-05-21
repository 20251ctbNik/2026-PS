import json
import os

PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
ARQUIVO_JSON = os.path.join(PASTA_ATUAL, "pets.json")


class Pet:
    def __init__(self, nome, especie, idade, peso, nome_dono, vacinado, hospedado=False):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.nome_dono = nome_dono
        self.vacinado = vacinado
        self.hospedado = hospedado

    def exibir_dados(self):
        print("\n--- Dados do Pet ---")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Peso: {self.peso:.2f} kg")
        print(f"Dono: {self.nome_dono}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        if self.hospedado:
            print(f"\n[Aviso] {self.nome} já está hospedado.")
        else:
            self.hospedado = True
            print(f"\n[Sucesso] {self.nome} entrou no hotel.")

    def registrar_saida(self):
        if not self.hospedado:
            print(f"\n[Aviso] {self.nome} não está hospedado.")
        else:
            self.hospedado = False
            print(f"\n[Sucesso] {self.nome} saiu do hotel.")

    def para_dicionario(self):
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "nome_dono": self.nome_dono,
            "vacinado": self.vacinado,
            "hospedado": self.hospedado
        }

    @staticmethod
    def criar_de_dicionario(dados):
        return Pet(
            dados["nome"],
            dados["especie"],
            dados["idade"],
            dados["peso"],
            dados["nome_dono"],
            dados["vacinado"],
            dados["hospedado"]
        )


# --- FUNÇÕES DE VALIDAÇÃO DE ENTRADA (SEGURANÇA) ---

def ler_inteiro(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, digite um número maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número inteiro.")

def ler_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))
            if valor < 0:
                print("Por favor, digite um número maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número decimal (ex: 12.5).")

def ler_string(mensagem):
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("Este campo não pode ficar vazio. Tente novamente.")
            continue
        return valor


# ---- SISTEMA DE BUSCA INTELIGENTE / AUTOCOMPLETAR ----

def selecionar_pet(lista_pets, mensagem_busca):
    """
    Busca pets por correspondência parcial (ex: digitar 'Li' encontra 'Luna' e 'Pipoca').
    Se achar apenas 1, seleciona direto (autocompletar).
    Se achar mais de um, cria um mini menu para escolha.
    """
    termo = ler_string(mensagem_busca).lower()
    encontrados = [pet for pet in lista_pets if termo in pet.nome.lower()]

    if not encontrados:
        print(f"\nNenhum pet encontrado com o termo '{termo}'.")
        return None

    # Cenário 1: Autocompleta se encontrar apenas um
    if len(encontrados) == 1:
        pet_escolhido = encontrados[0]
        print(f"\n[Sistema] Pet selecionado automaticamente: {pet_escolhido.nome} ({pet_escolhido.especie})")
        return pet_escolhido

    # Cenário 2: Múltiplas opções encontradas (cria um mini menu focado)
    print(f"\nForam encontrados {len(encontrados)} pets compatíveis:")
    for idx, pet in enumerate(encontrados, 1):
        print(f"{idx} - {pet.nome} ({pet.especie} | Dono: {pet.nome_dono})")

    while True:
        opcao = ler_inteiro(f"Escolha o número do pet desejado (1 a {len(encontrados)}): ")
        if 1 <= opcao <= len(encontrados):
            return encontrados[opcao - 1]
        print(f"Opção inválida! Digite um número entre 1 e {len(encontrados)}.")


# --- FUNÇÕES DE PERSISTÊNCIA ----

def salvar_pets(lista_pets):
    lista_dicionarios = []
    for pet in lista_pets:
        lista_dicionarios.append(pet.para_dicionario())

    try:
        with open(ARQUIVO_JSON, "w", encoding="utf-8") as arquivo:
            json.dump(lista_dicionarios, arquivo, ensure_ascii=False, indent=4)
        print("\nDados salvos com sucesso em pets.json!")
    except Exception as e:
        print(f"\nErro ao salvar o arquivo: {e}")


def carregar_pets():
    if not os.path.exists(ARQUIVO_JSON):
        return []

    try:
        with open(ARQUIVO_JSON, "r", encoding="utf-8") as arquivo:
            lista_dicionarios = json.load(arquivo)

        lista_pets = []
        for dados in lista_dicionarios:
            pet = Pet.criar_de_dicionario(dados)
            lista_pets.append(pet)
        return lista_pets
    except Exception as e:
        print(f"Erro ao carregar o arquivo pets.json: {e}")
        return []


# --- INTERFACES DO MENU --

def cadastrar_pet(lista_pets):
    print("\n--- Cadastro de Pet ---")
    nome = ler_string("Nome do pet: ")
    especie = ler_string("Espécie: ")
    idade = ler_inteiro("Idade: ")
    peso = ler_float("Peso (kg): ")
    nome_dono = ler_string("Nome do dono: ")

    resposta = input("O pet está vacinado? (s/n): ").strip().lower()
    vacinado = resposta == "s"

    pet = Pet(nome, especie, idade, peso, nome_dono, vacinado)
    lista_pets.append(pet)
    salvar_pets(lista_pets)  # Autosave por segurança
    print("Pet cadastrado com sucesso!")


def listar_pets(lista_pets):
    print("\n--- Lista de Pets ---")
    if not lista_pets:
        print("Nenhum pet cadastrado.")
        return

    for i, pet in enumerate(lista_pets, 1):
        print(f"\nID #{i}:")
        pet.exibir_dados()


def buscar_especifico(lista_pets):
    print("\n--- Buscar Pet ---")
    pet = selecionar_pet(lista_pets, "Digite o nome (ou parte do nome) do pet: ")
    if pet:
        pet.exibir_dados()


def menu():
    pets = carregar_pets()

    while True:
        print("\n========= HOTEL PARA PETS =========")
        print("1 - Cadastrar pet")
        print("2 - Listar todos os pets")
        print("3 - Registrar entrada (Check-in)")
        print("4 - Registrar saída (Check-out)")
        print("5 - Buscar pet por nome")
        print("6 - Salvar dados")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_pet(pets)

        elif opcao == "2":
            listar_pets(pets)

        elif opcao == "3":
            pet = selecionar_pet(pets, "Digite o nome (ou parte) para Check-in: ")
            if pet:
                pet.registrar_entrada()
                salvar_pets(pets)  # Grava a alteração de status no JSON

        elif opcao == "4":
            pet = selecionar_pet(pets, "Digite o nome (ou parte) para Check-out: ")
            if pet:
                pet.registrar_saida()
                salvar_pets(pets)  # Grava a alteração de status no JSON

        elif opcao == "5":
            buscar_especifico(pets)

        elif opcao == "6":
            salvar_pets(pets)

        elif opcao == "0":
            salvar_pets(pets)
            print("Sistema encerrado com segurança.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()