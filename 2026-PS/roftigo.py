# Projeto: Sistema de Controle de Estoque
# Autor: Nickolas Kinceski Martins
# Data: 26/02/2026

print("\n______ SISTEMA DE CONTROLE DE ESTOQUE DO NICKOLAS______")

# Lista de produtos em estoque:
estoque = [
    {"Produto": "Gabriele"   , "Quantidade": 10, "Valor": 1500.0},
    {"Produto": "Rodrigo", "Quantidade": 500, "Valor": 0.30},
    {"Produto": "Nathlay", "Quantidade":  1, "Valor": 300000000000.0},
    {"Produto": "Mayara Milervas", "Quantidade":  7, "Valor":  450.0},
]

# Análise do estoque e exibição do status de cada produto
for itens in estoque:
    produto = itens["Produto"]
    quantidade = itens["Quantidade"]
    valor = itens["Valor"]
    # Diz o status do produto
    if quantidade < 5:
        status = "Crítico"
    elif quantidade >= 5 and quantidade < 20:
        status = "Adequado"
    elif quantidade >= 20:
        status = "Excesso"
    total = quantidade * valor
    print(f"Produto: {produto} Quantidade: {quantidade} Valor: R${valor:.2f} "
          f"Total: R${total:.2f} - Status: {status}")

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
        # valida o valor unitário
        while True:
            try:
                valor = float(input("\nDigite o valor unitário do produto (ex: 1999.90): ").replace(",","."))
                if valor < 0:
                    print("\nValor negativo não é permitido. Informe um número não‑negativo.")
                    continue
                break
            except ValueError:
                print("\nValor inválido. Por favor, digite um número para o valor.")
        estoque.append({"Produto": produto, "Quantidade": quantidade, "Valor": valor})
        print(f"\nO Produto '{produto}' foi adicionado com quantidade de {quantidade} "
              f"unidade(s) e valor de R${valor:.2f} cada.")

# Função para ver se o usuário deseja consultar o status de um produto específico
consultar = perguntar_sim_nao("\nDeseja consultar o status de um produto específico? (s (sim) / n (não)): ")
if consultar == "s":
    prod_consult = input("\nDigite o nome do produto que deseja consultar: ")
    for itens in estoque:
        if itens["Produto"].strip().lower() == prod_consult.strip().lower():
            prod_consult = itens["Produto"]
            quantidade = itens["Quantidade"]
            valor = itens["Valor"]
            if quantidade < 5:
                status = "Crítico"
            elif quantidade >= 5 and quantidade < 20:
                status = "Adequado"
            elif quantidade >= 20:
                status = "Excesso"
            total = quantidade * valor
            print(f"\nProduto: {prod_consult} |   Quantidade: {quantidade} | "
                  f"Valor: R${valor:.2f} | Total: R${total:.2f} - Status: {status}")
            break
    else:
        print(f"Produto '{prod_consult}' não encontrado no estoque.")

# =================== RELATÓRIO GERAL =============================
print("\n====== RELATÓRIO DO ESTOQUE DO NICKOLAS ======")
for itens in estoque:
    produto = itens["Produto"]
    quantidade = itens["Quantidade"]
    valor = itens["Valor"]
    # Diz o status do produto
    if quantidade < 5:
        status = "Crítico"
    elif quantidade >= 5 and quantidade < 20:
        status = "Adequado"
    elif quantidade >= 20:
        status = "Excesso"
    total = quantidade * valor
    print(f"Produto: {produto} |   Quantidade: {quantidade} | "
          f"Valor: R${valor:.2f} | Total: R${total:.2f} - Status: {status}")

# Exibição do produto com menor quantidade
if estoque:
    produto_menor = min(estoque, key=lambda x: x["Quantidade"])
    print(f"\nProduto com menor quantidade: {produto_menor['Produto']} - "
          f"Quantidade: {produto_menor['Quantidade']}")
print(f"\nCORRE COMPRAR O {produto_menor['Produto']} ANTES QUE ACABE!!")
# eNCERRAMENTO DO PROGRAMA
print("\n______ FIM DO SISTEMA DE CONTROLE DE ESTOQUE ______")
# Só pra dar as 100 linhas.