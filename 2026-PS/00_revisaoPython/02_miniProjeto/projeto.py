# =================================================================
# Sistema de Controle de Estoque
# Equipe: Knockin' On Haven's Door
# Descrição: Sistema para gerenciar produtos de um depósito
# =================================================================

# ================= BASE DE DADOS =================
# Lista de dicionários que representa o estoque
# Cada produto possui: nome, valor, quantidade e código único

estoque = [
    {"produto": "Computador Pichau Gamer", "valor": 12000, "quantidade": 30, "codigo": 1},
    {"produto": "Headset Gamer Logtec G Astro A50 X LIGHTSPEED", "valor": 2200, "quantidade": 120, "codigo": 2},
    {"produto": "Razer Huntsman V3 Pro Tenkeyless", "valor": 2500, "quantidade": 100, "codigo": 3},
    {"produto": "Mouse Gamer Razer Viper Mini Signature", "valor": 5200, "quantidade": 50, "codigo": 4},
    {"produto": "Monitor Gamer Curvo Samsung Odyssey Ark 55''", "valor": 17000, "quantidade": 30, "codigo": 5},
]

# Variáveis globais para controle de movimentação do estoque
entrada_total = 0  # Soma de todos os produtos adicionados
saida_total = 0    # Soma de todos os produtos retirados


# ================= FUNÇÕES AUXILIARES =================

def ler_int(mensagem):
    """
    Função para garantir que o usuário digite um número inteiro válido.
    Também impede valores negativos.
    """
    while True:
        try:
            valor = int(input(mensagem))  # tenta converter para inteiro

            if valor < 0:
                print("❌ Digite um número positivo.")
            else:
                return valor  # retorna apenas se for válido

        except ValueError:
            # Caso o usuário digite letras ou algo inválido
            print("❌ Entrada inválida. Digite um número inteiro.")


def ler_float(mensagem):
    """
    Função para leitura de números com casas decimais (preços).
    Também valida entrada e impede valores negativos.
    """
    while True:
        try:
            valor = float(input(mensagem))

            if valor < 0:
                print("❌ Digite um valor positivo.")
            else:
                return valor

        except ValueError:
            print("❌ Entrada inválida. Digite um número válido.")


def buscar_produto(codigo):
    """
    Procura um produto dentro da lista de estoque pelo código.
    Retorna o produto se encontrado, ou None se não existir.
    """
    for item in estoque:
        if item["codigo"] == codigo:
            return item
    return None


# ================= MENU PRINCIPAL =================

def menu():
    """
    Função principal do sistema.
    Exibe o menu e direciona para as funcionalidades.
    """
    while True:
        print("\n" + "=" * 50)
        print("📦 SISTEMA DE ESTOQUE")
        print("1 - Listar produtos")
        print("2 - Consultar produto")
        print("3 - Solicitar produto")
        print("4 - Adicionar produto")
        print("5 - Relatório geral")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        # Direcionamento para cada funcionalidade
        if opcao == "1":
            listar_produtos()
        elif opcao == "2":
            consultar_produto()
        elif opcao == "3":
            solicitar_produto()
        elif opcao == "4":
            adicionar_produto()
        elif opcao == "5":
            relatorio()
        elif opcao == "0":
            print("Encerrando sistema...")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")


# ================= LISTAGEM =================

def listar_produtos():
    """
    Mostra todos os produtos cadastrados no estoque.
    """
    print("\n📋 LISTA DE PRODUTOS")

    for item in estoque:
        print(f"Código: {item['codigo']} | {item['produto']} | R$ {item['valor']} | Qtd: {item['quantidade']}")


# ================= CONSULTA =================

def consultar_produto():
    """
    Permite consultar um produto específico pelo código.
    """
    codigo = ler_int("Digite o código do produto: ")

    produto = buscar_produto(codigo)

    if produto:
        print(f"\nProduto: {produto['produto']}")
        print(f"Valor: R$ {produto['valor']}")
        print(f"Quantidade: {produto['quantidade']}")
    else:
        print("❌ Produto não encontrado.")

# ================= SAÍDA DE PRODUTO =================

def solicitar_produto():
    """
    Realiza a retirada de produtos do estoque.
    Diminui a quantidade disponível.
    """
    global saida_total  # permite alterar variável global

    codigo = ler_int("Código do produto: ")
    produto = buscar_produto(codigo)

    if produto:
        qtd = ler_int("Quantidade: ")

        if qtd == 0:
            print("❌ Quantidade não pode ser zero.")
            return

        # Verifica se há estoque suficiente
        if qtd <= produto["quantidade"]:
            produto["quantidade"] -= qtd  # diminui estoque
            saida_total += qtd           # soma na saída total
            print("✅ Produto retirado do estoque.")
        else:
            print("❌ Estoque insuficiente.")
    else:
        print("❌ Produto não encontrado.")


# ================= ENTRADA DE PRODUTO =================

def adicionar_produto():
    """
    Adiciona produtos ao estoque.
    Pode:
    - Aumentar quantidade de um produto existente
    - Cadastrar um novo produto
    """
    global entrada_total

    codigo = ler_int("Código do produto: ")
    produto = buscar_produto(codigo)

    if produto:
        # Produto já existe → apenas adiciona quantidade
        qtd = ler_int("Quantidade a adicionar: ")

        if qtd == 0:
            print("❌ Quantidade não pode ser zero.")
            return

        produto["quantidade"] += qtd
        entrada_total += qtd
        print("✅ Estoque atualizado.")

    else:
        # Produto novo → cadastra no sistema
        print("📦 Produto novo!")

        nome = input("Nome do produto: ").strip()

        # Validação de nome vazio
        while nome == "":
            print("❌ Nome não pode ser vazio.")
            nome = input("Nome do produto: ").strip()

        valor = ler_float("Valor: ")
        qtd = ler_int("Quantidade: ")

        if qtd == 0:
            print("❌ Quantidade não pode ser zero.")
            return

        # Adiciona novo produto na lista
        estoque.append({
            "produto": nome,
            "valor": valor,
            "quantidade": qtd,
            "codigo": codigo
        })

        entrada_total += qtd
        print("✅ Produto cadastrado com sucesso!")


# ================= RELATÓRIO =================

def relatorio():
    """
    Exibe um resumo geral do sistema:
    - Total de entradas
    - Total de saídas
    - Produtos com baixo estoque
    """
    print("\n📊 RELATÓRIO GERAL")

    print(f"Total de entradas: {entrada_total}")
    print(f"Total de saídas: {saida_total}")

    print("\n⚠ Produtos com baixo estoque (<= 10):")

    baixo = False  # controle para saber se encontrou algum

    for item in estoque:
        if item["quantidade"] <= 10:
            print(f"{item['produto']} | Qtd: {item['quantidade']}")
            baixo = True

    if not baixo:
        print("Nenhum produto com estoque baixo.")


# ================= INÍCIO DO SISTEMA =================

# Chamada da função principal
menu()