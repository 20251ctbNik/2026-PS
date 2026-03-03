# Projeto: Sistema de Controle de Estoque
# Autor: Nickolas Kinceski Martins
# Data: 26/02/2026

print("\n______ SISTEMA DE CONTROLE DE ESTOQUE______")

# Lista de produtos em estoque:
estoque = [
    {"Produto": "CPU Intel Core Ultra 9"   , "Quantidade": 10},
    {"Produto": "Memória RAM DDR 5 16GB", "Quantidade": 35},
    {"Produto": "GPU NVIDIA GeForce RTX 5090", "Quantidade":  2},
    {"Produto": "Gigabyte B760M Aorus Elite", "Quantidade":  7},
]

# Análise do estoque e exibição do status de cada produto
for itens in estoque:
    produto = itens["Produto"]
    quantidade = itens["Quantidade"]
    # Diz o status do produto
    if quantidade < 5:
        status = "Crítico"
    elif quantidade >= 5 and quantidade < 20:
        status = "Adequado"
    elif quantidade >= 20:
        status = "Excesso"
    print(f"Produto: {produto} Quantidade: {quantidade} - Status: {status}")

# função para perguntar sim ou não, com tratamento de erros
def perguntar_sim_nao(prompt):
    while True:
        try:
            resposta = input(prompt).strip().lower()
        except Exception:
            print("\nErro ao ler a entrada. Tente novamente.")
            continue
        if resposta in ("s", "n"):
            return resposta
        print("\nEntrada inválida. Por favor, digite 's' para sim ou 'n' para não.")

# Quer adicionar outro produto (um monitor Samsung Odyssey Neo G9 talvez)??
newproduto = "s"
while newproduto == "s":
    newproduto = perguntar_sim_nao("\nDeseja adicionar um novo produto? (s (sim) / n (não)): ")

    if newproduto == "s":
        produto = input("Digite o nome do produto: ")
        # valida se a quantidade é um número não-negativo
        while True:
            try:
                quantidade = int(input("\nDigite a quantidade do novo produto: "))
                if quantidade < 0:
                    print("\nQuantidade negativa não é permitida. Informe um número inteiro por favor.")
                    continue
                break
            except ValueError:
                print("\nQuantidade inválida. Por favor, digite um número inteiro para a quantidade.")
        estoque.append({"Produto": produto, "Quantidade": quantidade})  # Adiciona o novo produto à lista de estoque
        print(f"\nO Produto '{produto}' foi adicionado com quantidade de {quantidade} unidade(s).")

# Função para ver se o usuário deseja consultar o status de um produto específico
consultar = perguntar_sim_nao("\nDeseja consultar o status de um produto específico? (s (sim) / n (não)): ")
if consultar == "s":
    prod_consult = input("\nDigite o nome do produto que deseja consultar: ")
    for itens in estoque:
        if itens["Produto"].strip() == prod_consult.strip():
            prod_consult = itens["Produto"]
            quantidade = itens["Quantidade"]
            if quantidade < 5:
                status = "Crítico"
            elif quantidade >= 5 and quantidade < 20:
                status = "Adequado"
            elif quantidade >= 20:
                status = "Excesso"
            print(f"\nProduto: {prod_consult} |   Quantidade: {quantidade} - Status: {status}")
            break
    else:
        print(f"Produto '{prod_consult}' não encontrado no estoque.")

# =================== RELATÓRIO GERAL =============================
print("\n====== RELATÓRIO GERAL DO ESTOQUE ======")
for itens in estoque:
    produto = itens["Produto"]
    quantidade = itens["Quantidade"]
    # Diz o status do produto
    if quantidade < 5:
        status = "Crítico"
    elif quantidade >= 5 and quantidade < 20:
        status = "Adequado"
    elif quantidade >= 20:
        status = "Excesso"
    print(f"Produto: {produto} |   Quantidade: {quantidade} - Status: {status}")

# Exibição do produto com menor quantidade
if estoque:
    produto_menor = min(estoque, key=lambda x: x["Quantidade"])
    print(f"\nProduto com menor quantidade: {produto_menor['Produto']} - Quantidade: {produto_menor['Quantidade']}")

# eNCERRAMENTO DO PROGRAMA
print("\n______ FIM DO SISTEMA DE CONTROLE DE ESTOQUE ______")
# Só pra dar as 100 linhas.