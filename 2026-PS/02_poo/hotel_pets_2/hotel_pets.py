import os

class Pet:
    def __init__(self, nome, especie, idade, peso=0.0):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.peso = peso
        self.check_in = False

def ler_inteiro(mensagem):
    """Garante que o usuário digite um número inteiro válido e positivo."""
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
    """Garante que o usuário digite um número decimal válido e positivo."""
    while True:
        try:
            valor = float(input(mensagem).replace(',', '.'))  # Aceita vírgula também
            if valor < 0:
                print("Por favor, digite um número maior ou igual a zero.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida! Por favor, digite um número decimal (ex: 12.5).")

def ler_string(mensagem):
    """Garante que o usuário não deixe o campo em branco."""
    while True:
        valor = input(mensagem).strip()
        if not valor:
            print("Este campo não pode ficar vazio. Tente novamente.")
            continue
        return valor

# --- MENU PRINCIPAL ---

def menu(pets):
    if os.path.exists("pets.bin"):
        carregar_de_binario(pets)
    else:
        carregar_de_txt(pets)

    while True:
        print("\n============= Hotel Pet =============")
        print("1  - Cadastrar um Pet.")
        print("2  - Listar os Pets.")
        print("3  - Calcular a diária do pet.")
        print("4  - Salvar em .txt.")
        print("5  - Salvar em binário.")
        print("6  - Atualizar peso do pet.")
        print("7  - Check-in.")
        print("8  - Check-out.")
        print("9  - Buscar por pet.")
        print("10 - Relatório de pets hospedados.")
        print("11 - Resumo individual do pet.")
        print("12 - Sair.")
        print("====================================")
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar(pets)
        elif opcao == "2":
            listar_pet(pets)
        elif opcao == "3":
            calcular_diaria(pets)
        elif opcao == "4":
            salvarecarregar_em_txt(pets)
        elif opcao == "5":
            salvarecarregar_em_binario(pets)
        elif opcao == "6":
            atualizar_peso(pets)
        elif opcao == "7":
            registrar_entrada(pets)
        elif opcao == "8":
            registrar_saida(pets)
        elif opcao == "9":
            buscar_pet(pets)
        elif opcao == "10":
            relatorio_pets(pets)
        elif opcao == "11":
            resumo_individual(pets)
        elif opcao == "12":
            salvarecarregar_em_txt(pets)
            salvarecarregar_em_binario(pets)
            print("Saindo do programa. Até mais!")
            break
        else:
            print("\nOpção inválida. Tente novamente com um número de 1 a 12.")

"""======================================= Funções do Sistema ========================================================"""

def cadastrar(pets):
    print("\n--- Cadastro de Pet ---")
    nome = ler_string("Digite o nome do pet: ")
    especie = ler_string("Digite a espécie do pet: ")
    idade = ler_inteiro("Digite a idade do pet (anos): ")
    peso = ler_float("Digite o peso do pet (kg): ")
    
    pet = Pet(nome, especie, idade, peso)
    pets.append(pet)
    print(f"\nPet '{nome}' cadastrado com sucesso!")

def listar_pet(pets):
    if not pets:
        print("\nNenhum pet cadastrado.")
        return
    print("\nLista de Pets Cadastrados:")
    for idx, pet in enumerate(pets, start=1):
        print(f"{idx}. Nome: {pet.nome}, Espécie: {pet.especie}, Idade: {pet.idade} anos, Peso: {pet.peso:.2f} kg")

def atualizar_peso(pets):
    nome = ler_string("Digite o nome do pet para atualizar o peso: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            novo_peso = ler_float(f"Digite o novo peso para {pet.nome} (kg): ")
            pet.peso = novo_peso
            print(f"Peso do pet '{pet.nome}' atualizado para {novo_peso:.2f} kg.")
            return
    print(f"Pet '{nome}' não encontrado.")

def registrar_entrada(pets):
    nome = ler_string("Digite o nome do pet para check-in: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            if pet.check_in:
                print(f"O pet '{pet.nome}' já está hospedado.")
                return
            pet.check_in = True
            print(f"Pet '{pet.nome}' fez check-in com sucesso!")
            return
    print(f"Pet '{nome}' não encontrado.")

def registrar_saida(pets):
    nome = ler_string("Digite o nome do pet para check-out: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            if not pet.check_in:
                print(f"O pet '{pet.nome}' não está hospedado no momento.")
                return
            pet.check_in = False
            print(f"Pet '{pet.nome}' fez check-out com sucesso!")
            return
    print(f"Pet '{nome}' não encontrado.")

def buscar_pet(pets):
    termo = ler_string("Digite o nome (ou parte do nome) do pet: ").lower()
    encontrados = False

    print(f"\nResultados para '{termo}':")
    for pet in pets:
        if termo in pet.nome.lower():
            status = "Presente" if pet.check_in else "Saiu/Não hospedado"
            print(f"- Nome: {pet.nome} | Espécie: {pet.especie} | Idade: {pet.idade} anos [{status}]")
            encontrados = True
    
    if not encontrados:
        print(f"Nenhum pet encontrado com o termo '{termo}'.")

def relatorio_pets(pets):
    hospedados = [pet for pet in pets if pet.check_in]
    if not hospedados:
        print("\nNenhum pet hospedado no momento.")
        return
    print("\nRelatório de Pets Hospedados:")
    for pet in hospedados:
        print(f"Nome: {pet.nome}, Espécie: {pet.especie}, Idade: {pet.idade} anos, Peso: {pet.peso:.2f} kg")
        
def resumo_individual(pets):
    nome = ler_string("Digite o nome do pet para resumo individual: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            print(f"\n{'='*40}")
            print(f"Resumo do Pet '{pet.nome}'")
            print(f"{'='*40}")
            print(f"Espécie: {pet.especie}")
            print(f"Idade: {pet.idade} anos")
            print(f"Peso: {pet.peso:.2f} kg")
            status = "Hospedado" if pet.check_in else "Não hospedado"
            print(f"Status: {status}")
            print(f"{'='*40}\n")
            return
    print(f"Pet '{nome}' não encontrado.")

def calcular_diaria(pets):
    nome = ler_string("Digite o nome do pet para calcular a diária: ")
    for pet in pets:
        if pet.nome.lower() == nome.lower():
            idade = pet.idade
            if idade <= 3:
                valor = 50.00
            elif 4 <= idade <= 10:
                valor = 60.00
            else:
                valor = 75.00
            
            if idade > 30:
                print("Nota: Este pet tem uma idade muito avançada registrada.")
                
            print(f"O valor da diária para o pet '{pet.nome}' (Idade: {idade} anos) é: R$ {valor:.2f}")
            return
    print(f"Pet '{nome}' não encontrado.")

"""======================= Arquivos e Persistência ==============================="""

def salvarecarregar_em_txt(pets):
    try:
        with open("pets.txt", "w", encoding="utf-8") as file:
            for pet in pets:
                file.write(f"{pet.nome},{pet.especie},{pet.idade},{pet.peso},{pet.check_in}\n")
        print("Pets salvos em 'pets.txt' com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar pets.txt: {e}")

def carregar_de_txt(pets):
    if os.path.exists("pets.txt"):
        try:
            with open("pets.txt", "r", encoding="utf-8") as file:
                for linha in file.readlines():
                    if linha.strip():
                        dados = linha.strip().split(",")
                        if len(dados) >= 5:
                            pet = Pet(dados[0], dados[1], int(dados[2]), float(dados[3]))
                            pet.check_in = dados[4].lower() == "true"
                            if pet.nome.lower() not in [p.nome.lower() for p in pets]:
                                pets.append(pet)
        except Exception as e:
            print(f"Erro ao carregar pets.txt: {e}")

def salvarecarregar_em_binario(pets):
    try:
        with open("pets.bin", "wb") as file:
            for pet in pets:
                file.write(f"{pet.nome},{pet.especie},{pet.idade},{pet.peso},{pet.check_in}\n".encode('utf-8'))
        print("Pets salvos em 'pets.bin' com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar pets.bin: {e}")

def carregar_de_binario(pets):
    if os.path.exists("pets.bin"):
        try:
            with open("pets.bin", "rb") as file:
                for linha in file.readlines():
                    if linha.strip():
                        dados = linha.decode('utf-8').strip().split(",")
                        if len(dados) >= 5:
                            pet = Pet(dados[0], dados[1], int(dados[2]), float(dados[3]))
                            pet.check_in = dados[4].lower() == "true"
                            if pet.nome.lower() not in [p.nome.lower() for p in pets]:
                                pets.append(pet)
        except Exception as e:
            print(f"Erro ao carregar pets.bin: {e}")

if __name__ == "__main__":
    lista_pets = []
    menu(lista_pets)