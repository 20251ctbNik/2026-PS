# SysControl v2.0 — Produto

Atividade de Programação Orientada a Objetos: classes, encapsulamento e validação.

## 📌 Variante escolhida

Entidade: **Produto**

Atributos:
- `nome` (String)
- `codigo` (String)
- `preco` (double)
- `quantidadeEstoque` (int)

## 🔒 Encapsulamento

Todos os atributos são `private`. O acesso externo acontece apenas por:
- **Getters**: `getNome()`, `getCodigo()`, `getPreco()`, `getQuantidadeEstoque()`
- **Setters** (apenas onde faz sentido alterar diretamente): `setPreco()`, `setQuantidadeEstoque()`
  - `nome` e `codigo` não têm setter, pois representam a identidade do produto e não devem ser alterados livremente após a criação.

## ✅ Validações implementadas

1. Nome não pode ser vazio.
2. Código não pode ser vazio.
3. Preço não pode ser negativo.
4. Quantidade em estoque não pode ser negativa.

Essas validações são aplicadas tanto no construtor quanto nos setters, para garantir que nenhum objeto exista em estado inválido.

## ⚙️ Métodos de comportamento

- `venderUnidades(int quantidade)`: reduz o estoque do produto. Recusa a operação (retorna `false`) se a quantidade solicitada for maior que o estoque disponível.
- `aplicarDesconto(double percentual)`: aplica um desconto percentual ao preço. Recusa (retorna `false`) se o percentual for menor que 0 ou maior que 100.

## 🧩 Desafios complementares escolhidos

1. **Método de resumo textual** — `resumo()`: retorna uma descrição formatada do produto (código, nome, preço e estoque).
2. **Comparação entre objetos** — `compararPorPreco(Produto outro)`: compara dois produtos pelo preço, retornando negativo, positivo ou zero.

Também foi implementado um **construtor alternativo** com menos parâmetros (`Produto(nome, codigo, preco)`), que cria o produto com estoque inicial zero.

## 🧪 Personalização dos testes

Conforme exigido no enunciado:
- **Dia de nascimento (11)** usado na quantidade de estoque do produto `p3` (Monitor 24 polegadas).
- **Duas primeiras letras do nome ("Ni")** usadas no código do produto `p3` (`NI003`).

## 📋 Casos de teste executados

| Teste | Ação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| 1 | Criar 3 objetos com dados válidos | Objetos criados e exibidos | ✅ |
| 2 | Criar produto com nome vazio | Alteração recusada (exceção lançada) | ✅ |
| 3 | Definir preço negativo via `setPreco()` | Alteração recusada, estado preservado | ✅ |
| 4 | Vender 10 unidades (estoque suficiente) | Estoque reduzido corretamente | ✅ |
| 5 | Vender 500 unidades (estoque insuficiente) | Operação recusada, estado preservado | ✅ |

## ▶️ Como executar

```bash
javac Produto.java Main.java
java Main
```

## 📸 Exemplo de execução

*(Substitua esta seção pela captura de tela real da execução dos 5 testes antes de entregar.)*

```
===== TESTE 1: Criar objetos com dados válidos =====
Produto[codigo=COD001, nome=Teclado Mecânico, preco=R$ 250.00, estoque=15 un.]
Produto[codigo=COD002, nome=Mouse Gamer, preco=R$ 120.50, estoque=30 un.]
Produto[codigo=NI003, nome=Monitor 24 polegadas, preco=R$ 899.90, estoque=11 un.]
...
```

## 📦 Histórico de commits

1. Criação do projeto e da classe `Produto`
2. Atributos privados e construtor
3. Getters, setters e validações
4. Métodos de comportamento (`venderUnidades`, `aplicarDesconto`)
5. Classe `Main` e casos de teste
6. Desafios complementares (resumo e comparação) + correções e README