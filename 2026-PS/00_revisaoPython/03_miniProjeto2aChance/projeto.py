# =================================================================
# Sistema de Controle de Estoque
# Alunos: Nickolas Kinceski, Gustavo Koller e Mateus Felix
# Descrição: Sistema para gerenciar produtos de uma loja de carros
# =================================================================

import os

ARQUIVO = os.path.join(os.path.dirname(__file__), "estoque.txt")

# ================= CARREGAR ESTOQUE =================
def carregar_estoque():
    estoque = []
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                nome, qtd, valor = linha.strip().split(",")
                estoque.append({
                    "Produto": nome,
                    "Quantidade": int(qtd),
                    "Valor": float(valor)
                })
    except FileNotFoundError:
        print("📂 Primeiro uso: criando estoque inicial...")

        # Estoque padrão (só na primeira vez)
        estoque = [
            {"Produto": "Lamborghini", "Quantidade": 0, "Valor": 2000000},
            {"Produto": "Peugeot do Ventura", "Quantidade": 1, "Valor": 100000000000},
            {"Produto": "Ferrari", "Quantidade": 20, "Valor": 1500000},
            {"Produto": "BMW X6", "Quantidade": 50, "Valor": 500000},
            {"Produto": "Aston Martin Vantage", "Quantidade": 10, "Valor": 500000},
        ]

        salvar_estoque(estoque)

    return estoque


# ================= SALVAR ESTOQUE =================
def salvar_estoque(estoque):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for item in estoque:
            arquivo.write(f"{item['Produto']},{item['Quantidade']},{item['Valor']}\n")


# ================= STATUS =================
def calcular_status(qtd):
    if qtd < 5:
        return "Crítico"
    elif qtd < 20:
        return "Adequado"
    else:
        return "Excesso"


# ================= FUNÇÃO SIM/NÃO =================
def perguntar_sim_nao(msg):
    while True:
        resp = input(msg).strip().lower()
        if resp in ("s", "n"):
            return resp
        print("❌ Digite 's' ou 'n'.")


# ================= MENU =================
def menu():
    estoque = carregar_estoque()

    print("\n______ SISTEMA DE CONTROLE DE ESTOQUE______")

    while True:
        print("\n====== MENU ======")
        print("1 - Ver estoque")
        print("2 - Adicionar produto")
        print("3 - Consultar produto")
        print("4 - Relatório")
        print("0 - Sair")

        op = input("Escolha: ")

        # ================= LISTAR =================
        if op == "1":
            if not estoque:
                print("Estoque vazio.")
            else:
                for item in estoque:
                    status = calcular_status(item["Quantidade"])
                    total = item["Quantidade"] * item["Valor"]

                    print(f"{item['Produto']} | Qtd: {item['Quantidade']} | "
                          f"R${item['Valor']:.2f} | Total: R${total:.2f} | {status}")

        # ================= ADICIONAR =================
        elif op == "2":
            nome = input("Nome do produto: ").strip()

            while True:
                try:
                    qtd = int(input("Quantidade: "))
                    if qtd < 0:
                        print("❌ Não pode ser negativo.")
                        continue
                    break
                except:
                    print("❌ Digite um número.")

            while True:
                try:
                    valor = float(input("Valor: ").replace(",", "."))
                    if valor < 0:
                        print("❌ Não pode ser negativo.")
                        continue
                    break
                except:
                    print("❌ Digite um valor válido.")

            estoque.append({
                "Produto": nome,
                "Quantidade": qtd,
                "Valor": valor
            })

            salvar_estoque(estoque)
            print("✅ Produto salvo no estoque!")

        # ================= CONSULTAR =================
        elif op == "3":
            busca = input("Nome do produto: ").strip().lower()

            for item in estoque:
                if item["Produto"].lower() == busca:
                    status = calcular_status(item["Quantidade"])
                    total = item["Quantidade"] * item["Valor"]

                    print(f"\n{item['Produto']} | Qtd: {item['Quantidade']} | "
                          f"R${item['Valor']:.2f} | Total: R${total:.2f} | {status}")
                    break
            else:
                print("❌ Produto não encontrado.")

        # ================= RELATÓRIO =================
        elif op == "4":
            print("\n📊 RELATÓRIO GERAL")

            for item in estoque:
                status = calcular_status(item["Quantidade"])
                print(f"{item['Produto']} | Qtd: {item['Quantidade']} | {status}")

            if estoque:
                menor = min(estoque, key=lambda x: x["Quantidade"])
                print(f"\n⚠ Menor estoque: {menor['Produto']} ({menor['Quantidade']})")

        # ================= SAIR =================
        elif op == "0":
            salvar_estoque(estoque)
            print("💾 Dados salvos. Saindo do sistema...")
            break

        else:
            print("❌ Opção inválida.")


# ================= EXECUÇÃO =================
menu()