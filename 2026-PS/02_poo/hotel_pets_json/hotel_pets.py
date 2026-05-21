import os
import json

class Pet:
    def __init__(self, nome, especie, idade, peso=0.0, check_in=False):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.check_in = check_in

    def para_dicionario(self):
        """Requisito: Converte a instância do Pet em um dicionário para o JSON."""
        return {
            "nome": self.nome,
            "especie": self.especie,
            "idade": self.idade,
            "peso": self.peso,
            "check_in": self.check_in
        }

    @classmethod
    def de_dicionario(cls, dados):
        """Requisito: Reconstrói o objeto Pet a partir de um dicionário vindo do JSON."""
        return cls(
            nome=dados["nome"],
            especie=dados["especie"],
            idade=dados["idade"],
            peso=dados["peso"],
            check_in=dados["check_in"]
        )

# --- FUNÇÕES DE VALIDAÇÃO DE ENTRADA ---

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

# --- BUSCA INTELIGENTE COM AUTOCOMPLETAR ---

def selecionar_pet(pets, mensagem_busca):
    """Auxiliar: ajuda a encontrar o pet por correspondência parcial de nome."""
    termo = ler_string(mensagem_busca).lower()
    encontrados = [pet for pet in pets if termo in pet.nome.lower()]
    
    if not encontrados:
        print(f"Nenhum pet encontrado com o termo '{termo}'.")
        return None
        
    if len(encontrados) == 1:
        pet_escolhido = encontrados[0]
        print(f"[Sistema] Pet selecionado automaticamente: {pet_escolhido.nome} ({pet_escolhido.especie})")
        return pet_escolhido
        
    print(f"\nForam encontrados {len(encontrados)} pets para o termo '{termo}':")
    for idx, pet in enumerate(encontrados, start=1):
        print(f"{idx} - {pet.nome} ({pet.especie})")
        
    while True:
        opcao = ler_inteiro(f"Escolha o número do pet desejado (1 a {len(encontrados)}): ")
        if 1 <= opcao <= len(encontrados):
            return encontrados[opcao - 1]
        print(f"Opção inválida! Digite um número entre 1 e {len(encontrados)}.")

# --- MENU PRINCIPAL ---

def menu(pets):
    carregar_de_json(pets)

    while True:
        print("\n============= Hotel Pet =============")
        print("1  - Cadastrar um Pet.")
        print("2  - Listar os Pets.")
        print("3  - Calcular a diária do pet.")
        print("4  - Atualizar peso do pet.")
        print("5  - Check-in.")
        print("6  - Check-out.")
        print("7  - Buscar por pet.")
        print("8  - Relatório de pets hospedados.")
        print("9  - Resumo individual do pet.")
        print("10 - Sair.")
        print("====================================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(pets)
        elif opcao == "2":
            listar_pet(pets)
        elif opcao == "3":
            calcular_diaria(pets)
        elif opcao == "4":
            atualizar_peso(pets)
        elif opcao == "5":
            registrar_entrada(pets)
        elif opcao == "6":
            registrar_saida(pets)
        elif opcao == "7":
            buscar_pet(pets)
        elif opcao == "8":
            relatorio_pets(pets)
        elif opcao == "9":
            resumo_individual(pets)
        elif opcao == "10":
            salvar_em_json(pets)  
            print("Dados salvos com sucesso. Saindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente com um número de 1 a 10.")

"""======================================= Funções do Sistema ========================================================"""

def cadastrar(pets):
    print("\n--- Cadastro de Pet ---")
    nome = ler_string("Digite o nome do pet: ")
    especie = ler_string("Digite a espécie do pet: ")
    idade = ler_inteiro("Digite a idade do pet (anos): ")
    peso = ler_float("Digite o peso do pet (kg): ")
    
    pet = Pet(nome, especie, idade, peso)
    pets.append(pet)
    salvar_em_json(pets)
    print(f"\nPet '{nome}' cadastrado e salvo com sucesso!")

def listar_pet(pets):
    if not pets:
        print("\nNenhum pet cadastrado.")
        return
    print("\nLista de Pets Cadastrados:")
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. Nome: {pet.nome} | Espécie: {pet.especie} | Idade: {pet.idade} anos | Peso: {pet.peso:.2f} kg")

def atualizar_peso(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) do pet para atualizar o peso: ")
    if pet:
        novo_peso = ler_float(f"Digite o novo peso para {pet.nome} (kg): ")
        pet.peso = novo_peso
        salvar_em_json(pets)
        print(f"Peso do pet '{pet.nome}' atualizado para {novo_peso:.2f} kg.")

def registrar_entrada(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) do pet para check-in: ")
    if pet:
        if pet.check_in:
            print(f"O pet '{pet.nome}' já está hospedado.")
            return
        pet.check_in = True
        salvar_em_json(pets)
        print(f"Pet '{pet.nome}' fez check-in com sucesso!")

def registrar_saida(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) do pet para check-out: ")
    if pet:
        if not pet.check_in:
            print(f"O pet '{pet.nome}' não está hospedado no momento.")
            return
        pet.check_in = False
        salvar_em_json(pets)
        print(f"Pet '{pet.nome}' fez check-out com sucesso!")

def buscar_pet(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) para buscar: ")
    if pet:
        status = "Presente" if pet.check_in else "Saiu/Não hospedado"
        print(f"\nResultados da Busca:")
        print(f"- Nome: {pet.nome} | Espécie: {pet.especie} | Idade: {pet.idade} anos | Peso: {pet.peso:.2f} kg [{status}]")

def relatorio_pets(pets):
    hospedados = [pet for pet in pets if pet.check_in]
    if not hospedados:
        print("\nNenhum pet hospedado no momento.")
        return
    print("\nRelatório de Pets Hospedados:")
    for pet in hospedados:
        print(f"Nome: {pet.nome}, Espécie: {pet.especie}, Idade: {pet.idade} anos, Peso: {pet.peso:.2f} kg")
        
def resumo_individual(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) do pet para resumo individual: ")
    if pet:
        print(f"\n{'='*40}")
        print(f"Resumo do Pet '{pet.nome}'")
        print(f"{'='*40}")
        print(f"Espécie: {pet.especie}")
        print(f"Idade: {pet.idade} anos")
        print(f"Peso: {pet.peso:.2f} kg")
        status = "Hospedado" if pet.check_in else "Não hospedado"
        print(f"Status: {status}")
        print(f"{'='*40}\n")

def calcular_diaria(pets):
    pet = selecionar_pet(pets, "Digite o nome (ou parte do nome) do pet para calcular a diária: ")
    if pet:
        idade = pet.idade
        if idade <= 3:
            valor = 50.00
        elif 4 <= idade <= 10:
            valor = 60.00
        else:
            valor = 75.00
            
        print(f"O valor da diária para o pet '{pet.nome}' (Idade: {idade} anos) é: R$ {valor:.2f}")

"""======================= PERSISTÊNCIA EM JSON ==============================="""

# Procura a pasta real onde o script .py está guardado no seu disco
PASTA_ATUAL = os.path.dirname(os.path.abspath(__file__))
# Junta a pasta encontrada com o nome do arquivo, forçando a criação no local certo
CAMINHO_JSON = os.path.join(PASTA_ATUAL, "pets.json")

def criar_dados_iniciais():
    return [
        Pet("Thor", "Cachorro", 4, 15.3, True),
        Pet("Luna", "Gato", 2, 4.2, False), 
        Pet("Pipoca", "Calopsita", 11, 0.09, True) 
    ]

def salvar_em_json(pets):
    try:
        lista_dicts = [pet.para_dicionario() for pet in pets]
        with open(CAMINHO_JSON, "w", encoding="utf-8") as file:
            json.dump(lista_dicts, file, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar pets.json: {e}")

def carregar_de_json(pets):
    if not os.path.exists(CAMINHO_JSON):
        print("Arquivo 'pets.json' não encontrado. Gerando base inicial nesta pasta...")
        pets_iniciais = criar_dados_iniciais()
        salvar_em_json(pets_iniciais)
        pets.extend(pets_iniciais)
        return

    try:
        with open(CAMINHO_JSON, "r", encoding="utf-8") as file:
            lista_dicts = json.load(file)
            for dados in lista_dicts:
                pet = Pet.de_dicionario(dados)
                pets.append(pet)
    except Exception as e:
        print(f"Erro ao carregar pets.json: {e}")

if __name__ == "__main__":
    lista_pets = []
    menu(lista_pets)